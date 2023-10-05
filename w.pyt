import math


a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    print("to tr")
    p = 1/2*(a+b+c)
    p = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"Polep tr: {p}")
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("to jest tr prost")
    else:
        print("to nie jest tr prost")
else:
    print("to nie jest tr")