import tensorflow as tf

x = tf.constant(3)
y = tf.constant(4)

result = tf.multiply(x,y)
print(tf.__version__)
#print(output)

with tf.Session() as sess:
    output = sess.run(result)
    print(output)

