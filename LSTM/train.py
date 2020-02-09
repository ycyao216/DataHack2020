import tensorflow as tf
from graph import *
from data_loader import *

path = 'Embarcadero, San Francisco, CA->Fisherman\'s Wharf, San Francisco, CA'
save_directory = './models/'
steps = 10
save_interval = 5

global_step = tf.Variable(0, name="step_count")
graph = Graph()
loader = data_loader('../data/barts_hotspots_sorted.csv', path)

optimizer = tf.train.AdamOptimizer().minimize(graph.mse_loss, global_step=global_step)
saver = tf.train.Saver()
with tf.Session() as sess:
    for i in range(steps):
        x_input, y_input = loader.next_batch()
        sess.run(optimizer, feed_dict={graph.x_input:x_input,
            graph.y_gt:y_input})
        if(i%save_interval):
            saver.save(sess, save_directory,
                    global_step=global_step)
