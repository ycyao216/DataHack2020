import tensorflow as tf

path = 'Embarcadero, San Francisco, CA->Fisherman\'s Wharf, San Francisco, CA'
save_directory = './models/'
name = input('Enter the suffix for the model, default none')
save_directory+=name

global_step = tf.Variable(0, name="step_count")
graph = Graph()
loader = data_loader('../data/barts_hotspots_sorted.csv',)
