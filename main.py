wpis = int(input("Wpisz liczbę do dzielenia: "))

zakres = list(range(1,wpis+1))

listaDzielnikow = []

for liczba in zakres:
    if wpis % liczba == 0:
        listaDzielnikow.append(liczba)

print(listaDzielnikow)