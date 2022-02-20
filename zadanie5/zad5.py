#5. Komputer jest doskonałym narzędziem służącym do szyfrowania i deszyfrowania tajnych
#wiadomości. W metodzie Gronsfelda, będącą modyfikacją szyfru Cezara, stosuje się klucz liczbowy.
#Biorąc klucz o wartości 31206 i niezaszyfrowany tekst „PROGRAMOWANIE”, uzyskujemy następujący
#szyfrogram:
#31206 31206 312
#PROGR AMOWA NIE
#SSQGX DNQWG QJG
#Kolejne litery są przesuwane o kolejne wartości z klucza. Proszę napisać programy dokonujące
#szyfrowania i deszyfrowania pliku tekstowego zadanym kluczem.
import math
import numpy as np

#zakładamy że poruszamy się po 128 znakach z podstawowej tabeli ASCII
key = 3853214

def encrypt(s,key):
    #tablica wartości ascii znaków
    t1 = np.array([ord(x) for x in s])

    #tablica przesunieć rozszerzona do rozmiaru tekstu
    t2 = str(key)* math.ceil(len(s)/len(str(key)))
    t2 = np.array([int(x) for x in t2[0:len(s)]])

    #przesunięcie liter
    t3 = (t1 + t2) % 128

    return "".join(chr(x) for x in t3)

def decrypt(s,key):
    #tablica wartości ascii znaków
    t1 = np.array([ord(x) for x in s])

    #tablica przesunieć rozszerzona do rozmiaru tekstu
    t2 = str(key)* math.ceil(len(s)/len(str(key)))
    t2 = np.array([int(x) for x in t2[0:len(s)]])

    #przesunięcie liter
    t3 = (t1 - t2) % 128

    return "".join(chr(x) for x in t3)

#plik wejściowy z tekstem jawnym znajduje się w folderze bieżącym
#otwarcie pliku z tekstem jawnym
with open("jawny.txt") as f:
    s = f.read()

#otwarcie nowego pliku do zapisu i zapis szyfrogramu
with open("zaszyfrowany.txt","w") as f:
    f.write(encrypt(s,key))

#otwarcie szyfrogramu i deszyfrowanie

with open("zaszyfrowany.txt") as f:
    e = f.read()


#zapisanie odszyfrowanego tekstu
with open("odszyfrowany.txt","w") as f:
    f.write(decrypt(e,key))

#sprawdzenie przykładu z opisu zadania
print(encrypt("PROGRAMOWANIE", 31206))