list_nbre_vulns=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000,
                  6000, 7000, 8000, 9000, 10000]



Nbre_properties=10000
list_properties = list()
list_combination=list()
list_negation_properties = list()
# Nbre_properties = input("Donner le nombre de propriétés:")
# Nbre_properties = int(Nbre_properties)
# Nbre_vulns = input("Donner le nombre de vulnérabilité:")
# Nbre_vulns = int(Nbre_vulns)
list_partial_built_vulns_smt = list()
list_partial_built_vulns_txt = list()
list_built_vulns_smt = list()
list_built_vulns_txt = list()
str_and_smt = "(and "
str_final_smt = ") "
str_start = "(not (and "
str_end = " )) "

i = 0
while i < Nbre_properties:
    list_properties.insert(i, "p" + str(i+1))
    i = i+1

new_state=""
for e in list_properties:
    new_state= new_state+ str(e) + " "
new_state= str_and_smt + new_state + str_final_smt

print(new_state)
str_add_smt = ""
str_add_txt = ""
list_temp_vulns_smt = list()
list_temp_vulns_txt = list()
i=0
while i<len(list_properties):
    list_vulns_temp_smt = list()
    str_add_smt = "(not " + str(list_properties[i]) + ")"
    vulns_built_temp = ""
    j=0
    while j < len(list_properties):
        if i != j:
            list_vulns_temp_smt.append(list_properties[j])
        j=j+1
    list_vulns_temp_smt.append(str_add_smt)
    i=i+1
    m=0
    while m<len(list_vulns_temp_smt)-1:
        vulns_built_temp = vulns_built_temp+str(list_vulns_temp_smt[m]) + " "
        m = m+1
    vulns_built_temp = vulns_built_temp + list_vulns_temp_smt[m]
    list_temp_vulns_smt.append(vulns_built_temp)
str_vulns_file_smt = ""
for element in list_temp_vulns_smt:
    print(element)
    list_temp_vulns_smt[list_temp_vulns_smt.index(element)] = str_start + str(element) + str_end
    print(element)
print("HELLLO "+str(list_temp_vulns_smt))
i=0
str_smt_tempo=""
str_smt_file=""


for el in list_nbre_vulns:
    Nbre_vulns= int(el)
    while i <Nbre_vulns:
        str_smt_tempo= str_smt_tempo + str(list_temp_vulns_smt[i])+ " "
        i=i+1
    str_smt_file = "(and " + str_smt_tempo+ " " + new_state+ ")"
    #print("la chaine smt du fichier hello " + str_smt_file)
    mon_fichier = open(str(el)+"vulns.smt", "w")
    mon_fichier.write("(set-logic ALL)\n")
    mon_fichier.write("(set-option :produce-models true)\n")
    i=0
    while i < Nbre_properties:
        mon_fichier.write("(declare-const p"+ str(i+1)+ " Bool)\n")
        i = i+1
    mon_fichier.write("(assert  " + str_smt_file +" )\n")
    mon_fichier.write("(check-sat)\n")
    #mon_fichier.write("(get-model)\n")
    mon_fichier.close()











