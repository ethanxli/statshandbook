from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tempfile
import urllib

import numpy as np
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)
flags = tf.app.flags
FLAGS = flags.FLAGS

flags.DEFINE_string(
    "train_data",
    "",
    "Path to the training data.")
flags.DEFINE_string(
    "test_data",
    "",
    "Path to the test data.")
flags.DEFINE_string(
    "predict_data",
    "",
    "Path to the prediction data.")

tf.logging.set_verbosity(tf.logging.INFO)
# Learning rate for the model
LEARNING_RATE = 0.001

def maybe_download():
    """Maybe downloads training data and returns train and test file names."""
    train_file_name = test_file_name = predict_file_name = ''

    if FLAGS.train_data:
        train_file_name = FLAGS.train_data
    else:
        train_file = tempfile.NamedTemporaryFile(delete=False)
        urllib.urlretrieve("http://download.tensorflow.org/data/abalone_train.csv", train_file.name)
        train_file_name = train_file.name
        train_file.close()
        print("Training data is downloaded to %s" % train_file_name)

    if FLAGS.test_data:
        test_file = tempfile.NamedTemporaryFile(delete=False)
        urllib.urlretrieve("http://download.tensorflow.org/data/abalone_test.csv", test_file.name)
        test_file_name = test_file.name
        test_file.close()
        print("Test data is downloaded to %s" % test_file_name)

    if FLAGS.predict_data:
        predict_file_name = FLAGS.predict_data
    else:
        predict_file = tempfile.NamedTemporaryFile(delete=False)
        urllib.urlretrieve("http://download.tensorflow.org/data/abalone_predict.csv", predict_file.name)
        predict_file_name = predict_file.name
        predict_file.close()
        print("Prediction data is downloaded to %s" % predict_file_name)

    return train_file_name, test_file_name, predict_file_name


def model_fn(features, targets, mode, params):
    """Model function for Estimator."""

    # Connect the first hidden layer to input layer
    # (features) with relu activation
    first_hidden_layer = tf.contrib.layers.relu(features, 10)

    # Connect the second hidden layer to first hidden layer with relu
    second_hidden_layer = tf.contrib.layers.relu(first_hidden_layer, 10)

    # Connect the output layer to second hidden layer (no activation fn)
    output_layer = tf.contrib.layers.linear(second_hidden_layer, 1)

    # Reshape output layer to 1-dim Tensor to return predictions
    predictions = tf.reshape(output_layer, [-1])
    predictions_dict = {"ages": predictions}

    # Calculate loss using mean squared error
    loss = tf.contrib.losses.mean_squared_error(predictions, targets)

    train_op = tf.contrib.layers.optimize_loss(
      loss=loss,
      global_step=tf.contrib.framework.get_global_step(),
      learning_rate=params["learning_rate"],
      optimizer="Adam")

    return predictions_dict, loss, train_op




def input_fn(df):
  # Creates a dictionary mapping from each continuous feature column name (k) to
  # the values of that column stored in a constant Tensor.
  continuous_cols = {k: tf.constant(df[k].values) for k in CONTINUOUS_COLUMNS}

  # Creates a dictionary mapping from each categorical feature column name (k)
  # to the values of that column stored in a tf.SparseTensor.
  categorical_cols = {k: tf.SparseTensor(
      indices=[[i, 0] for i in range(df[k].size)],
      values=df[k].values,
      shape=[df[k].size, 1])
                      for k in CATEGORICAL_COLUMNS}
  # Merges the two dictionaries into one.
  feature_cols = dict(continuous_cols.items() + categorical_cols.items())
  # Converts the label column into a constant Tensor.
  label = tf.constant(df[LABEL_COLUMN].values)
  # Returns the feature columns and the label.
  return feature_cols, label


def eval_input_fn():
  return input_fn(df_test)

def main(unused_argv):
    # Load datasets
    abalone_train, abalone_test, abalone_predict = maybe_download()

    # Training examples
    training_set = tf.contrib.learn.datasets.base.load_csv_without_header(
      filename=abalone_train,
      target_dtype=np.int,
      features_dtype=np.float32)

    # Test examples
    test_set = tf.contrib.learn.datasets.base.load_csv_without_header(
      filename=abalone_test,
      target_dtype=np.int,
      features_dtype=np.float32)

    # Set of 7 examples for which to predict abalone ages
    prediction_set = tf.contrib.learn.datasets.base.load_csv_without_header(
      filename=abalone_predict,
      target_dtype=np.int,
      features_dtype=np.float32)

    # Set model params
    model_params = {"learning_rate": LEARNING_RATE}

    # Build 2 layer fully connected DNN with 10, 10 units respectively.
    nn = tf.contrib.learn.SKCompat(tf.contrib.learn.Estimator(model_fn=model_fn, params=model_params))

    # Fit
    nn.fit(x=training_set.data, y=training_set.target, steps=5000)

    # Score accuracy
    ev = nn.evaluate(x=test_set.data, y=test_set.target)
    print (ev)
    # loss_score = ev["loss"]
    # print("Loss: %s" % loss_score)

    # Print out predictions
    predictions = nn.predict(x=prediction_set.data)
    for i, p in enumerate(predictions):
        print(i,p)
        # print("Prediction %s: %s" % (i + 1, p["ages"]))


if __name__ == "__main__":
    tf.app.run()
