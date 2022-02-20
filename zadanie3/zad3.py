#3. Palindrom to coś, co czyta się tak samo od przodu i od tyłu. Hipoteza: weź dowolną liczbę naturalną.
#Jeżeli nie jest palindromem, to zapisz ją od tyłu i dodaj obie liczby. Jeżeli wynik nadal nie jest
#palindromem, kontynuuj, traktując go jako daną. Przerwij, gdy osiągniesz palindrom, albo po 10.
#próbie. Na przykład: 78+87=165, 165+561=726, 726+627=1353, 1353+3531=4884. Napisz program
#sprawdzający hipotezę dla pierwszych 200 liczb naturalnych jako startowych. Czy zawsze osiągniemy
#palindrom?

#funkcja rekurencyjna sprawdzająca hipotezę
def pal_rekurencja(x,n):
    if x == x[::-1]:
        return x    
    if n==0:
        return -1
    return pal_rekurencja(str(int(x)+int(x[::-1])),n-1)

#tworzymy słownik zawierający :
#klucz - liczba, od której zaczynamy
#wartość - palindrom, który udało się znaleźć lub -1, kiedy go nie znaleziono
palindromy={}

#pętla - zaczynamy dla kolejnych 200 liczb
for i in range(1,201):
    palindromy[i] = pal_rekurencja(str(i),10)

#wypisujemy cały wynik
print(palindromy)

#wypisujemy tylko te przypadki, kiedy nie udało się znaleźć palindromu
pal_brak = [k for k,v in palindromy.items() if v == -1]
print("Nie znaleziono palindromów rozpoczynając od liczb: ", pal_brak)