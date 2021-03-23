import itertools

import os
l=[1 ,2,3]
ll=[1,2,3]
if  l[0]== ll[0]:
    print(l[0])


Nbre_properties=input("Donner le nombre de propriétes:")
Nbre_properties=int(Nbre_properties)
print("Le nombre de propriété est: " + str(Nbre_properties))
#
# list_properties=list()
# list_security_functions=list()
# i=0
# while i<Nbre_properties:
#     list_properties.insert(i, "p" + str (i+1))
#
#     i=i+1
# print(list_properties)
#
#
#
# Nbre_security_fucntions=input("Donnez le nombre de fonctions de sécurité:")
# Nbre_security_fucntions=int(Nbre_security_fucntions)
# i=0
# while i< Nbre_security_fucntions:
#     if i==0:
#         prop=input("Donnez le numéro de la  proprités de la 1 ère fonction de sécurité:")
#
#     else:
#         prop=input("Donnez le numéro de la  proprités de la " + str(prop) +" ème fonction de sécurité:")
#     prop=int(prop)
#     list_security_functions.insert(i, "not p" + str (prop))
#     i=i+1
# print(list_security_functions)
#
#
# new_state=list()
# Nbrepropnewstate=input("Donnez le nombre de propriétés de l'état actuel du système:")
# Nbrepropnewstate = int(Nbrepropnewstate)
# i=0
# while i< Nbrepropnewstate:
#     if i==0:
#         prop=input("Donnez  la 1 ère propriété:")
#     else:
#         prop=input("Donnez la " + str(i+1) +" ème propriété:")
#
#     new_state.insert(i, prop)
#     i=i+1
# print("le nouveau etat :")
# print(new_state)
i=0
k=0
list_security_functions=['not p1', 'not p2', 'not p3']
new_state=['p1', 'p2', 'not p3']

list_non_existant=list()
while i<len(list_security_functions):
    j=0
    while j<len(new_state):
        if list_security_functions[i] == new_state[j]:
            print(new_state[j])
            k=k+1
        else:
            list_non_existant.append(list_security_functions[i])
        j=j+1
        break
    i=i+1
if(k==len(list_security_functions)):
    print("Aucune des fonctions de sécurité ne peut remedier aux vulnerabilité presentent dans cet état")
else:
    print("HELLO")
    print(list_non_existant)

