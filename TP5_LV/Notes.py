notecoef = []
note = []
coef = []
for i in range(1, 6):
    notecoef.append(str(input("Veuillez entrer la note du module {} et le coefficient correspondant séparés d'un espace : ".format(i))))
    tmp = notecoef[i-1].split(" ")
    note.append(float(tmp[0]))
    coef.append(float(tmp[1]))
print(note, coef)
moy = (note[0]*coef[0] + note[1]*coef[1] + note[2]*coef[2] + note[3]*coef[3] + note[4]*coef[4]) / sum(coef)
print("L'étudiant a une moyenne de {}".format(moy))

if moy > 10:
    admis = 1
for i in range(5):
    if note[i] < 8:
        admis = 0

if admis == 1:
    print("L'étudiant est admis")
else:
    print("L'étudiant n'est pas admis")