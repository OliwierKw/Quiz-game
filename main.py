print("Witamy w moim quzie!")
print("Tematyka jest z histori Polski :)")

gra = input("Czy chcesz zagrać?")
if gra.lower() != "tak":
    quit()

wynik = 0

pytanie = input("Kiedy odbył się chrzest Polski?")
if pytanie == "966":
    print("Prawda!")
    wynik += 1
else:
    print("Błąd!")

pytanie = input("Kto zastał Polskę drewnianą a zostawił murowaną? (Imie i przydomek)")
if pytanie.lower() == "kazimierz wielki":
    print("Prawda!")
    wynik += 1
else:
    print("Błąd!")

pytanie = input("Jaka była pierwsza stolica Polski? (nazwa)")
if pytanie.lower() == "gniezno":
    print("Prawda!")
    wynik += 1
else:
    print("Błąd!")

pytanie = input("Kiedy w Polsce rozpoczął się stan wojenny? (rok)")
if pytanie == "1981":
    print("Prawda!")
    wynik += 1
else:
    print("Błąd!")

print("Koniec quizu! Udało ci się odpowiedzieć dobrze na " + str(wynik) + " pytania!")
print("Rozwiązałeś quiz poprawnie w " + str((wynik / 4) * 100) + "%.")