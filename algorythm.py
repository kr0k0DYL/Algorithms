wiersz = 0
tablica=[]
with open("sygnaly.txt") as file:
    for linia in file:
        wiersz= wiersz+1
        linia = linia.strip()
        if(wiersz % 40 == 0 ):
            tablica.append(linia)


for i in range(len(tablica)):
    print(tablica[i][9],end="")
    wyraz = tablica[i]

