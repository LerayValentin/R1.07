#a
L1= [0]*3
print("a)")
print(L1, "\n",type(L1),"\n",id(L1))

#b
print("b)")
print(L1[0], "\n",type(L1[0]),"\n",id(L1[0]))
print(L1[1], "\n",type(L1[1]),"\n",id(L1[1]))
print(L1[2], "\n",type(L1[2]),"\n",id(L1[2]))
#Les 3 ont les mêmes types, id, et valeurs

#c
print("c)")
L1[1] += 1
print(L1, "\n",type(L1),"\n",id(L1))
#L'id de la liste ne change pas

#d
print("d)")
print(L1[0], "\n",type(L1[0]),"\n",id(L1[0]))
print(L1[1], "\n",type(L1[1]),"\n",id(L1[1]))
print(L1[2], "\n",type(L1[2]),"\n",id(L1[2]))
#L1[1] n'a plus le même id que les autres ==> il s'agit d'un nouvel objet

#e
print("e)")
C1 = ["m","a","c","h","a","i","n","e"]
print(C1, "\n",type(C1),"\n",id(C1))
for i in range(len(C1)):
    print((C1[i]), "\n", type(C1[i]), "\n", id(C1[i]))
#ils on tous un id unique, sauf les caractère apparaissant plusieurs fois