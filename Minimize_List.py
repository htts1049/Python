# 리스트 함축

a_list = [1, 3, 5]
b_list = []


# for문과 append사용
for i in a_list:
    b_list.append(i)
print("for 문과 append 사용: ",b_list)


# 보다 간결하게 1개의 line으로 작성
b_list = [i for i in a_list]
print("하나의 line만으로 작성 : ",b_list)

# 생성될 값을 조절하여 아래와도 같이 가능
b_list = [i*i for i in a_list]
print("값을 제곱한 리스트 : ", b_list)

# for중첩문도 가능
mult_list = [i*j for i in range(3) for j in range(3)]

print(mult_list)
        
# if문도 추가할 수 있다.
my_list = [10, -10, -1, 12, -500, 13, 15 ,-3]
new_list = [i for i in my_list if i>0]
print(new_list)