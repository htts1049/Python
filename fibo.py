# 튜플로 피보나치수열 함수 생성

def fibo(n):
    a, b = 1,0
    i = 1
    while i<=n:
        print(i,'번째 피보나치 수열 : ',a)
        a,b = a+b, a
        i+=1
        

n = int(input('정수를 입력하시오 : '))

print(fibo(n))