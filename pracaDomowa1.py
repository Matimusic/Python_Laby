##############  Zadania do wykonania
## 1. Sprawdź wynik działań
# 0 > 1
# 0 <= 1
# 0 >= 1
# 1 == 0
# 1 == 1
# 1 != 0
# 1 != 1
print ("1 zadanie")
print(0 > 1)
print(0 <= 1)
print(0 >= 1)
print(1 == 0)
print(1 == 1)
print(1 != 0)
print(1 != 1)
## 2. Oblicz wyrażenie 2x+5y   gdzie: x,y to dowolne dwie liczby które podaje użytkownik (w konsoli)

x = float(input("Podaj x: "))
y = float(input("Podaj y: "))

wynik = 2*x + 5*y

print("Wynik:", wynik)

## 3. Wyświetl zdanie "Jestem a b mam c lat studiuję d",
##  gdzie : a-imie, a-nazwisko, c-liczba, d-kierunek studiów są dowolne zmienne które podaje użytkownik (wczytywane z klawiatury)

imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")
wiek = input("Podaj wiek: ")
studia = input("Podaj studia: ")

print("Jestem {} {} mam {} lat i studiuje {}.".format(imie, nazwisko, wiek, studia))

## 4. Sprawdź/porównaj czy 1+2+10+20000001+4+347586970885 jest równa 321784560456434534646

wynik1 = 1+2+10+20000001+4+347586970885
wynik2 = 321784560456434534646

print("Czy oba wyniki sa sobie rowne? ", wynik1, "Porownujemy do", wynik2, wynik1 == wynik2)

## 5. Sprawdź czy suma dowolnych dwóch liczb podanych przez użytkownika jest liczbą parzystą czy nieparzystą wyświetl właściwy
# komunikat
##   użyj operatora modulo % który zwraca resztę z dzielenia  np. 5%2   czyli 2 reszta 0

liczba1 = (float(input("podaj liczbe1: ")))
liczba2 = (float(input("podaj liczbe2: ")))

sumaLiczb = liczba1 + liczba2

if sumaLiczb % 2 == 0:
    print("Suma liczb jest podzielna przez 2.")
else:
    print("Suma liczb nie jest podzielna przez 2.")

## 6. Utwórz prosty kalkulator dla 2 zmiennych podanych przez użytkownika, który obliczy: sumę, różnicę,
## iloczyn, iloraz, potęgę tych liczb, nie zapomnij o stosownych komentarzach informacyjnych dla użytkownika.
number1 = float(input("Podaj liczbe pierwsza: "))
number2 = float(input("Podaj liczbe druga: "))

suma = number1 + number2
roznica = number1 - number2
iloczyn = number1 * number2
potega = number1 ** number2

if number2 != 0:
    iloraz = number1 / number2
else:
    print("Nie dzielimy przez 0!")

print("suma: {}".format(suma))
print("ronica {}".format(roznica))
print("potega {}".format(potega))
print("iloczyn {}".format(iloczyn))
print("iloraz {}".format(iloraz))


## 7. Dla dowolnego x sprawdź wynik działań (x > 1 and x < 13) oraz (c)

dowolnyX = float(input("wprowadz x: "))
if dowolnyX > 1 and dowolnyX < 13:
    print("{} jest wiekszy od 1 i mniejszy od 13".format(dowolnyX))
else:
    print("{} nie jest wiekszy od 1 i nie jest mniejszy od 13".format(dowolnyX))

if dowolnyX != 5 or dowolnyX < 0:
    print("{} jest inny od 5 albo jest mniejszy od 0".format(dowolnyX))
else:
    print("{} jest równy 5 i nie jest mniejszy od 0".format(dowolnyX))

# Zadania dodatkowe:
# 1. Wykonaj mini ankietę tj. poproś użytkownika o następujące informacje: imie, nazwisko, wiek, zadaj mu pytania: "Czy zdrowo się odżywiasz?",
# , "Czy lubisz sport?" i dodatkowo 3 inne własne. Po uzyskaniu wszystkich odpowiedzi wyświetl ich podsumowanie.
# 2. Twoim zadaniem jest przygotowanie uniwersalnego i profesjonalnego życiorysu, złożonego z 5-ciu zdań, które wyświetlisz na ekranie
# Użytkownik wpisuje tylko swoje imie, nazwisko, wiek, zawód, miejsce urodzenia, zainteresowania i ... życiorys jest gotowy.
# 3. Przygotuj dla dziecka, które uczy się czytać zestaw sylab do nauki, ale zrób to inteligentnie tj.
# dziecko wpisuje na klawiaturze 1 spółgłoskę a Ty dodajesz do niej odpowiednie samogłoski i wyświetlasz całość na ekranie
# 4. Użytkownik podaje imie, sprawdź czy to imie to Janusz lub Grażyna
