# 얕은복사, 깊은복사의 이해

a_list = [1,2, [5,10]]
b_list = a_list[:]

b_list[0] = 0
b_list[1] = 0
b_list[2][0] = 0
b_list[2][1] = 0

# b_list값의 변경이 a_list값에 영향을 미칠까?

print("얕은복사 : ", a_list)

# 리스트 내의 리스트는 참조였기 때문에 a_lsit의 내부리스트도 변경된다!
# 이러한 문제는 copy 패키지안에 있는 deepcopy 함수를 통해 해결한다.

import copy

a_list = [1,2, [5,10]]
b_list = copy.deepcopy(a_list)

print("깊은복사 : ", a_list)