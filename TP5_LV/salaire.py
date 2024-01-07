h = float(input("Entrez le nombre d'heures travaillées : "))
salh = float(input("Entrez le salaire horaire : "))

sal = min(h, 160) * salh
if h > 160:
    sal += min(max(h - 160, 0), 40) * salh * 1.25
if h > 200:
    sal += max(h - 200, 0) * salh * 1.5
print(f"Le salaire total est de {sal} euros.")
