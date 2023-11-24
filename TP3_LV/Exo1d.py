y = 0
x = int(input("Entrez un nombre supérieur à 1 : "))
while x < 1:
    x = int(input("Le nombre doit être supérieur à 1 : "))
while y*(y+1)/2 <= x:
    y += 1
print("Le nombre recherché est", y-1,)




