
from termcolor import colored, cprint



print("++++Les propriétes++++")
Nbre_properties=input("Donner le nombre de propriétes:")
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
print(list_properties)
print(list_negation_properties)





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
print (list_vulns)


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
print(str_not_vulns)