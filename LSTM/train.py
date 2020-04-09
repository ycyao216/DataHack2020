import tensorflow as tf
from graph import *
from data_loader import *

path = 'Embarcadero, San Francisco, CA->Fisherman\'s Wharf, San Francisco, CA'
save_directory = './models/'
steps = 2000
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
            print('Gradients on MSE loss')
            print(gradients)

            flat_x = sess.run(graph.pre_middle, feed_dict={graph.x_input:x_input,
                                                       graph.y_gt:y_input})
            print('pre_middle')
            print(flat_x)

            flat_x = sess.run(graph.middle, feed_dict={graph.x_input:x_input,
                graph.y_gt:y_input})
            print('middle')
            print(flat_x)

            print('y input')
            print(y_input)

            loss = sess.run(graph.mse_loss, feed_dict={graph.x_input:x_input,
                graph.y_gt:y_input})
            print('MSE loss')
            print(loss)

            loss = sess.run(graph.y_pred, feed_dict={graph.x_input:x_input,
                graph.y_gt:y_input})
            print('Prediction y')
            print(loss)
            loss = sess.run(graph.W1, feed_dict={graph.x_input:x_input,
                graph.y_gt:y_input})
            print('W1 weights')
            print(loss)
