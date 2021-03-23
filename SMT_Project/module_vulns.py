import itertools

import os


list_properties = list()
list_negation_properties = list()
Nbre_properties = input ("Donner le nombre de propriétes:")
Nbre_properties = int(Nbre_properties)
i = 0
while i < Nbre_properties:
    list_properties.insert(i, "p" + str(i+1))
    list_negation_properties.insert(i, "(not  p" + str(i+1) + ")")
    i = i+1
Nbre_vulns=input("Donner le nombre de vulnerabilités :")
Nbre_vulns=int(Nbre_vulns)
k=0
tab_vuln = list ()
chaine_vulns=""
while k<Nbre_vulns:
    if Nbre_vulns== 1:
        print("Entrer les propriétés de la vulnérabilité:")
    else:
        if k == 0:
            print("Entrer les propriétés de la " + str (k+1) + " ère vulnérabilité:")
        else:
            print("Entrer les propriétés de la " + str (k + 1) + " ème vulnérabilité:")
    m=0
    s = ""
    prop=""
    vuln=""
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

        if prop.startswith("(not"):
            prop=prop.strip("(not ")
            prop="¬"+prop
            prop=prop.strip(prop[-1])
        print("C'est la prop    "+ prop)
        vuln = vuln + "∧" + prop
        m = m + 1
        vuln = vuln.lstrip('∧')
    print("c'est l'indice de la vulns en question:" + vuln)

    tab_vuln.append(vuln)
    print(tab_vuln)
    chaine_not_vulns="(not(and "+ s +"))"
    print("la vuln hhhhhhhhhhhhhhhhhhhh "+ str(k)+ "est: " +chaine_not_vulns)
    chaine_vulns=chaine_vulns+chaine_not_vulns
    k = k + 1
smt_file_not_vulns=""
smt_file_not_vulns= "(and " +chaine_vulns+ ")"
print("SMT FILLLLLLLE: "+ smt_file_not_vulns)

print("Afficher toutes les vulnerabilité:")
print(tab_vuln)
i=0
while i<len(tab_vuln):
    print("v"+str(i+1)+"= " + tab_vuln[i])
    i=i+1























