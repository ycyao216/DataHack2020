import tensorflow as tf
class Graph():
    def __init__(self):
        self.x_input = tf.placeholder("float", [None, 10, 3])
        self.y_gt = tf.placeholder("float", [None])
        #LSTM_layer = tf.keras.layers.CuDNNLSTM(3)
        LSTM_layer = tf.keras.layers.LSTM(3)
        pre_fc = LSTM_layer(self.x_input)
        W = tf.get_variable("FC_weights", shape=[3,1], dtype=tf.dtypes.float32, trainable=True)
        self.y_pred = tf.matmul(pre_fc, W)
        self.mse_loss = tf.keras.losses.MSE(self.y_gt, self.y_pred)
