import tensorflow as tf
from graph import *
from data_loader import *

path = 'Embarcadero, San Francisco, CA->Fisherman\'s Wharf, San Francisco, CA'
save_directory = './models/'
steps = 1000
save_interval = 50

global_step = tf.Variable(0, name="step_count")
graph = Graph()
loader = data_loader('../data/barts_hotspots_sorted.csv', path)

optimizer = tf.train.AdamOptimizer().minimize(graph.mse_loss, global_step=global_step)
saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    x_0, y_0 = loader.next_batch()
    for i in range(steps):
        x_input, y_input = loader.next_batch()
        sess.run(optimizer, feed_dict={graph.x_input:x_input,
            graph.y_gt:y_input})
        if(i%save_interval==0):
            saver.save(sess, save_directory,
                    global_step=global_step)
            gradients = tf.gradients(graph.mse_loss, graph.W1)
            gradients = sess.run(gradients, feed_dict={graph.x_input:x_input,
                graph.y_gt:y_input})
            print(gradients)
            loss = sess.run(graph.mse_loss, feed_dict={graph.x_input:x_input,
                graph.y_gt:y_input})
            print(loss)
            loss = sess.run(graph.pre_fc, feed_dict={graph.x_input:x_input,
                graph.y_gt:y_input})
            print(loss)
