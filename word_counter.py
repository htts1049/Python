# 문자열을 입력으로 받아 쪼개어 단어의 빈도수를 출력하는 함수

s = input(('문자열을 입력하라 : ')).split()

wrd_counter = {}
for wrd in s:
    
    wrd_counter[wrd] = wrd_counter.get(wrd, 0)+1


print(wrd_counter)