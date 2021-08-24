str = input("문자를 입력하시오: ").lower()
col = 'aeiou'
count = 0
for i in range(len(str)):
    if str[i] in col:
        count += 1
        
print("모음은 총",count, "개 입니다.")