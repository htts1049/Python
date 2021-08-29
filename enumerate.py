# enumerate 함수로 인덱싱
# enumerate(이터러블, 시작=n) -> (n,이터러블[0]), ...

a_list = ['Tom', 'Dick', 'Jane']

print(list(enumerate(a_list, 1)))




# for 루프와 함께 사용하여 원하는 결과 생성

print('\n')
for item_num, name_str in enumerate(a_list,1):
    print(item_num, '. ', name_str, sep='')