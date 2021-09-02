# reduce 함수

import functools

def add_func(a, b):
    return a+b

def mul_func(a, b):
    return a * b

n = 5
a_list = list(range(1, n+1))

triangle_num = functools.reduce(add_func, a_list)
fact_num = functools.reduce(mul_func, a_list)

print(f'triangle_num is {triangle_num}\nfact_num is {fact_num}')


# lambda 함수 (reduce 함수와 함께 쓰면 좋다.)

my_f = lambda x, y: x+y

sum1 = my_f(3,7)
print('\n3+7=',sum1)
sum2 = my_f(10,15)
print('10+15=',sum2)


# 위처럼 덧셈, 곱셈 함수를 직접 정의하는 대신 lambda 함수를 통해 더 간단하게 작성
triangle_num = functools.reduce(lambda x, y: x+y, [1,2,3,4,5])
fact_num = functools.reduce(lambda x, y: x*y, [1,2,3,4,5])

print(f'\ntriangle_num is {triangle_num}\nfact_num is {fact_num}')
