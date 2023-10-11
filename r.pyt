#  licznik 0
# licznik = 0

#  suma 0
# suma_parzystych = 0
# suma_nieparzystych = 0
# suma_podzielnych = 0

#  list
# lista = []

#  6 liczb
# for i in range(6):
#     liczba = float(input(f"Podaj liczbę {i+1}: "))
#     lista.append(liczba)
    
#     if liczba >= 0:
#         licznik += 1
    
#     if liczba % 2 == 0:
#         suma_parzystych += liczba
#     else:
#         suma_nieparzystych += liczba

#     if liczba % 35 == 0:
#         suma_podzielnych += liczba

#  najwieksza i najmniejsza
# indeks_max = [i for i, x in enumerate(lista) if x == max(lista)]
# indeks_min = [i for i, x in enumerate(lista) if x == min(lista)]

#  wyniki
# print("Liczba liczb większych lub równych 0: ", licznik)
# print("Suma wszystkich elementów parzystych: ", suma_parzystych)
# print("Suma wszystkich elementów nieparzystych: ", suma_nieparzystych)
# print("Suma wszystkich elementów podzielnych przez 5 i 7: ", suma_podzielnych)
# print("Indeksy największych wartości: ", indeks_max)
# print("Indeksy najmniejszych wartości: ", indeks_min)

#  ile razy w liscie
# liczba_uzytkownika = float(input("Podaj liczbę, aby sprawdzić ile razy występuje na liście: "))
# liczba_wystapien = lista.count(liczba_uzytkownika)
# print(f"Liczba {liczba_uzytkownika} występuje na liście {liczba_wystapien} razy.")