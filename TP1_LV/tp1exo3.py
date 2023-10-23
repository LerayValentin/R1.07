jour = int(input("Jour(s) :"))
heure = int(input("Heure(s) :"))
minute = int(input("Minute(s) :"))
total = (jour-1)*24*60 + heure*60 + minute
print(total)