# déclaration de la fonction ajouter_elt(liste, elt):
def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

lst1 = [0, 1, 2]
lst2 = [ajouter_elt(lst1, len(lst1))]

print((lst1), "\n", type(lst1), "\n", id(lst1))
print((lst2), "\n", type(lst2), "\n", id(lst2))
#lst1 est modifiée par lst2