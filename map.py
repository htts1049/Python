# map( function, iterable ) 이터러블에 함수 실행

my_list = [1, 2, 3, 4, 5]

# for 반복문 이용
result1 = []
for val in my_list:
    result1.append(val+1)
    
print(f'for 반복문 이용 : {result1}')



# map 함수 이용
result2 = list(map( lambda x: x+1 , my_list) )

print(f'map 함수 이용 : {result2}')