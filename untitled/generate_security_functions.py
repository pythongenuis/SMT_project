import itertools
print("++++Les propriétes++++")
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
print(list_properties)
print(list_negation_properties)
n=0
while n<Nbre_properties:
    chaine = list_negation_properties[n]
    m=0
    while m<Nbre_properties:
        if n!=m:
            chaine= chaine + " and " +list_properties[m]
        m=m+1
    n=n+1
    print(chaine)
S=list_properties + list_negation_properties
print(S)

list_test=list()
print("ddddddddddddddddddddddddddddddddddddddddddddddd")
for L in range(0, len(S)+1):
    for subset in itertools.combinations(S, L):
        if len(subset)== Nbre_properties:
            list_test.append(subset)
            print(subset)
print(list_test)
print("hellllllllllllllllllllllllllllo")

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
    print(ch)
    list_combinaisons_fonctions.append(ch)
print("Tableau des combinaisons:\n")
print(list_combinaisons_fonctions)
list_combinaisons_fonctions.pop(0)
print("Tableau des combinaisons hello:\n")
print(list_combinaisons_fonctions)



















