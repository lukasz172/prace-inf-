import math

print("Kalkulator pól i obwodów figur")
print("a - Kwadrat")
print("b - Prostokąt")
print("c - Trójkąt")
print("d - Trapez")
print("e - Równoległobok")
print("f - Romb")

wyb = input("Wybierz literę figury: ")

if wyb == 'a':
    bk_k = float(input("Bok kwadratu: "))
    pl_k = bk_k * bk_k
    obw_k = 4 * bk_k
    print("Pole kwadratu:", pl_k)
    print("Obwód kwadratu:", obw_k)
elif wyb == 'b':
    a_p = float(input("Pierwszy bok prostokąta: "))
    b_p = float(input("Drugi bok prostokąta: "))
    pl_p = a_p * b_p
    obw_p = 2 * (a_p + b_p)
    print("Pole prostokąta:", pl_p)
    print("Obwód prostokąta:", obw_p)
elif wyb == 'c':
    a_t = float(input("Podstawa trójkąta: "))
    h_t = float(input("Wysokość trójkąta: "))
    pl_t = 0.5 * a_t * h_t
    print("Pole trójkąta:", pl_t)
elif wyb == 'd':
    a_t = float(input("Pierwsza podstawa trapezu: "))
    b_t = float(input("Druga podstawa trapezu: "))
    h_t = float(input("Wysokość trapezu: "))
    pl_t = 0.5 * (a_t + b_t) * h_t
    print("Pole trapezu:", pl_t)
elif wyb == 'e':
    a_r = float(input("Jeden bok równoległoboku: "))
    h_r = float(input("Wysokość równoległoboku: "))
    pl_r = a_r * h_r
    obw_r = 2 * (a_r + h_r)
    print("Pole równoległoboku:", pl_r)
    print("Obwód równoległoboku:", obw_r)
elif wyb == 'f':
    d1_ro = float(input("Pierwsza przekątna rombu: "))
    d2_ro= float(input("Druga przekątna rombu: "))
    pl_ro= 0.5 * d1_ro * d2_ro
    print("Pole rombu:", pl_ro)

else:
    print("Wybrano złą literę figury.")
