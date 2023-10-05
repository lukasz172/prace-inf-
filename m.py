# 1: Utwórz pustą listę o nazwie "numbers"
numbers = []

# 2: Poproś użytkownika o podanie 5 liczb i dodaj je do listy
for i in range(5):
    number = float(input(f"Podaj liczbę {i+1}: "))
    numbers.append(number)

# 3: Oblicz sumę liczb znajdujących się w liście "numbers"
suma = sum(numbers)

# 4: Znajdź największą liczbę w "numbers"
max_number = max(numbers)

# 5: Znajdź najmniejszą liczbę w "numbers"
min_number = min(numbers)

# 6: Znajdź średnią arytmetyczną w "numbers"
average = suma / len(numbers)

# 7: Znajdź ilość liczb parzystych w "numbers"
even_count = sum(1 for num in numbers if num % 2 == 0)

# 8: Stwórz nową listę o nazwie "duplicates" zawierającą powtarzające się elementy z listy "numbers"
duplicates = [num for num in numbers if numbers.count(num) > 1]

# 9: Usuń wszystkie powtarzające się elementy z listy "numbers"
numbers = list(set(numbers))

# 10: Stwórz nową listę o nazwie "squares" zawierającą kwadraty liczb z listy "numbers"
squares = [num**2 for num in numbers]

# Wyświetl wyniki
print(f"Suma liczb: {suma}")
print(f"Największa liczba: {max_number}")
print(f"Najmniejsza liczba: {min_number}")
print(f"Średnia arytmetyczna: {average}")
print(f"Ilość liczb parzystych: {even_count}")
print(f"Powtarzające się elementy: {duplicates}")
print(f"Liczby bez powtórzeń: {numbers}")
print(f"Kwadraty liczb: {squares}")