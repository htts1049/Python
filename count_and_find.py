# count 와 find 함수의 차이 비교

str = "doo be doo be doo..."

n_count = str.count('doo')
n_count_1to10= str.count('doo',1,10)

print("해당문자열 : ", str, '\n')

print("문자열 'doo'의 개수는 : ", n_count)
print("2번째 문자에서 10번째 문자까지 문자열 'doo'의 개수는 : ", n_count_1to10,'\n')


n_find = str.find('doo')
n_notfind = str.find('Doo')

print("'doo'문자열은 있다 : ", n_find)
print("'Doo'문자열은 없다 : ", n_notfind)


n=-1
print("문자열 'doo'가 나타나는 위치 : ", end='')
while True :
    n = str.find('doo', n+1)            # n=-1 이므로 첫번째 인덱스부터 'doo'가 있는지 확인
    if n==-1:                           # 첫번째 인덱스부터 'doo'가 있으므로 n=0
        break                           # n=0 이므로 두번째 인덱스부터 'doo'가 있는지 확인
    print(n, end=', ')                  # 여덟번째 인덱스부터 'doo'가 있으므로 n=7
                                        # n=7이므로 str[8]부터 'doo'가 있는지 확인
                                        # 15번째 인덱스부터 'doo'가 있으므로 n=14                                                        
                                        
                                        # 그 뒤로는 없으므로 n=-1, 루프에서 나옴
