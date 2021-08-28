# 두 리스트가 같은 값을 공유하는 것을 확인

a_list = [2, 5, 10]
b_list = a_list

b_list.append(100)
a_list.append(200)
b_list.append(1)

print(a_list)