import random
na = random.randint(0, 100)
compteur = 0
n = -1
while n != na:
    n = float(input("Trouvez le nombre entre 0 et 100! : "))
    if n < na:
        compteur += 1
        print ("Le nombre mystère est supérieur!")
    elif n > na:
        compteur += 1
        print("Le nombre mystère est inférieur!")
    else:
        compteur += 1
        print("Bien joué, vous avez trouvé le nombre mystère!")
