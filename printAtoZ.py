# append 함수와 join 메서드를 이용해 알파벳 A에서 Z까지 출력하는 함수

A = ord('A')

a_lst=[]

for i in range(A, A+26):
    a_lst.append(chr(i))            # i의 주소값을 a_lst 리스트에 추가
    i += 1


print(''.join(a_lst))               # join 함수를 이용해 리스트를 문자열로 변환