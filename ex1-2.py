import math

Radius = float(input("구의 반지름을 입력하시오 :"))
pi = math.pi

Area = 4* (Radius**2) * pi

print(f'해당 구의 넓이는{Area: 0.2f}입니다.')
