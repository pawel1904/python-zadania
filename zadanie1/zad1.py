#1. Proszę napisać program rozwiązujący układ równań N równań liniowych O N niewiadomych.
#Dane dla problemu należy wczytać z pliku tekstowego. W pierwszym wierszu znajduje się liczba
#równań N, kolejne wiersze zawieraja macierz współczynników oraz wyrazy wolne, na przykład plik:
#3
#1 2 3 7
#-1 2 4 6
#2 1 1 13
#Odpowiada układowi 3 równań o 3 niewiadomych w postaci:
#X+2Y+3Z=7
#-X+2Y+4Z=6
#2X+Y+Z=13
#Program powinien uwzględnić przypadki układu nieoznaczonego i sprzecznego. Wskazówka:
#rozważyć zastosowanie biblioteki numpy.

########################################################################################
import numpy as np
########################################################################################
#wczytanie danych z pliku
#dla uproszczenia przyjąłem załozenie, że plik znajduje się w tym samym folderze co skrypt
#brak obsługi błędów np. litera zamiast liczby
#wrzuciłem trzy pliki - dla układu oznaczonego, nieoznaczonego i sprzecznego
#dla każdego można sobie sprawdzic działanie, podstawiając odpowiednią wartość pod zmienną FILE_

#FILE_ = "dane_sprzeczny.txt"
#FILE_ = "dane_nieoznaczony.txt"
FILE_ = "dane_oznaczony.txt"

with open(FILE_) as f:
    lines = f.readlines()

########################################################################################

#konwersja na listę list - obcinanie znaków nowej linii i podział napisów po spacji
#przypisanie wyników do zmiennej wsp_list
wsp_list= [ x.strip().split(" ") for x in lines]

#pierwsza wartość to liczba równań/niewiadomych
N = int(wsp_list[0][0])

#współczynniki rozbijamy na dwie tablice numpy i zmieniamy typ na float
#A - tablica współczynników przy niewiadomych
#b - tablica wyrazów wolnych
A = np.array(wsp_list[1:], dtype=float)[:,:-1]
b = np.array(wsp_list[1:], dtype=float)[:,-1]

#metoda pierwsza - użycie wbudowanej funkcji z biblioteki linalg
#zadziała wyłącznie przy założeniu, że układ ma jedno rozwiązanie
#w innym przypadku nie wiemy, czy układ jest nieoznaczony czy sprzeczny
#definicja funkcji
print("="*50)
print("Metoda pierwsza. Wbudowana funkcja solve()")
try:
    result = np.linalg.solve(A, b)
    print("Układ jest oznaczony. Rozwiązanie:", result)
except np.linalg.LinAlgError as e:
     #jeżeli przechwyciliśmy wyjątek (czyli układ sprzeczny lub nieoznaczony) to zwracamy tablicę wartości NaN
    print("Układ nieoznaczony lub sprzeczny")


#metoda druga, trochę bardziej na piechotę, przy pomocy wzorów Cramera
#https://www.naukowiec.org/wiedza/matematyka/twierdzenie-cramera_616.html

print("="*50)
print("Metoda druga. Wyznaczniki.")

#wyznacznik główny
wA = np.linalg.det(A)

#wyznaczniki dla macierzy Ai powstałej poprzez podstawienie za i-tą kolumne macierzy wyrazów wolnych
wlist = []
for i in range(N):
    tmp = np.copy(A)
    tmp[:,i] = b
    wlist.append(np.linalg.det(tmp))
    
#zmiana z listy na tablicę numpy
res = np.array(wlist)
#jeśli wyznacznik główny jest różny od zera to istnieje dokładnie jedno rozwiązanie,
if wA!=0:
    print("Układ jest oznaczony. Rozwiązanie: ", res/wA)
#jeśli wyznacznik główny i wszystkie wyznaczniki szczególne są równe zero to układ ma nieskończenie wiele rozwiązań
elif (res==0).all():
    print("Układ jest nieoznaczony")
#jeśli wyznacznik główny jest równy zero, a któryś (przynajmniej jeden) z wyznaczników szczególnych jest różny od zera, to układ jest sprzeczny.
else: 
    print("Układ jest sprzeczny")

print("="*50)
