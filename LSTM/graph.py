import tensorflow as tf
class Graph():
    def __init__():
        x_input = tf.placeholder("float", [None, 10, 3])
        y_gt = tf.placeholder("float", [1])
        LSTM_layer = tf.keras.layers.CuDNNLSTM(3)
        pre_fc = LSTM_layer.call(x_input)
        W = tf.get_variable("FC_weights", shape=[3,1], dtype=tf.dtypes.float16, trainable=True)
        y_pred = tf.matmul(pre_fc, W)
        mse_loss = tf.keras.losses.MSE(y_gt, y_pred)
