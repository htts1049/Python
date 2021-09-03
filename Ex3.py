# Ex 3-1
# 임의로 선택된 숫자로 이루어진 리스트의 평균값을 reduce 함수를 이용하여 작성

import functools
a_list = [10, 7, 5, 12, 19]
average=functools.reduce(lambda a,b : (a+b) ,a_list)/len(a_list)
print(average)

# 각 항목과 평균값의 차이를 계산하여 각 값의 제곱수를 구하기 (편차 제곱)

b_list=[round((i-average)**2,2) for i in a_list]
print(b_list)




# Ex 3-2
# 사용자가 원하는 만큼 숫자를 입력한 후 그 숫자들로 구성된 리스트를 만드는 프로그램 작성
# 평균값이 아닌 중앙값을 찾기, 항목이 짝수개라면 중간에 있는 2개의 평균값을 중앙값으로 지정

num_list=[]
num= input('원하는 만큼 숫자를 입력하세요 :')
num_list.append(num)
while num !='':
    num= input('원하는 만큼 숫자를 입력하세요 :')
    num_list.append(num)
    if num =='' :
        num_list.pop()
        break
    
mean = float(num_list[int((len(num_list))/2)])
if len(num_list)%2 ==0 :
    mean = (mean+float(num_list[int(len(num_list)/2)-1]))/2
        
print(mean)