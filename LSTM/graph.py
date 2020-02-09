import tensorflow as tf
class Graph():
    def __init__(self):
        self.x_input = tf.placeholder("float", [None, 10, 3])
        self.y_gt = tf.placeholder("float", [None])
        initializer1 = tf.initializers.truncated_normal(mean=10.0)
        initializer2 = tf.initializers.truncated_normal()
        #LSTM_layer = tf.keras.layers.CuDNNLSTM(3)
        LSTM_layer = tf.keras.layers.LSTM(3, kernel_initializer=initializer2,
                recurrent_initializer=initializer2)
        self.pre_fc = LSTM_layer(self.x_input)
        self.W1 = tf.get_variable("FC_weights1", shape=[3,3], dtype=tf.dtypes.float32,
                trainable=True, initializer=initializer1)
        middle = tf.nn.relu(tf.matmul(self.pre_fc, self.W1))
        self.W2 = tf.get_variable("FC_weights2", shape=[3,1], dtype=tf.dtypes.float32,
                trainable=True, initializer=initializer1)
        self.y_pred = tf.matmul(middle, self.W2)
        self.mse_loss = tf.keras.losses.MSE(self.y_gt, self.y_pred)
