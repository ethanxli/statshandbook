#tensorflow RNN for predicting electricity prices


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from tensorflow.contrib import learn
from sklearn.metrics import mean_squared_error, mean_absolute_error
from LSTM_Predictor import generate_data, load_csvdata, lstm_model

from tensorflow.contrib.learn.python import SKCompat #

TIMESTEPS = 10
RNN_LAYERS = [{'num_units' : 5}]
DENSE_LAYERS = [10,10]
BATCH_SIZE = 100
DENSE_LAYERS = None
TRAINING_STEPS = 100
PRINT_STEPS = TRAINING_STEPS / 10

dateparse = lambda dates: pd.datetime.strptime(dates, '%d/%m/%Y %H:%M')
rawdata = pd.read_csv("./data/RealMarketPriceDataPT.csv",
                   parse_dates={'timeline': ['date', '(UTC)']},
                   index_col='timeline', date_parser=dateparse)

X, y = load_csvdata(rawdata, TIMESTEPS)


params = [TIMESTEPS,RNN_LAYERS,DENSE_LAYERS]

regressor = SKCompat(learn.Estimator(model_fn=lstm_model(TIMESTEPS, RNN_LAYERS, DENSE_LAYERS))) # new


validationMonitor = learn.monitors.ValidationMonitor(X['val'], y['val'],
                                                    every_n_steps=PRINT_STEPS,
                                                    early_stopping_rounds=1000)


regressor.fit(X['train'], y['train'], monitors = [validationMonitor])

print(X['test'].shape)
print(y['test'].shape)
predicted = regressor.predict(X['test']) # ,as_iterable=False)
#rmse = np.sqrt(((predicted - y['test']) ** 2).mean(axis=0))
score = mean_squared_error(predicted, y['test'])
print ("MSE: %f" % score)

plot_predicted, = plt.plot(predicted, label='predicted')
plot_test, = plt.plot(y['test'], label='test')
plt.legend(handles=[plot_predicted, plot_test])
plt.show()
