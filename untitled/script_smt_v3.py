import itertools
import os
from termcolor import colored, cprint
print(colored("*******************************************************" , "red"))
print(colored("Saisie des propriété","green") , colored("********************************","red"))
print(colored("*******************************************************" , "red"))
Nbre_properties=input("++Donner le nombre de propriétes:")
Nbre_properties=int(Nbre_properties)
print(Nbre_properties)
i=0
list_properties=list()
list_negation_properties=list()
list_security_functions=list()
list_vulns=list()
while i<Nbre_properties:
    list_properties.insert(i, "p" + str (i+1))
    list_negation_properties.insert(i, "(not  p" + str (i) + ")")
    i=i+1
# La list des prop
print(list_properties)
print(colored("*******************************************************" , "red"))
print(colored("Saisie des fonctions de sécurtité","green") , colored("********************************","red"))
print(colored("*******************************************************" , "red"))

list_security_functions= list()
Nbre_security_fucntions=input("Donnez le nombre de fonctions de sécurité:")
Nbre_security_fucntions=int(Nbre_security_fucntions)
i=0
while i< Nbre_security_fucntions:
    if i==0:
        prop=input("Donnez le numéro de la  proprités de la 1 ère fonction de sécurité:")

    else:
        prop=input("Donnez le numéro de la  proprités de la " + str(prop) +" ème fonction de sécurité:")
    prop=int(prop)
    list_security_functions.insert(i, "not p" + str (prop))
    i=i+1
print(list_security_functions)






print(colored("*******************************************************" , "red"))
print(colored("Saisie de vulnérabilté","green") , colored("********************************","red"))
print(colored("*******************************************************" , "red"))


Nbre_vulns=input("Donner le nombre de vulnerabilités :")
Nbre_vulns=int(Nbre_vulns)
k=0
chaine_vulns=""
while k<Nbre_vulns:
    if Nbre_vulns== 1:
        print("Entrer les propriétés de la vulnérabilité:")
    else:
        if k == 0:
            print("Entrer les propriétés de la " + str (k+1) + " ère vulnérabilité:")
        else:
            print("Entrer le spropriétés de la " + str (k + 1) + " ème vulnérabilité:")
    m=0
    s = ""
    prop=""
    while m < Nbre_properties:
        if m==0:
            prop = input ("Entrer la " + str (m + 1) + " ère proprité:  ")
            if prop.startswith("not") == True:
                prop= "(" +str(prop)+ ")"

        else:
            prop = input ("Entrer la " + str (m + 1) + " ème proprité:  ")
            if prop.startswith("not") == True:
                prop= "(" +str(prop)+ ")"

        s=s+ " " +prop
        # if m < Nbre_properties - 1:
        #     s = s + prop + " and "
        # else:
        #     s = s + prop
        m = m + 1
    chaine_not_vulns="(not(and "+ s +"))"
    print("la vuln hhhhhhhhhhhhhhhhhhhh "+ str(k)+ "est: " +chaine_not_vulns)
    chaine_vulns=chaine_vulns+chaine_not_vulns
    k = k + 1
smt_file_not_vulns=""

smt_file_not_vulns= "(and " +chaine_vulns+ ")"
print("SMT FILLLLLLLE: "+ smt_file_not_vulns)


print(colored("Les caractéristiques du composant:", "red"))
print(colored("Les propriétés du composant:", "blue"))
i=0
while i<len(list_properties):
    print("P" +str (i+1) + " = " + list_properties[i])
    i=i+1

print(colored("Les fonctions de sécurité:", "blue"))
i=0
while i<len(list_security_functions):
    print("F" + str(i+1)+" = "+list_security_functions[i])
    i=i+1

print(colored("Le format SMT de la combinaisons des vunerabilté:", "blue"))
print(smt_file_not_vulns)

#nouveau état du système après la migration


new_state=list()
Nbrepropnewstate=input("Donnez le nombre de propriétés de l'état du système après migration:")
Nbrepropnewstate = int(Nbrepropnewstate)
i=0
while i< Nbrepropnewstate:
    if i==0:
        prop=input("Donnez  la 1 ère propriété:")
    else:
        prop=input("Donnez la " + str(i+1) +" ème propriété:")
    new_state.insert(i, prop)
    i=i+1
print(new_state)
i=0
p=""
str_new_state=""
while i<len(new_state):
    if new_state[i].startswith("not") == True:
        p="(" + new_state[i] + ")"
    else:
        p=new_state[i]

    str_new_state=str_new_state+ " " +str(p)
    i = i + 1
new_state_smt="(and  "+str_new_state + ")"
print("The new state is :"+  new_state_smt)

#Générer le fichier SMT pour tester l'état du système après la migration

smtfile= "(and "+ smt_file_not_vulns + " " +new_state_smt +")"

mon_fichier = open("fichier.smt", "w")
mon_fichier.write("(set-logic ALL)\n")
mon_fichier.write("(set-option :produce-models true)\n")
i=0
while i < Nbre_properties:
    mon_fichier.write ("declare-const p"+ str(i+1)+ " Bool)\n")
    i = i+1
mon_fichier.write("(assert (and " + smtfile +" ))\n")
mon_fichier.write("(check-sat)\n")
mon_fichier.write("(get-model)\n")
mon_fichier.close()