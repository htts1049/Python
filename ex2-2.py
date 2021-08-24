def remove_front_end(str):
    sen = str.replace(str[0],'')
    sen = sen.replace(str[len(sen)],'')
    return sen

n = input("문자열을 입력하시오. : ")

print("처음과 마지막 문자를 제거했습니다. : ", remove_front_end(n))
