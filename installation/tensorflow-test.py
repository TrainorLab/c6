import tensorflow as tf

tf.config.list_physical_devices('GPU')

node1 = tf.constant(3.0)
node2 = tf.constant(4.0)
print(node1, node2)
print(node1 + node2)
