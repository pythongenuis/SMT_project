
str_and_smt = "(and "
str_final_smt = ") "
str_start = "(not (and "
str_end = " )) "
Nbre_vulns=50

list_Nbre_properties=[50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000,
                  6000, 7000, 8000, 9000, 10000]
for ele in list_Nbre_properties:
    Nbre_properties = int(ele)
    list_properties = list()
    i = 0
    while i < Nbre_properties:
        list_properties.insert(i, "p" + str(i+1))
        i = i+1
    new_state=""
    for e in list_properties:
        new_state= new_state+ str(e) + " "
    new_state= str_and_smt + new_state + str_final_smt
    #print(new_state)
    str_add_smt = ""
    str_add_txt = ""
    list_temp_vulns_smt = list()
    list_temp_vulns_txt = list()
    i = 0
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
    final_list = list()
    z=0
    while z<Nbre_vulns:
        final_list.append(str_start + list_temp_vulns_smt[z] + str_end)
        z=z+1
    str_smt_tempo=""
    for element in final_list:
        str_smt_tempo= str_smt_tempo + str(element) + " "

    str_smt_file = "(and " + str_smt_tempo+ " " + new_state+ ")"
    mon_fichier = open(str(Nbre_properties)+"vulns_prop.smt", "w")
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
    print("Le fihcier : " +str(Nbre_properties) + "vulns_prop.smt est généré.")











