import random

from postac import Bożydar_Konstantynopolitańczykowianeczkowski

Bożydar_Konstantynopolitańczykowianeczkowski.przedstaw_sie()

Bożydar_Konstantynopolitańczykowianeczkowski.przedstaw_historie()

def wybierz_slowo(kategoria="przedmioty"):
    kategorie_słów_do_wybrania = {
        "komputerowe": [
                "python",
                "programowanie",
                "gra",
                "komputer",
                "informatyka",
                "nauka", 
                "monitor",
                "system",
                "wirus",
                "laptop", 
                "ekran",
                "dysk",
                "nauczyciel",
                "lekcje",
                "kosz",
                "aplikacja",
                "klawisze",
                "algorytm",
                "bajt",
                "bit",
                "dvd",
                "folder",
                "ikona",
                "internet",
                "kursor",
                "modem"
        ],
        "owoce": [
                "jabłko",
                "banan",
                "ananas",
                "arbuz",
                "pomarańcza",
                "kiwi",
                "truskawka",
                "porzeczka",
                "malina",
                "gruszka",
                "śliwka",
                "borówka",
                "limonka",
                "mandarynka",
                "wiśnia",
                "brzoskwinia",
                "mango",
                "jeżyna",
                "grejpfrut",
        ],
        "przedmioty": [
                "ołówek",
                "długopis",
                "gumka",
                "temperówka",
                "pióro",
                "wkład",
                "korektor",
                "zeszyt",
                "podręcznik",
                "zakreślacz",
                "linijka",
                "kątomierz",
                "nożyczki",
                "kredka",
                "mazak",
                "plecak",
                "cyrkiel",
                "kalkulator",
        ],
        "instrumenty": [
                "gitara",
                "pianino",
                "ukulele",
                "dzwonki",
                "skrzypce",
                "perkusja",
                "harfa",
                "wiolonczela",
                "saksofon",
                "trąbka",
                "tuba",
                "tamburyn",
                "marakasy",
                "flet",
                "akordeon",
                "bębny",
        ],
        "marki_samochodow": [
                "ferrari",
                "lamborghini",
                "mclaren",
                "audi",
                "bmw",
                "fiat",
                "mercedes",
                "kia",
                "dodge",
                "chevrolet",
                "bentley",
                "ford",
                "jeep",
                "honda",
                "mazda",
                "porsche",
                "toyota",
                "volskwagen",
                "volvo",
                "nissan",
        ],
        "kraje" :[
                "polska",
                "niemcy",
                "rosja",
                "anglia",
                "ukraina",
                "hiszpania",
                "portugalia",
                "brazylia",
                "argentyna",
                "belgia",
                "francja",
                "dania",
                "chiny",
                "japonia",
                "albania",
                "meksyk",
                "usa",
                "rumunia",
                "szwecja",
                "szwajcaria",

        ]
        

    }


    if kategoria in kategorie_słów_do_wybrania:
        return random.choice(kategorie_słów_do_wybrania[kategoria])
    else:
        return "nie ma takiej kategori"


def włącz_gre():
    słowo = wybierz_slowo()
    ukryte_słowo = ["_"] * len(słowo)
    return słowo, ukryte_słowo, []


def wisielec(błędy):
    jakie_są_rysunki = [
        """
           --------
           |      |  
           |      |
           |      O
           |     \|/
           |      |
           |     / \
           |
           |
           _
        """,
        """
           --------
           |      |  
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           |
           |
           _
        """,
        """
           --------
           |      |  
           |      |
           |      O
           |     \|/
           |      |
           |      
           |
           |
           _
        """,
        """
           --------
           |      |
           |      |
           |      O
           |     \|
           |      |
           |     
           |
           |
           _
        """,
        """
           --------
           |      |  
           |      |
           |      O
           |      |
           |      |
           |     
           |
           |
           _
        """,
        """
           --------
           |      |  
           |      |
           |      O
           |     
           |     
           |     
           |
           |
           _
        """,
        """
           --------
           |      |
           |      |  
           |      
           |     
           |     
           |     
           |
           |
           _
        """
    ]
    return jakie_są_rysunki[len(błędy)]

def rysuj_wisielca(ukryte_słowo, błędy):
    print(wisielec(błędy))
    print(" ".join(ukryte_słowo))

def wpisz():
    return input("Podaj literę: ")


def czy_chcesz_zagrac_ponownie():
    odpowiedz = input("Chcesz spróbować ocalić Bożydara jeszcze raz? (tak/nie): ").lower()
    return odpowiedz == "tak"


def restartuj_gre():
    return włącz_gre()

MAX_BLEDY = 6

def gra():
    while True:
        słowo, ukryte_słowo, błędy = włącz_gre()
        koniec_gry = False

        while not koniec_gry:
            rysuj_wisielca(ukryte_słowo, błędy)
            ruch = wpisz()

            if ruch in słowo:
                for i in range(len(słowo)):
                    if słowo[i] == ruch:
                        ukryte_słowo[i] = ruch
            else:
                błędy.append(ruch)

            koniec_gry = all(litera != "_" for litera in ukryte_słowo) or len(błędy) == MAX_BLEDY

            if len(błędy) == MAX_BLEDY:
                print("Przegrałeś, Bożydar umarł i nikt cię nie lubi Dobra odpowiedź to", słowo)
                break

        rysuj_wisielca(ukryte_słowo, błędy)
        if all(litera != "_" for litera in ukryte_słowo):
            print("Dobra robota, ocaliłeś Bożydara!")
        else:
            print(f"Przegrałeś, Bożydar umarł i nikt cię nie lubi, Dobra odpowiedź to: {słowo}")

        if not czy_chcesz_zagrac_ponownie():
            print("Bożydar życzy miłego dnia")
            break  


if __name__ == "__main__":
    gra()  