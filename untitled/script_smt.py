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

print("+++Les fonction de securié++++")
Nbre_security_functions=input("Donner le nombre de fonctions de securité:")

Nbre_security_functions=int(Nbre_security_functions)
j=0
while j<Nbre_security_functions:
    x= input("Donner le numéro de la propriété de la "+ str (j + 1) + " fonctions de securité:")
    x=int(x)
    list_security_functions.insert(j, (list_negation_properties[x]))
    j=j+1
print(list_security_functions)
print("+++Les vulns++++")
Nbre_vulns=input("Donner le nombre de vulnerabilités:")
Nbre_vulns=int(Nbre_vulns)
k=0

while k<Nbre_vulns:
    Nbre_propr=input("Entrer le nombre des propriétés de la " + str (k+1) + " ère/ème vulnérabilité:")
    Nbre_propr=int(Nbre_propr)
    m=0
    s = ""
    while m < Nbre_propr:
        p = input("Entrer la " + str(m+1) + " ère/ème proprité:  ")
        s=s+ p + " and "
        print (s)
        m = m + 1
    list_vulns.insert(k, s)
    k=k+1
print(list_vulns)


