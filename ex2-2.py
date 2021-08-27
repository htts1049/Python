def remove_front_end(str):
    new_str = str.strip(str[0])
    new_str = new_str.strip(str[-1])
    
    return new_str

n = input("문자열을 입력하시오. : ")

print("처음과 마지막 문자를 제거했습니다. : ", remove_front_end(n))
