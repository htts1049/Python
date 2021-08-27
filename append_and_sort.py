# 빈 리스트에 입력을 받아 출력

a_list=[]

while True:
    name = input('이름을 입력하시오.: ')
    if not name:
        break
    a_list.append(name)     # "변수를 넣을 데이터의 이름".append("넣고자 하는 변수의 이름")
    

a_list.sort(reverse=True)               # a_list 리스트를 정렬, reverse=True(또는 1) 대입시 거꾸로 정렬

print("\n입력한 이름은 다음과 같다",'\n', a_list)