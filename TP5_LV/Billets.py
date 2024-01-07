
somme = int(input("Entrez la somme d'argent à decomposer : "))
temp = somme
b100 = somme // 100
r100 = somme % 100
b50 = r100 // 50
r50 = r100 % 50
b10 = r50 // 10
r10 = r50 % 10
p2 = r10 // 2
r2 = r10 % 2
p1 = r2
print(temp,"euros, c’est donc",b100,"billet(s) de 100,",b50,"de 50,",b10,"de 10,",p2,"pièce(s) de 2 et",p1,"pièce(s) de 1.")
