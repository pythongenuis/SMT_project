import itertools
file_to_write_vulns=input("Donnez le nom du fichier où les vulnérabilité seront écrites:")

char_erase = input("Pour effacer le contenu du fichier, veuillez taper \"E\" :")
if char_erase == "E":
    open(file_to_write_vulns, 'w').close()
list_properties = list()
list_combination=list()
list_negation_properties = list()
Nbre_properties = input("Donner le nombre de propriétés:")
Nbre_properties = int(Nbre_properties)
list_partial_built_vulns_smt=list()
list_partial_built_vulns_txt=list()
list_built_vulns_smt=list()
list_built_vulns_txt=list()
i = 0
while i < Nbre_properties:
    list_properties.insert(i, "p" + str(i+1))
    list_negation_properties.insert(i, "(not  p" + str(i+1) + ")")
    i = i+1
#print(list_properties)
#Générer toute les combinaisons
for L in range(0, len(list_properties)+1):
    for subset in itertools.combinations(list_properties, L):
        #print(subset)
        list_combination.append(subset)
#print(list_combination)
#print(len(list_combination))
#Générer les vulnérabilté avec une seule prpriété
i=0
str_add_smt=""
str_add_txt=""
list_temp_vulns_smt = list()
list_temp_vulns_txt = list()
while i<len(list_properties):
    list_vulns_temp_smt = list()
    list_vulns_temp_txt = list()
    str_add_smt = "(not " + str(list_properties[i]) + ")"
    str_add_txt = "¬" + str(list_properties[i])
    vulns_built_temp = ""
    vuln_txt_temp = ""
    j=0
    while j < len(list_properties):

        if i!=j:
            list_vulns_temp_smt.append(list_properties[j])
            list_vulns_temp_txt.append(list_properties[j])
        j=j+1
    list_vulns_temp_smt.append(str_add_smt)
    list_vulns_temp_txt.append (str_add_txt)
    i=i+1
    #print(list_vulns_temp_smt)
    #print(list_vulns_temp_txt)
    m=0
    while m<len(list_vulns_temp_smt)-1:
        vulns_built_temp=vulns_built_temp+str(list_vulns_temp_smt[m]) + " "
        vuln_txt_temp=vuln_txt_temp+str(list_vulns_temp_txt[m]) + " " + "∧" + " "
        m=m+1
    vulns_built_temp = vulns_built_temp + list_vulns_temp_smt[m]
    vuln_txt_temp = vuln_txt_temp + list_vulns_temp_txt[m]
    list_temp_vulns_smt.append(vulns_built_temp)
    list_temp_vulns_txt.append(vuln_txt_temp)
# for element in list_temp_vulns_smt:
#     print(element)
# for el in list_temp_vulns_txt:
#     print(el)
#Générer les autres vulns : deux propriété et plus
k=len(list_properties)+1
l=list()
while k<len(list_combination):
    z=0
    list_tuple = list()
    while z<len(list_combination[k]):
        list_tuple.append(list_combination[k][z])
        z=z+1
    #print("la list de la combinaison est:"+ str(list_tuple))
    l=list_properties+list_tuple
    #print("la " + str(k)+" liste des combinaison: "+ str(l))
    coucou = list()
    hello = list()
    joujou =list()
    list_built_vulns=list()
    list_fils_vuls=list()
    vulns_built=""
    vuln_txt=""
    j=0
    i=0
    coucou=list()
    joujou=list()
    hello=list()
    while i<len(l):
        j=0
        while j<len(l):
            if j!= i and l[i]==l[j]:
                coucou.append("(not "+str(l[i]) + ")")
                joujou.append("¬" + str(l[i]))
                break
            if j == len(l)-1:
                hello.append(l[i])
            j=j+1
        i=i+1
    list_built_vulns=list(set(coucou))+list(set(hello))
    list_fils_vuls=list(set(joujou))+list(set(hello))
    m=0
    while m<len(list_built_vulns)-1:
        vulns_built=vulns_built+list_built_vulns[m] + " "
        vuln_txt=vuln_txt+list_fils_vuls[m] + " " + "∧" + " "
        m=m+1
    vulns_built = vulns_built + list_built_vulns[m]
    vuln_txt = vuln_txt + list_fils_vuls[m]
    #print(vulns_built)
    #print(vuln_txt)
    list_partial_built_vulns_smt.append(vulns_built)
    list_partial_built_vulns_txt.append(vuln_txt)
    k=k+1
#for el in list_partial_built_vulns_txt:
#    print(el)
list_generated_vuln_smt=list()
list_generated_vuln_txt=list
list_generated_vuln_smt=list_temp_vulns_smt + list_partial_built_vulns_smt
list_generated_vuln_txt=list_temp_vulns_txt + list_partial_built_vulns_txt
list_generated_vuln_smt.sort()
list_generated_vuln_txt.sort()
#print(list_generated_vuln_txt)
str_start = "(not(and "
str_end = " ))"
str_file_smt =""
str_print_to_file=""
Nbre_vulns_to_gerate=-1
# print(type(Nbre_vulns_to_gerate))
# print(type(len(list_generated_vuln_txt)))
l=0
while Nbre_vulns_to_gerate < 0 or Nbre_vulns_to_gerate > len(list_generated_vuln_txt):
    Nbre_vulns_to_gerate=input("Donner le nombre de vulnérabilités à générer (Il doit être inférieur à:"+ str(len(list_generated_vuln_txt))+"):")
    Nbre_vulns_to_gerate=int(Nbre_vulns_to_gerate)
    l=l+1
i=0
while i<len(list_generated_vuln_txt) and i < Nbre_vulns_to_gerate:
    str_print_to_file = "V"+str(i+1)+"= " + str(list_generated_vuln_txt[i])
    print(str_print_to_file)
    file_object = open(file_to_write_vulns, 'a', encoding='utf8')
    file_object.write(str_print_to_file+"\n")
    file_object.close()
    print("v"+str(i+1)+"= "+list_generated_vuln_smt[i])
    str_file_smt= str_file_smt+str_start+str(list_generated_vuln_smt[i])+str_end
    print("########################################")
    i = i+1
print("(and "+str_file_smt+")")





