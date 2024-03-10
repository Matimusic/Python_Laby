#### Zadanie 1
## Poniżej masz 3 zbiory genów, 3 różnych pacjentów chorych na różne choroby
## Odpowiedz na poniższe pytania:
## a) Które elementy/geny są wspólne dla wszystkich pacjentów?
## b) Jakie elementy/geny są wspólne dla 2 pacjentów?
## c) Jakie elementy/geny występują wyłącznie w przypadku 1 choroby?

import math

print('zadanie 1')
set_gene1 = set(['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
set_gene2 = set(['SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421', 'ANGC3', 'WELNT14', 'EOO11',
                'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
set_gene3 = set(['SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3','GALNT14', 'ERCC11',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT15', 'EOO1',
                'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'])

print("a) wspolne geny pacjentow: ",set_gene1.union(set_gene2.union(set_gene3)))

print("b) Wspólne geny tylko dwa dwoch pacjentow: ",set_gene1.union(set_gene2))

print("c) Geny występujące tylko w jednej chorobie: ",set_gene1.intersection(set_gene2.intersection(set_gene3)))


# ##########Zadanie 2
# ### Sprawdź czy w poniższym zbiorze występuje gen 'FGFR4' oraz 'FGERA4', jeśli tak to wskaż index
# ### genu na liście
#
lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']

print('\nzadanie 2')
for i in range(0, len(lista_gene1)):
    if lista_gene1[i] == 'FGFR4' or lista_gene1[i] == 'FGERA4':
        print('indeksy: ',i)

print('\nzadanie 3')


#####Zadanie 3
## Przekopiuj dowolny ale długi fragment tekstu ze strony:
## http://www.national-geographic.pl/ludzie/dziennikarka-kontra-komputer-kto-napisze-lepszy-tekst
## sprawdź:

## a) ile razy w tekście występuje słowo Emma
textNational = ("""Emma i ja dostałyśmy instrukcje, by o 9:30 napisać o oficjalnych danych dotyczących zatrudnienia w Wielkiej Brytanii i wysłać nasze wersje do redaktora. Byłam przekonana, że Emma będzie ode mnie szybsza, ale miałam też szczerą nadzieję, że to ja będę lepsza. 
 

Twórca Emmy, start-up o nazwie Stealth, nazywa ją „niezależną sztuczną inteligencją” zaprojektowaną, by świadczyć profesjonalne usługi, takie jak badania i analiza. Odkąd w modzie są prognozy, że sztuczna inteligencja (ang. artificial intelligence, AI) zastąpi pracowników biurowych, w tym również dziennikarzy, chciałam to sprawdzić na własnej skórze. 
 

Emma rzeczywiście była szybka – dane wysłała w 12 minut. Mi zajęło to 35. Jej wersja była też lepsza, niż się spodziewałam. Fakty się zgadzały, zawarła nawet trafne treści, takie jak możliwość Brexitu (choć podzielała wątpliwą opinię, że wyjście z Unii Europejskiej byłoby niezwykle korzystne dla brytyjskiej gospodarki). """)

cout_emma = textNational.lower().count("emma")
print('slowo emma wystepuje: ', cout_emma)

## b) zamień całość tekstu na duże litery
upper_text = textNational.upper()
print("tekst z powiekszonymi literami: \n", upper_text)

## c) wstaw poszczególne wyrazy jako elementy listy
word_list = textNational.split()
print("lista poszczególnch wyrazów:")
print(word_list)

## d) ile zdań jest w analizowanym tekście?
senetence_list = textNational.split('.')
num_sentences = len(senetence_list) - 1
print("W tekscie wystepuje ", num_sentences, "zdań. \n")

########Zadanie 4
## Sprawdź czy dowolnie podana przez użytkownika liczba jest parzysta czy nieparzysta

number = int(input("Podaj liczbe: "))

if (number % 2) == 0:
    print('Podana liczba jest parzysta')
else:
    print('Podana liczba nie jest parzysta')


########Zadanie 5
## W zależności od procentu uzyskanych punktów z kolokwium z Python'a
## student uzyskuje określoną ocenę końcową z laboratorium
## np 50%-60% to 3.0, 61%-70% to 3.5, ...., 91%-100% to 5.0 to 5.0 - if

## Korzystając z instrukcji i/if, napisz program który będzie wyznaczał ocenę studenta na podstawie uzyskanych punktów (max 15pkt)
########### Pętla for  - jako wektor

punkty = int(input("Podaj ilosc swoich punktow: "))
if punkty/15 < 0.51:
    print('Nie zaliczyles')
elif 0.51 <= punkty/15 < 0.61:
    print('Zaliczyles na 3')
elif 0.61 <= punkty/15 < 0.71:
    print('Zaliczyles na 3.5')
elif 0.71 <= punkty/15 < 0.81:
    print('Zaliczyles na 4')
elif 0.81 <= punkty/15 < 0.91:
    print('Zaliczyles na 4.5')
elif 0.91 <= punkty/15 <= 1:
    print('Zaliczyles na 5')
else:
    print('Podana ilosc punktów jest błędna! MAX 15')

# # #Zadanie 6
### Napisz skrypt, ktory obliczy sume ciagu: 1+1/2+1/3+...+1/n korzystając z pętli for
### Zmienna wejsciowa n jest dowolnia, m-parametr wprowadzany jako dane wejsciowe przez uzytkownika (użyj input)

print('\n Podany jest ciąg Sn = n + 1. Wpisz liczbe n, którego wyrazu chcesz obliczyć sume: ')
n_ciag = int(input('Podaj n: '))
wynik_Ciagu = 0
for i in range(1, n_ciag+1):
    wynik_Ciagu += i + 1

print('Synik sumy wysnoi: ', wynik_Ciagu)


###### Zadanie 7
###### Calculate the root of the numbers from 1 to 10 using the while loop
###### Oblicz pierwiastek liczb od 1 do 10 korzystając z pętli while
numbers = 1
while numbers <= 10:
    squere_root = math.sqrt(numbers)
    print(f'Pierwiastek z {numbers} wynosi {squere_root}')
    numbers += 1