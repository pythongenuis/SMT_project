import itertools

chaine="10000.smt"
chaine.strip(".smt")
print(chaine[0:-4])
file_to_write_vulns="v.txt"

list_properties = list()

Nbre_properties = input("Donner le nombre de propriétés:")

Nbre_properties = int(Nbre_properties)

while i < Nbre_properties:
    list_properties.insert(i, "p" + str(i+1))
    # list_negation_properties.insert(i, "(not  p" + str(i+1) + ")")
    i = i+1
print("La list des propriété")
print(list_properties)


list_built_vulns_smt=list()
list_built_vulns_txt=list()
i = 0
while i < Nbre_properties:
    list_properties.insert(i, "p" + str(i+1))
    # list_negation_properties.insert(i, "(not  p" + str(i+1) + ")")
    i = i+1
#print(list_properties)
#Générer toute les combinaisons
for L in range(1, len(list_properties)+1):
    for subset in itertools.combinations(list_properties, L):
        #print(subset)
        list_combination.append(subset)
#print(list_combination)
#print(len(list_combination))
#Générer les vulnérabilté avec une seule prpriété
i=0
str_add_smt = ""
str_add_txt = ""
list_temp_vulns_smt = list()
list_temp_vulns_txt = list()
while i<len(list_properties):
    list_vulns_temp_smt = list()
    #list_vulns_temp_txt = list()
    str_add_smt = "(not " + str(list_properties[i]) + ")"
    #str_add_txt = "¬" + str(list_properties[i])
    vulns_built_temp = ""
    vuln_txt_temp = ""
    j=0
    while j < len(list_properties):

        if i!=j:
            list_vulns_temp_smt.append(list_properties[j])
            #list_vulns_temp_txt.append(list_properties[j])
        j=j+1
    list_vulns_temp_smt.append(str_add_smt)
    #list_vulns_temp_txt.append(str_add_txt)
    i=i+1
    #print(list_vulns_temp_smt)
    #print(list_vulns_temp_txt)
    m=0
    while m<len(list_vulns_temp_smt)-1:
        vulns_built_temp=vulns_built_temp+str(list_vulns_temp_smt[m]) + " "
        #vuln_txt_temp=vuln_txt_temp+str(list_vulns_temp_txt[m]) + " " + "∧" + " "
        m=m+1
    vulns_built_temp = vulns_built_temp + list_vulns_temp_smt[m]
    #vuln_txt_temp = vuln_txt_temp + list_vulns_temp_txt[m]
    list_temp_vulns_smt.append(vulns_built_temp)
    #list_temp_vulns_txt.append(vuln_txt_temp)
str_and_smt = "(and "
str_finla_smt = ") "
str_start = "(not (and "
str_end = " )) "
str_vulns_file_smt=""
for element in list_temp_vulns_smt:
    print(element)
    list_temp_vulns_smt[list_temp_vulns_smt.index(element)] = str_start + str(element) + str_end
    print(element)
print(list_temp_vulns_smt)
for element in list_temp_vulns_smt:
    str_vulns_file_smt=str_vulns_file_smt+str(element)
str_vulns_file_smt=str_and_smt +str_vulns_file_smt+str_finla_smt
print(str_vulns_file_smt)
