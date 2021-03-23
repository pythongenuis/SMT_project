import itertools
from termcolor import colored, cprint
import os

print(colored("*******************************************************" , "red"))
print(colored("Properties","green") , colored("********************************","red"))
print(colored("*******************************************************" , "red"))
Nbre_properties=input("Donner le nombre de propriétes:")
Nbre_properties=int(Nbre_properties)
print(Nbre_properties)

list_properties=list()
list_negation_properties=list()
list_security_functions=list()
list_vulns=list()
i=0
while i<Nbre_properties:
    list_properties.insert(i, "p" + str (i+1))
    list_negation_properties.insert(i, "(not  p" + str (i+1) + ")")
    i=i+1
#print(list_properties)
#print(list_negation_properties)
n=0
while n<Nbre_properties:
    chaine = list_negation_properties[n]
    m=0
    while m<Nbre_properties:
        if n!=m:
            chaine= chaine + " and " +list_properties[m]
        m=m+1
    n=n+1
    #print(chaine)
S=list_properties + list_negation_properties
#print(S)

list_test=list()


#les combinaisons de fonctions de sécurité

for L in range(0, len(S)+1):
    for subset in itertools.combinations(S, L):
        if len(subset)== Nbre_properties:
            list_test.append(subset)
            #print(subset)
#print(list_test)


z=0
list_combinaisons_fonctions=list()
while z<len(list_test):
    ch = '('
    p=0
    while p<Nbre_properties-1:
        # print(list_test[z][p])
        ch=ch+ list_test[z][p]+ " and "
        p=p+1
    ch = ch + list_test[z][Nbre_properties-1] +" )"
    z=z+1
    #print(ch)
    list_combinaisons_fonctions.append(ch)
#print("Tableau des combinaisons:\n")
#print(list_combinaisons_fonctions)
list_combinaisons_fonctions.pop(0)
#print("Tableau des combinaisons hello:\n")
#print(list_combinaisons_fonctions)

print(colored("*******************************************************" , "red"))
print(colored("Saisie de vulnérabilté","green") , colored("********************************","red"))
print(colored("*******************************************************" , "red"))


Nbre_vulns=input("Donner le nombre de vulnerabilités :")
Nbre_vulns=int(Nbre_vulns)
k=0
while k<Nbre_vulns:
    if Nbre_vulns== 1:
        print("Entrer les propriétés de la vulnérabilité:")
    else:
        if k == 0:
            print("Entrer les propriétés de la " + str (k+1) + " ère vulnérabilité:")
        else:
            print("Entrer lespropriétés de la " + str (k + 1) + " ème vulnérabilité:")
    m=0
    s = ""
    while m < Nbre_properties:
        if m==0:
            prop = input ("Entrer la " + str (m + 1) + " ère proprité:  ")
        else:
            prop = input ("Entrer la " + str (m + 1) + " ème proprité:  ")
        if m < Nbre_properties - 1:
            s = s + prop + " and "
        else:
            s = s + prop
        m = m + 1
    list_vulns.insert (k, s)
    k = k + 1
#print (list_vulns)


print(colored("*******************************************************" , "red"))
print(colored("Creation of the SMT file","green") , colored("********************************","red"))
print(colored("*******************************************************" , "red"))

s=""
stri=""
str_not_vulns=""
i=0
while i<len(list_vulns):
    s="( " +str(list_vulns[i])+ ")"
    stri=stri+s
    i=i+1
str_not_vulns="(not "+stri + ")"
#print(str_not_vulns)
i=0
print("la liste des combinaison que va prendre le fichier SMT:\n")
input_smt_file=""

input_smt_file="(and " + str_not_vulns + list_combinaisons_fonctions[i] + ")"
print(input_smt_file)
while i<len(list_combinaisons_fonctions):

    with open ('file.smt', 'w') as mon_fichier:
        mon_fichier.write("(set - logic ALL)\n")
        mon_fichier.write("(set - option :produce-models true)\n")
        mon_fichier.write("(assert ( "+input_smt_file+"))\n")
        mon_fichier.write("(check - sat)")
    mon_fichier.close()



















