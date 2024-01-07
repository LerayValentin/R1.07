# déclaration de la fonction ajouter_elt(lst=[0, 1, 2], elt=3)
def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    return lst

print(ajouter_elt()) #ajoute 3 à la liste
print(ajouter_elt()) #ajoute une nouvelle fois 3 à la liste

def ajouter_carac(ch="abc", elt="d"):
     return ch + elt

print(ajouter_carac())#renvoie abcd
print(ajouter_carac())#renvoie de nouveau abcd car pas d'ajout à une liste comme précédemment, mais une simple concaténation