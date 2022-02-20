#6. Korzystając z rachunku prawdopodobieństwa jesteśmy w stanie policzyć szansę, że wśród n osób są
#przynajmniej 2, które mają urodziny tego samego dnia. Proszę napisać program, który sprawdzi to
#empirycznie: należy wylosować n dni urodzin i sprawdzić, czy któryś się powtórzył. Takie losowanie
#powtarzamy wielokrotnie (np. 1000 razy) i sprawdzamy w ilu przypadkach zdarzyło się, że
#przynajmniej 2 osoby miały urodziny tego samego dnia.
#Wersja nieco trudniejsza: niech to nie będą 2 osoby, tylko k osób.

import random
from collections import Counter

#liczba losowanych dni urodzin
N = 500

#liczba przypadków
cases = 1000

#liczba osób mających urodziny tego samego dnia
k = 5
result={}

for i in range(1,cases+1):

#losowanie list 
    days=[random.randint(1,29) for i in range(N)]
    months=[random.randint(1,13) for i in range(N)]


#łączenie dzień+miesiąc
    dates = ["{}.{}".format(x1,x2) for x1,x2 in zip(days,months)]

#zliczanie tych samych wartości
    dates = Counter(dates)

#ile powtórzonych dat dla danej liczby osób k
    powtorzone_daty = len([key_ for key_,value_ in dates.items() if value_ >= k])

# wstawianie do słownika wynikowego : Przypadek nr i : liczba powtórzeń 
    result["Przypadek nr {}".format(i)] = powtorzone_daty

print(result)