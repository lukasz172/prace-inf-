

class Postac:
    def __init__(self, imie, wiek, opis, historia):
        self.imie = imie
        self.wiek = wiek
        self.opis = opis
        self.historia = historia
        self.zadanie = zadanie
    def przedstaw_sie(self):
        print(f"Witaj graczu, jestem {self.imie}, mam {self.wiek} lat.")
        print(f"Wygląd: {self.opis}")

    def przedstaw_historie(self):
        print("Moja historia:")
        print(self.historia)
        print("Zadanie:")
        print(zadanie)



imie = "Bożydar Konstantynopolitańczykowianeczkowski"
wiek = 69
opis = "Mądry lecz z autyzmem mający 203 centymetry wzrostu mężczyzna o zielonych oczach nie mający włosów będący prawnikiem."
historia = "W krainie wielkich możliwości, w sercu nowoczesnego miasta, żył niezwykły człowiek o imieniu Bożydar. Miał 203 centymetry wzrostu, co sprawiało, że zawsze rzucał się w oczy w tłumie. Jego zielone oczy emanowały głębokim zrozumieniem świata, a ich intensywny kolor przyciągał uwagę każdego, kto spojrzał w ich stronę, lecz niestety jednego dnia na rozprawie sądowej oskarżony wkurzył go i uderzył oskarżonego tak mocno że wywaliła się cała ławka, za to został skazany na powieszenie."
zadanie = "Z powodu skazania Bożydara na powieszenie twoim zadaniem jest go ocalić zanim straci wszystkie kończyny które odetną mu jeżeli odpowiesz źle, chcąc cię zastraszyć już odcięli mu nogę lecz to cię nie powstrzyma, twoim zadaniem jest odgadnięcie o jakie słowo chodzi związane z daną kategorią którą możesz wybrać na początku gry, możesz popełnić tylko 6 błędów. Powodzenia!!!"
Bożydar_Konstantynopolitańczykowianeczkowski = Postac(imie, wiek, opis, historia)


    




