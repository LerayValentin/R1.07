x = int(input("Choisissez entre la boucle while (tapez 1) et la boucle for (tapez 2) : "))
n = int(input("Entrez un nombre dont vous aimeriez savoir la factorielle : "))
a = 1

if x == 1:
    print("Vous avez choisi la boucle while.")
    while n != 1:
        a = a*n
        n -= 1
        print(a)
    print("Voici votre nombre : ", a)

if x == 2:
    print("Vous avez choisi la boucle for.")
    for i in range(1, n+1):
        a = a*i
        print(a)
    print("Voici votre nombre : ", a)
    