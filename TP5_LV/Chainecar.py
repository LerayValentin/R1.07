# Algorithme 1
x = str(input("Entrez une chaine de caractères : "))
T = x + '\0' * (100 - len("Bonjour"))
taille = 0
while T[taille] != '\0':
    taille += 1
print("La taille de la chaîne est :", taille)

# Algorithme 2
T = x + '\0' * (100 - len("Bonjour"))
voyelles = sum(1 for c in T if c.lower() in "aeiou")
taille = len(T) - 1
pourcentage = (voyelles / taille) * 100
print("Le pourcentage de voyelles est :", pourcentage, "%")

# Algorithme 3
T = x + '\0' * 82
debut_occurrence = -1
taille_T = len(T)
index = 0
while index < taille_T - 4 and debut_occurrence == -1:
    if T[index:index+5] == 'wagon':
        debut_occurrence = index
    index += 1
if debut_occurrence != -1:
    print("La sous-chaîne 'wagon' existe à la position :", debut_occurrence)
else:
    print("La sous-chaîne 'wagon' n'existe pas dans T")

# Algorithme 4
T = x + '\0' * 62
occurrences = 0
taille_T = len(T)
index = 0
while index < taille_T - 4:
    if T[index:index+5] == 'wagon':
        occurrences += 1
    index += 1
print("Le nombre d'occurrences de 'wagon' est :", occurrences)
