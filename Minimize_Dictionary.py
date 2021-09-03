# 튜플로 이루어진 리스트 -> 딕셔너리

vals_list=[('pi',3.14), ('phi', 1.1618)]
my_dict = {i[0]:i[1] for i in vals_list}

print(my_dict)



# 두 리스트를 하나의 딕셔너리로 합치기

keys = ['Bob', 'Carol', 'Ted', 'Alice']
values = ['4.0', '4.0', '3.75', '3.9']
grade_dict = {keys[i]:values[i] for i in range(len(keys))}

print(grade_dict)



# 딕셔너리의 키-값을 서로 바꾸기

changed_dict = {v:k for k,v in grade_dict.items()}
# 위에서 value가 같으면 뒤바뀌었을때 키값이 같게 된다.
# 하나의 키에는 하나의 값만 들어가므로 바뀐 딕셔너리에 먼저 입력된 value값은 사라진다.
print(changed_dict)
# 'Bob'이 없어진 것을 볼 수 있다.