import time
import random

from swiat import swiat_gry


print(f"Witaj w {swiat_gry['nazwa']}!")
print(swiat_gry['opis'])

print("Dostępne lokacje:")

for nazwa_lokacji, dane_lokacji in swiat_gry['lokacje'].items():

    print(f"{nazwa_lokacji}: {dane_lokacji['opis']}")

    if 'mieszkancy' in dane_lokacji:

        print(f"Mieszkańcy: {', '.join(dane_lokacji['mieszkancy'])}")

    if 'sklepy' in dane_lokacji:

        print(f"Sklepy: {', '.join(dane_lokacji['sklepy'])}")

    if 'potwory' in dane_lokacji:

        print(f"Potwory: {', '.join(dane_lokacji['potwory'])}")

    if 'znaleziska' in dane_lokacji:

        print(f"Znaleziska: {', '.join(dane_lokacji['znaleziska'])}")



def print_stats(character):

    print(f"{character['name']} - Rola: {character['role']}, Zdrowie: {character['health']}")

def przedstawienie():
    print("Witaj w Krainie Przygód!")
    time.sleep(1)
    print("Jesteś bohaterem, który wyrusza w nieznane.")
    time.sleep(1)
    print("Twoim celem jest pokonanie złego smoka, który terroryzuje królestwo.")
    time.sleep(1)

opisy_postaci = {

    "wojownik": ["przystojny", "jasno włosy mężczyzna"],

    "wielkolud": ["duży", "jedno oki stwór"],

    "Goblin": ["zielony","niskiego wzrostu rozbujnik"],

    "Mieszkaniec": ["lokalny kupiec i sprzedawca towarów"],

    "Wampir": ["mieszkający w zamku","krwio pijca o jasnej karnacji"],

    "Łucznik": ["świetnie strzelający i grający na harmonii elf"],

    "Magik": ["znający dobrze magię człowiek"],

    "Krasnoludek": ["małe ale szybkie stworzenie mieszkające w lesie"],

    "Łowca": ["za pieniądze poluje na magiczne stworzenia"],

    "Czarnoksiężnik": ["posiada starożytną księge z najgorszymi zaklęciami"]

}

def wybierz_postac():
    postacie = [

        {"name": 
         
        "Wojownik",

        "role":

        "Miecz",

        "health":

        100},


        {"name":
         
        "Wielkolud",

        "role":

        "Pięści",

        "health":

        200},


        {"name":
         
        "Goblin",

        "role":

        "Nożyk",

        "health":

        110},


        {"name":
         
        "Mieszkaniec",

        "role":

        "pałka",

        "health":

        20},


        {"name":
         
        "Wampir",

        "role":

        "moce",

        "health":

        400},


        {"name":
         
        "Łucznik",

        "role":

        "Łuk",

        "health":

        80},


        {"name":
         
        "Magik",

        "role":

        "Czary",

        "health":

        70},


        {"name":
         
        "Krasnoludek",

        "role":

        "maczuga",

        "health":

        90},

        {"name":
         
        "Łowca",

        "role":

        "Pułapki",

        "health":
        
        120},


        {"name":
         
        "Czarnoksiężnik",

        "role":

        "Czarna magia",

        "health":

        80}
    
    
    ]


    print("Wybierz swoją postać:")
    for i, character in enumerate(postacie, 1):
        print(f"{i}. {character['name']}")

    choice = input("Twój wybór (1-10): ")
    while not choice.isdigit() or not (1 <= int(choice) <= 10):
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        choice = input("Twój wybór: ")

    print("Wybierz swoją postać:")
    for i, character in enumerate(postacie, 1):
        print(f"{i}. {character['name']}")


    chosen_character = postacie[int(choice) - 1]

    
    opis = opisy_postaci.get(chosen_character['name'], "Brak opisu dla tej postaci.")
    print(f"Opis postaci {chosen_character['name']}: {opis}")
    return postacie[int(choice) - 1]

def chapter_one(hero):
    print(f"Witaj, {hero['name']}!")
    time.sleep(1)
    print("Rozpoczynasz swoją podróż w małej wiosce na obrzeżach królestwa.")
    time.sleep(1)
    print("Nagle z daleka słyszysz krzyki mieszkańców.")
    time.sleep(1)
    print("Okazuje się, że wioskę zaatakowały orki!")
    time.sleep(1)

    choice = input("Czy chcesz stanąć do walki z orkami? (n): ")
    
    if choice.upper() == 'n':
        print("Wioska została zniszczona")
    else:
        print("Decydujesz się uniknąć walki, ponieważ mieszkańcy wyrzucili cię z swojego miasta. Orki zniszczyły wioskę.")


def chapter_two(hero):
    print(f"Po przygodzie z orkami, wyruszasz w dalszą podróż, {hero['name']}.")
    time.sleep(1)
    print("Docierasz do magicznego lasu, gdzie spotykasz tajemniczego czarodzieja.")
    time.sleep(1)
    print("Czarodziej oferuje ci magiczną amuletę, która ma zwiększyć twoje moce.")
    time.sleep(1)
    

def final_chapter(hero):
    print(f"Przed końcem jeszcze jedna walka, {hero['name']}.")
    time.sleep(1)
    print("Docierasz do wulkanicznej jaskini, gdzie według legendy mieszka złowrogi smok.")
    time.sleep(1)
    print("Walka zaczyna się...")
    time.sleep(1)

    
    dragon = {"name": "Smok", "role": "Ogień", "health": 100}

    while hero['health'] > 0 and dragon['health'] > 0:
        fight(hero, dragon)
        if dragon['health'] > 0:
            fight(dragon, hero)
            print(f"{hero['name']} pozostaje z {hero['health']} punktami zdrowia.")

    if hero['health'] <= 0:
        print(f"{hero['name']} nie przetrwał potyczki ze smokiem. Koniec przygody.")
    else:
        print(f"{hero['name']} pokonuje smoka i ratuje królestwo! Gratulacje!")

def fight(attacker, target):
    damage = random.randint(10, 30)
    print(f"{attacker['name']} atakuje {target['name']} i zadaje {damage} punktów obrażeń.")
    target['health'] -= damage

def main():
    przedstawienie()
    hero = wybierz_postac()
    chapter_one(hero)
    chapter_two(hero)
    final_chapter(hero)

if __name__ == "__main__":
    main()