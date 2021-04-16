import tensorflow as tf

# 노드를 만들어 데이터를 삽입, 그 노드들을 연결하여서 그래프를 구성하는 것이 tensorflow의 기본
# node = tf.constant("Hello, Tensorflow!", tf.string)
# print(node.numpy())

# Tensorflow를 가지고 덧셈 수행

# 그래프를 build
# node1 = tf.constant(3.0,tf.float32)
# node2 = tf.constant(4.0,tf.float32)

# def forward():
#     return node1 + node2

# # update variables
# out_a = forward()
# print(out_a)


# 그래프를 동적으로 수행 -> node를 constant가 아닌 placeholder로 만들어 값을 넘겨줌
# 위 방법은 버전 1에서의 방법, 현재 버전 2에서는 placeholder가 사라짐
# placeholder 대신 @tf.function.annotation을 이용하여 함수를 정의, 값을 넘김
@tf.function # tf의 함수를 정의
def adder(a, b):
    return a + b

a = tf.constant(1)
b = tf.constant(2)
print(adder(a, b))

c = tf.constant(3)
d = tf.constant(4)
print(adder(c, d))