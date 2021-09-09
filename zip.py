# zip 함수
# 여러개의 순회가능한( iterable ) 객체를 받고, 각 객체가 담겨있는 원소를
# 튜플의 형태로 차례료 접근할 수 있는 반복자 ( iterator ) 반환

numbers = [1,2,3,4,5,6]
letters = ["A","B","C","D"]
name = ["Jack","Ahn","Sam"]

for pair in zip(numbers,letters):
    print(pair)

print(list(zip(numbers,letters,name)))

# 객체의 길이가 다르면 더 적은 것의 개수만큼 반환