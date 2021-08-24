def remove_front_end(str):
    sen = str.replace(str[0],'')
    sen = sen.replace(str[len(sen)],'')
    return sen

n = input("문자열 입력: ")

print(remove_front_end(n))
