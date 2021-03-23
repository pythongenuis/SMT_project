file_new_state=input("Donner le noms du fichier des vulnérabilités:")
f = open(file_new_state, "r", encoding='utf8')
for x in f:
    if x.startswith():
        newstate=x




l=""
ls=""
list_read_vuln_from_file_smt=list()
list_read_vuln_from_file_txt=list()
for x in f:
    #list_read_vuln_from_file_txt.append(x)
    vuln=x
    vu=vuln.replace(" ", "")
    list_read_vuln_from_file_txt.append(vuln)
    ls = vu[3:-1]
    list_prop_vulns = ls.split("∧")
    str_start = "(not "
    str_end = ") "
    str_temp_second = ""
    str_temp_env = ""
    str_vulns_indvi = ""
    i = 0
    while i < len (list_prop_vulns):
        if str (list_prop_vulns[i]).startswith ("¬"):
            str_temp_env = str (list_prop_vulns[i])[1:3]
            str_temp_second = "(not " + str_temp_env + str_end
        else:
            str_temp_second =str(list_prop_vulns[i])+ " "
        str_vulns_indvi = str_vulns_indvi + str_temp_second
        i=i+1
    #print(str_vulns_indvi)
    list_read_vuln_from_file_smt.append(str_vulns_indvi)
    #print("++++++++++++")



print("#############################################################################")
print("Les vulnérabilités sous le format SMT:\n")
q=0
str_smt_file_input="(and "
for e in list_read_vuln_from_file_smt:
    q=q+1
    print("v"+str(q) +"= "+ "(and "+e+ ")")
    str_smt_file_input=str_smt_file_input+"(not(and "+e+ "))"
print("#############################################################################")
print("Les vulnérabilités sous le format TXT:\n")
str_smt_file_input=str_smt_file_input+")"

for e in list_read_vuln_from_file_txt:
    print(e)
print("#############################################################################")
print("Le format SMT pour le fichier SMT")
print(str_smt_file_input)





