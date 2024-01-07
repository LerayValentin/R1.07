x = str(input("Entrez une chaîne de caractères : "))

if (x == x[::-1]):
    print("L'entrée est un palindrome")
else:
    print("L'entrée n'est pas un palindrome")