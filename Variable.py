import tensorflow as tf

state = tf.Variable(0,name='counter')

print(state.name)

# 将 State 更新成 new_value
update = tf.assign(state, new_value)
one= tf.constant(1)
new_value =tf.add(state ,one)
# 如果定义 Variable, 就一定要 initialize
# init = tf.initialize_all_variables() # tf 马上就要废弃这种写法
init = tf.global_variables_initializer()  # 替换成这样就好
 
# 使用 Session
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))