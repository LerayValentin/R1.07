nbr = int(input("Entrez un nombre entier : "))

if nbr < 0:
    if nbr % 2 == 0:
        print("Le nombre négatif et pair")
    else:
        print("Le nombre est négatif et impair")

elif nbr > 0:
    if nbr % 2 == 0:
        print("Le nombre est positif et pair")
    else:
        print("Le nombre est positif et impair")

else:
    print("Le nombre est 0 (et il est pair)")
