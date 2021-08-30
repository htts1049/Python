# 이름을 입력받아 입력받은 이름을 나열하는 함수

def main():
    my_list=[]
    while True:
        name = input('Enter next name : ')
        if len(name) == 0:
            break
        my_list.append(name)
    my_list.sort()
    print('Here is the sorted list : ')
    for a_word in my_list:
        print(a_word, end=' ')
        

main()