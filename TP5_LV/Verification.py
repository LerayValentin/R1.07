import os
from datetime import datetime

fichier1 = str(input("Entrez le nom du premier fichier : "))
fichier2 = str(input("Entrez le nom du deuxième fichier : "))
print("\n")
if os.path.isfile(fichier1):
        taille1 = os.path.getsize(fichier1)
        date_modification1_timestamp = os.path.getmtime(fichier1)
        date_modification1 = datetime.fromtimestamp(date_modification1_timestamp)
        print(f"La taille du fichier {fichier1} est de {taille1} octets")
        print(f"Dernière modification : {date_modification1}")
else:
        print(f"Le fichier {fichier1} n'existe pas.")
print("\n")
if os.path.isfile(fichier2):
        taille2 = os.path.getsize(fichier2)
        date_modification2_timestamp = os.path.getmtime(fichier2)
        date_modification2 = datetime.fromtimestamp(date_modification2_timestamp)
        print(f"Taille du fichier {fichier2}: {taille2} octets")
        print(f"Dernière modification : {date_modification2}")
else:
        print(f"Le fichier {fichier2} n'existe pas.")

if 'date_modification1' in locals() and 'date_modification2' in locals():
    if date_modification1 > date_modification2:
        print(f"\nLe fichier le plus récent est : {fichier1}")
    elif date_modification1 < date_modification2:
        print(f"\nLe fichier le plus récent est : {fichier2}")
    else:
        print("\nLes deux fichiers ont la même date de modification.")
