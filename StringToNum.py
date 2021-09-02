# 프로그래머스 level 1. 숫자 문자열과 영단

def solution(s):
  
    s=s.replace('one','1')
    s=s.replace('two','2')
    s=s.replace('three','3')
    s=s.replace('four','4')
    s=s.replace('five','5')
    s=s.replace('six','6')
    s=s.replace('seven','7')
    s=s.replace('eight','8')
    s=s.replace('nine','9')
        
    answer=int(s)
    return answer

s=input("입력: ").lower()

while (len(s)<1) or (len(s)>50) or (s[0]=='0') or (s[0:4]=='zero'):
        s=input("다시 입력하세요: ")
        
if solution(s)>2000000000:
    print("다시 실행하세요.")
    exit()


print("변환된 값은 ",solution(s),'입니다.',sep='')
