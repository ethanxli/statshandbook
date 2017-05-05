import numpy as np
import scipy.optimize
from scipy import linalg




# blacklitterman
#   This function performs the Black-Litterman blending of the prior
#   and the views into a new posterior estimate of the returns as
#   described in the paper by He and Litterman.
# Inputs
#   delta  - Risk tolerance from the equilibrium portfolio
#   weq    - Weights of the assets in the equilibrium portfolio
#   sigma  - Prior covariance matrix
#   tau    - Coefficiet of uncertainty in the prior estimate of the mean (pi)
#   P      - Pick matrix for the view(s)
#   Q      - Vector of view returns
#   Omega  - Matrix of variance of the views (diagonal)
# Outputs
#   Er     - Posterior estimate of the mean returns
#   w      - Unconstrained weights computed given the Posterior estimates
#            of the mean and covariance of returns.
#   lambda - A measure of the impact of each view on the posterior estimates.
class RiskMngr():
    def __init__(self, tau):
        self.tau = tau

    def setViews(self, P, Q):
        self.P = P
        self.Q = Q



    def blacklitterman(delta, weq, sigma, tau, P, Q, Omega):
        # Reverse optimize and back out the equilibrium returns
        pi = weq.dot(sigma * delta)
        print(pi)
        # We use tau * sigma many places so just compute it once
        ts = tau * sigma
        # Compute posterior estimate of the mean
        # This is a simplified version of formula (8) on page 4.
        middle = linalg.inv(np.dot(np.dot(P,ts),P.T) + Omega)
        print(middle)
        print(Q-np.expand_dims(np.dot(P,pi.T),axis=1))
        er = np.expand_dims(pi,axis=0).T + np.dot(np.dot(np.dot(ts,P.T),middle),(Q - np.expand_dims(np.dot(P,pi.T),axis=1)))
        # Compute posterior estimate of the uncertainty in the mean
        # This is a simplified and combined version of formulas (9) and (15)
        posteriorSigma = sigma + ts - ts.dot(P.T).dot(middle).dot(P).dot(ts)
        print(posteriorSigma)
        # Compute posterior weights based on uncertainty in mean
        w = er.T.dot(linalg.inv(delta * posteriorSigma)).T
        # Compute lambda value
        # We solve for lambda from formula (17) page 7, rather than formula (18)
        # just because it is less to type, and we've already computed w*.
        lmbda = np.dot(linalg.pinv(P).T,(w.T * (1 + tau) - weq).T)
        return [er, w, lmbda]


#################################################################
#################################################################
# Keep track of leverage and long/short exposure


class ExposureMngr(object):

    def __init__(self, target_leverage = 1.0, target_long_exposure_perc = 0.50, target_short_exposure_perc = 0.50):
        self.target_leverage            = target_leverage
        self.target_long_exposure_perc  = target_long_exposure_perc
        self.target_short_exposure_perc = target_short_exposure_perc
        self.short_exposure             = 0.0
        self.long_exposure              = 0.0
        self.open_order_short_exposure  = 0.0
        self.open_order_long_exposure   = 0.0

    def get_current_leverage(self, context, consider_open_orders = True):
        curr_cash = context.portfolio.cash - (self.short_exposure * 2)
        if consider_open_orders:
            curr_cash -= self.open_order_short_exposure
            curr_cash -= self.open_order_long_exposure
        curr_leverage = (context.portfolio.portfolio_value - curr_cash) / context.portfolio.portfolio_value
        return curr_leverage

    def get_exposure(self, context, consider_open_orders = True):
        long_exposure, short_exposure = self.get_long_short_exposure(context, consider_open_orders)
        return long_exposure + short_exposure

    def get_long_short_exposure(self, context, consider_open_orders = True):
        long_exposure         = self.long_exposure
        short_exposure        = self.short_exposure
        if consider_open_orders:
            long_exposure  += self.open_order_long_exposure
            short_exposure += self.open_order_short_exposure
        return (long_exposure, short_exposure)

    def get_long_short_exposure_pct(self, context, consider_open_orders = True, consider_unused_cash = True):
        long_exposure, short_exposure = self.get_long_short_exposure(context, consider_open_orders)
        total_cash = long_exposure + short_exposure
        if consider_unused_cash:
            total_cash += self.get_available_cash(context, consider_open_orders)
        long_exposure_pct   = long_exposure  / total_cash if total_cash > 0 else 0
        short_exposure_pct  = short_exposure / total_cash if total_cash > 0 else 0
        return (long_exposure_pct, short_exposure_pct)

    def get_available_cash(self, context, consider_open_orders = True):
        curr_cash = context.portfolio.cash - (self.short_exposure * 2.0)
        if consider_open_orders:
            curr_cash -= self.open_order_short_exposure
            curr_cash -= self.open_order_long_exposure
        leverage_cash = context.portfolio.portfolio_value * (self.target_leverage - 1.0)
        return curr_cash + leverage_cash

    def get_available_cash_long_short(self, context, consider_open_orders = True):
        total_available_cash  = self.get_available_cash(context, consider_open_orders)
        long_exposure         = self.long_exposure
        short_exposure        = self.short_exposure
        if consider_open_orders:
            long_exposure  += self.open_order_long_exposure
            short_exposure += self.open_order_short_exposure
        current_exposure       = long_exposure + short_exposure + total_available_cash
        target_long_exposure  = current_exposure * self.target_long_exposure_perc
        target_short_exposure = current_exposure * self.target_short_exposure_perc
        long_available_cash   = target_long_exposure  - long_exposure
        short_available_cash  = target_short_exposure - short_exposure
        return (long_available_cash, short_available_cash)

    def update(self, context, data):
        #
        # calculate cash needed to complete open orders
        #
        self.open_order_short_exposure  = 0.0
        self.open_order_long_exposure   = 0.0
        for stock, orders in  get_open_orders().iteritems():
            price = data.current(stock, 'price')
            if price == np.NaN:
                continue
            amount = 0 if stock not in context.portfolio.positions else context.portfolio.positions[stock].amount
            for oo in orders:
                order_amount = oo.amount - oo.filled
                if order_amount < 0 and amount <= 0:
                    self.open_order_short_exposure += (price * -order_amount)
                elif order_amount > 0 and amount >= 0:
                    self.open_order_long_exposure  += (price * order_amount)

        #
        # calculate long/short positions exposure
        #
        self.short_exposure = 0.0
        self.long_exposure  = 0.0
        for stock, position in context.portfolio.positions.iteritems():
            amount = position.amount
            last_sale_price = position.last_sale_price
            if amount < 0:
                self.short_exposure += (last_sale_price * -amount)
            elif amount > 0:
                self.long_exposure  += (last_sale_price * amount)

#################################################################
#################################################################
#################################################################
#################################################################




def find_max_min(prices):
    prices_ = prices.copy()
    prices_.index = linspace(1., len(prices_), len(prices_))
    kr = KernelReg([prices_.values], [prices_.index.values], var_type='c', bw=[1.8,1])
    f = kr.fit([prices_.index.values])
    smooth_prices = pd.Series(data=f[0], index=prices.index)

    local_max = argrelextrema(smooth_prices.values, np.greater)[0]
    local_min = argrelextrema(smooth_prices.values, np.less)[0]

    price_local_max_dt = []
    for i in local_max:
        if (i>1) and (i<len(prices)-1):
            price_local_max_dt.append(prices.iloc[i-2:i+2].argmax())

    price_local_min_dt = []
    for i in local_min:
        if (i>1) and (i<len(prices)-1):
            price_local_min_dt.append(prices.iloc[i-2:i+2].argmin())

    prices.name = 'price'
    maxima = pd.DataFrame(prices.loc[price_local_max_dt])
    minima = pd.DataFrame(prices.loc[price_local_min_dt])
    max_min = pd.concat([maxima, minima]).sort_index()
    max_min.index.name = 'date'
    max_min = max_min.reset_index()
    max_min = max_min[~max_min.date.duplicated()]
    p = prices.reset_index()
    max_min['day_num'] = p[p['index'].isin(max_min.date)].index.values
    max_min = max_min.set_index('day_num').price

    return max_min


def find_patterns(max_min):
    patterns = defaultdict(list)

    for i in range(5, len(max_min)+1):
        window = max_min.iloc[i-5:i]

        # pattern must play out in less than 36 days
        if window.index[-1] - window.index[0] > 35:
            continue

        # Using the notation from the paper to avoid mistakes
        e1 = window.iloc[0]
        e2 = window.iloc[1]
        e3 = window.iloc[2]
        e4 = window.iloc[3]
        e5 = window.iloc[4]

        rtop_g1 = np.mean([e1,e3,e5])
        rtop_g2 = np.mean([e2,e4])
        # Head and Shoulders
        if (e1 > e2) and (e3 > e1) and (e3 > e5) and \
            (abs(e1 - e5) <= 0.03*np.mean([e1,e5])) and \
            (abs(e2 - e4) <= 0.03*np.mean([e1,e5])):
                patterns['HS'].append((window.index[0], window.index[-1]))

        # Inverse Head and Shoulders
        elif (e1 < e2) and (e3 < e1) and (e3 < e5) and \
            (abs(e1 - e5) <= 0.03*np.mean([e1,e5])) and \
            (abs(e2 - e4) <= 0.03*np.mean([e1,e5])):
                patterns['IHS'].append((window.index[0], window.index[-1]))

        # Broadening Top
        elif (e1 > e2) and (e1 < e3) and (e3 < e5) and (e2 > e4):
            patterns['BTOP'].append((window.index[0], window.index[-1]))

        # Broadening Bottom
        elif (e1 < e2) and (e1 > e3) and (e3 > e5) and (e2 < e4):
            patterns['BBOT'].append((window.index[0], window.index[-1]))

        # Triangle Top
        elif (e1 > e2) and (e1 > e3) and (e3 > e5) and (e2 < e4):
            patterns['TTOP'].append((window.index[0], window.index[-1]))

        # Triangle Bottom
        elif (e1 < e2) and (e1 < e3) and (e3 < e5) and (e2 > e4):
            patterns['TBOT'].append((window.index[0], window.index[-1]))

        # Rectangle Top
        elif (e1 > e2) and (abs(e1-rtop_g1)/rtop_g1 < 0.0075) and \
            (abs(e3-rtop_g1)/rtop_g1 < 0.0075) and (abs(e5-rtop_g1)/rtop_g1 < 0.0075) and \
            (abs(e2-rtop_g2)/rtop_g2 < 0.0075) and (abs(e4-rtop_g2)/rtop_g2 < 0.0075) and \
            (min(e1, e3, e5) > max(e2, e4)):

            patterns['RTOP'].append((window.index[0], window.index[-1]))

        # Rectangle Bottom
        elif (e1 < e2) and (abs(e1-rtop_g1)/rtop_g1 < 0.0075) and \
            (abs(e3-rtop_g1)/rtop_g1 < 0.0075) and (abs(e5-rtop_g1)/rtop_g1 < 0.0075) and \
            (abs(e2-rtop_g2)/rtop_g2 < 0.0075) and (abs(e4-rtop_g2)/rtop_g2 < 0.0075) and \
            (max(e1, e3, e5) > min(e2, e4)):
            patterns['RBOT'].append((window.index[0], window.index[-1]))

    return patterns


def _pattern_identification(prices, indentification_lag):
    max_min = find_max_min(prices)

    # we are only interested in the last pattern (if multiple patterns are there)
    # and also the last min/max must have happened less than "indentification_lag"
    # days ago otherways it mush have already been identified or it is too late to be usefull
    max_min_last_window = None

    for i in reversed(range(len(max_min))):
        if (prices.index[-1] - max_min.index[i]) == indentification_lag:
            max_min_last_window = max_min.iloc[i-4:i+1]
            break

    if max_min_last_window is None:
        return np.nan

    # possibly identify a pattern in the selected window
    patterns = find_patterns(max_min_last_window)
    if len(patterns) != 1:
        return np.nan

    name, start_end_day_nums = patterns.iteritems().next()

    pattern_code = {
           'HS'   : -2,
           'IHS'  : 2,
           'BTOP' : -1,
           'BBOT' : 1,
           'TTOP' : -4,
           'TBOT' : 4,
           'RTOP' : -3,
           'RBOT' : 3,
    }

    return pattern_code[name]


class PatternFactor(CustomFactor):

    params = ('indentification_lag',)
    inputs = [USEquityPricing.close]
    window_length = 40

    def compute(self, today, assets, out, close, indentification_lag):
        prices = pd.DataFrame(close, columns=assets)
        out[:] = prices.apply(_pattern_identification, args=(indentification_lag,))



def make_pipeline(context):
    """
    Create and return our pipeline.
    """
    pipe = Pipeline()

    #
    # Screen out penny stocks and low liquidity securities.
    #
    price = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=22)
    volume = SimpleMovingAverage(inputs=[USEquityPricing.volume], window_length=22)
    price_filter   = (price >= 5.0)
    volume_filter  = (volume >= 200 * 60 * 6.30)

    dollar_volume = AverageDollarVolume(window_length=20, mask=(price_filter&volume_filter))
    dollar_volume_filter = dollar_volume.top(500)

    full_filter = dollar_volume_filter
    pipe.set_screen(full_filter)

    #
    # Add factors
    #
    pattern = PatternFactor(mask=full_filter, window_length = 42, indentification_lag=1)

    pipe.add(pattern, "pattern")

    return pipe



# Put any initialization logic here. The context object will be passed to
# the other methods in your algorithm.
def initialize(context):
    set_commission(commission.PerShare(cost=0.00, min_trade_cost=0))

    #
    # Algo configuration
    #
    context.dont_buys = security_lists.leveraged_etf_list
    set_do_not_order_list(context.dont_buys)

    context.exposure = ExposureMngr(target_leverage = 1.0,
                                    target_long_exposure_perc = 0.50,
                                    target_short_exposure_perc = 0.50)


    # This variable put a percentage limit on the cash we can use for trading every day
    # so that something will be left available for the following days
    # as we expect to find events every day, we want to have some cash available for trading
    context.daily_cash_limit_perc  = 0.80

    #
    # Algo internal state
    #
    context.universe = []
    context.shorts =  pd.Series()
    context.longs  =  pd.Series()
    context.positions_to_clear = {}

    context.position_expire = {}

    #
    # Algo logic starts
    #
    attach_pipeline(make_pipeline(context), 'factors')

    #rebalance daily
    schedule_function(rebalance, date_rules.every_day(), time_rules.market_open())
    schedule_function(log_stats, date_rules.every_day(), time_rules.market_close())




# Compute final rank and assign long and short baskets.
def before_trading_start(context, data):
    results = pipeline_output('factors')
    results = results.replace([np.inf, -np.inf], np.nan)
    results = results.dropna()
    results = results.drop(context.dont_buys, axis=0, errors='ignore')

    print 'Basket of stocks %d / %d' % (len(results), len(pipeline_output('factors')))

    now = get_datetime()

    #
    # Fill context.positions_to_clear with positions that we need to exit
    # "rebalance" method will use that information to exit required positions
    #
    context.positions_to_clear = {}
    temporary_exclusions = []
    for sec, position in context.portfolio.positions.iteritems():
        temporary_exclusions.append(sec)
        if now >= context.position_expire.get(sec, now):
            context.positions_to_clear[sec] = position.amount

    # clear old entries
    for sec in context.position_expire.keys():
        if sec not in context.portfolio.positions:
            del context.position_expire[sec]

    # we don't want to enter positions that we already hold
    results = results.drop(temporary_exclusions, axis=0, errors='ignore')

    #
    # Now fill context.shorts and context.longs and "rebalance" method will use
    # that information to enter required positions
    #
    patterns = [ # name, code, number of days to hold the positions
           ('HS'  , -2, 1),
           ('IHS' ,  2, 1),
           ('BTOP', -1, 1),
           ('BBOT',  1, 1),
           ('TTOP', -4, 1),
           ('TBOT',  4, 1),
           ('RTOP', -3, 1),
           #('RBOT',  3, 4),
    ]

    context.shorts = pd.Series()
    context.longs  = pd.Series()
    for name, code, holding_days in patterns:
        positions = results[ results['pattern'] == code ]['pattern']
        if len(positions) <= 0:
            continue
        if code < 0:
            context.shorts = context.shorts.append( positions )
        elif code > 0:
            context.longs  = context.longs.append( positions )
        expire_date = now + datetime.timedelta(days=holding_days)
        for sec in positions.index:
            context.position_expire[sec] = expire_date

    print 'shorts (length %d):\n' % (len(context.shorts.index)), context.shorts
    print 'longs  (length %d):\n' % (len(context.longs.index)), context.longs

    context.universe = (context.longs.index | context.shorts.index)

def rebalance(context, data):

    #
    # calculate how much money we have for rebalancing today
    #
    context.exposure.update(context, data)

    available_cash = context.exposure.get_available_cash(context)

    log.debug( 'available_cash %f' % (available_cash) )

    #
    # as we expect to find events every day, we want to have some cash available for trading
    # we put a percentage limit on the cash we can use for trading every day
    # so that something will be left available for the following days
    #
    available_cash  *= context.daily_cash_limit_perc

    log.debug( 'We will use cash %f: long %d sec, short %d sec' % (available_cash, len(context.longs.index), len(context.shorts.index)) )

    #
    # Hre we decide how much cash we want to assing to each security
    #
    cash_per_sec = available_cash / (len(context.longs.index)+len(context.shorts.index))
    # no more than 2000 anyway
    cash_per_sec = min( cash_per_sec, 2000)

    #
    # Enter new positions
    #
    for sec in context.longs.index:
        if cash_per_sec > 0 and data.can_trade(sec):
            order_value(sec, cash_per_sec)
            log.debug( 'long order %s amount %f' % (str(sec), cash_per_sec) )

    for sec in context.shorts.index:
        if cash_per_sec > 0 and data.can_trade(sec):
            order_value(sec, -cash_per_sec)
            log.debug( 'short order %s amount %f' % (str(sec), cash_per_sec) )

    #
    # Clear positions for this day
    #
    for sec in context.positions_to_clear:
        if data.can_trade(sec):
            order_target(sec, 0)
            log.debug( 'clear positions for %s' % (str(sec)) )


def log_stats(context, data):
    context.exposure.update(context, data)
    long_exposure_pct, short_exposure_pct = context.exposure.get_long_short_exposure_pct(context)
    record(lever=context.account.leverage,
           exposure=context.account.net_leverage,
           num_pos=len(context.portfolio.positions),
           long_signals=len(context.longs.index),
           short_signals=len(context.shorts.index))
