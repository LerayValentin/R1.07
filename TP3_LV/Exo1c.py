nbrinfdix = 0
nbrsupdix = 0
nbrsupquinze = 0
n = -1
i = 0

for i in range(10):
    n = float(input("Entrez un nombre entre 0 et 20 : "))
    while n < 0 or n > 20 :
        n = float(input("Le nombre doit être compris entre 0 et 20 : "))
    if n < 10:
        nbrinfdix += 1
    elif 10 <= n < 15:
        nbrsupdix += 1
    else:
        nbrsupquinze += 1

print("Il ya a ", nbrinfdix, "valeur(s) strictement inférieure(s) à 10,", nbrsupdix, "valeur(s) supérieure(s) ou égale(s) à 10 et strictement inférieure(s) à 15, et ", nbrsupquinze, "valeur(s) supérieure(s) ou égale(s) à 15.")




