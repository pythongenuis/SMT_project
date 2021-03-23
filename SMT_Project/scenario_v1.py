import itertools
import os
#file_vuln=input("Donner le noms du fichier des vulnérabilités:")
Nbre_properties = input("Donnez le nombre de propriété du composant:")
Nbre_properties = int(Nbre_properties)
file_vuln="v.txt"
file_new_state="n.txt"
file_security_function="f.txt"
f = open(file_vuln, "r", encoding='utf8')
l=""
ls=""
list_read_vuln_from_file_smt=list()
list_read_vuln_from_file_txt=list()
for x in f:
    vuln=x
    vu=vuln.replace(" ", "")
    list_read_vuln_from_file_txt.append(vuln)
    ls = vu[vu.rfind('=')+1:-1]
    list_prop_vulns = ls.split("∧")
    str_start = "(not "
    str_end = ") "
    str_temp_second = ""
    str_temp_env = ""
    str_vulns_indvi = ""
    i = 0
    while i < len(list_prop_vulns):
        if str (list_prop_vulns[i]).startswith("¬"):
            str_temp_env = str(list_prop_vulns[i])[1:]
            str_temp_second = "(not " + str_temp_env + str_end
        else:
            str_temp_second =str(list_prop_vulns[i])+ " "
        str_vulns_indvi = str_vulns_indvi + str_temp_second
        i=i+1
    #print(str_vulns_indvi)
    list_read_vuln_from_file_smt.append(str_vulns_indvi)
    #print("++++++++++++")
print("#############################################################################################################\n")
print("La liste des vulnérabilités sous le format SMT:\n")
f.close()
q=0
str_smt_file_input="(and "
for e in list_read_vuln_from_file_smt:
    q=q+1
    print
    print("v"+str(q) +"= "+ "(and "+e+ ")")
    str_smt_file_input=str_smt_file_input+"(not(and "+e+ "))"
print("#############################################################################################################\n")
print("La liste des vulnérabilités sous le format TXT:\n")
str_smt_file_input=str_smt_file_input+")"
for e in list_read_vuln_from_file_txt:
    print(e)
print("#############################################################################################################\n")
print("Le format SMT pour toutes les vulnérabilités")
print(str_smt_file_input)
# Inject one state:
print("#############################################################################################################\n")

print("Le nouveau état:")
l=""
ls=""
list_read_vuln_from_file_smt=list()
list_read_vuln_from_file_txt=list()
file = open(file_new_state, "r", encoding='utf8')
new_state=file.read()
file.close()
print(new_state)
cc=new_state.replace(" ", "")
ss = cc[cc.rfind('=')+1 :-1]
list_prop_new_state = ss.split("∧")

str_new_state_indvi=""
str_temp_second_state=""
str_temp_new_state=""
list_new_state=list()
i=0
while i < len(list_prop_new_state):

    if str(list_prop_new_state[i]).startswith("¬"):
        str_temp_new_state = str(list_prop_new_state[i])[1:]

        str_temp_second_state = "(not " + str_temp_new_state  + str_end
        list_new_state.append("not " +str(str_temp_new_state))
    else:
        list_new_state.append(list_prop_new_state[i])
        str_temp_second_state = str (list_prop_new_state[i]) + " "
    str_new_state_indvi = str_new_state_indvi + str_temp_second_state
    i = i + 1
#print("VOILA LES PORPRITE DU NOUVEAU ETAT: "+ str(list_new_state))
new_state_file_smt = "( and "+str_new_state_indvi+")"
#print(new_state_file_smt)

#file to test the new state
str_to_test_new_state = "( and "+str_smt_file_input + new_state_file_smt+ ")"
print("#############################################################################################################\n")
print("Le fichier à du vulnérabilités et du nouveau état après la migration à injecter dans le CVC4:")
print(str_to_test_new_state)

#read security functions
file_functions = open(file_security_function, "r", encoding='utf8')
list_function=list()
list_read_functions_from_file_txt=list()
for line in file_functions:
    function=line
    ff=function.replace(" ", "")
    #ff = function.replace ("\n", "")
    list_read_functions_from_file_txt.append(line.replace(" ", ""))
    function = ff[ff.rfind('=')+1:-1]
    list_function.append(function)
    str_start = "(not "
    str_end = ") "
    str_temp_function = ""
    list_functions_smt_format=list()

    i = 0
    while i <len(list_function):
        if str (list_function[i]).startswith("¬"):
            str_temp_function = str(list_function[i])[1:]
            str_temp_second = "(not " + str_temp_function + str_end
        else:
            str_temp_second =str(list_function[i])+ " "
        list_functions_smt_format.append(str_temp_second)
        i=i+1
print("#############################################################################################################\n")
print("La liste des fonctions de sécurité :")
print(list_read_functions_from_file_txt)
# test the new state after the migration
print("#############################################################################################################\n")
print("Tester le nouveau état après la migration: ")
mon_fichier = open("fichier.smt", "w")
mon_fichier.write("(set-logic ALL)\n")
mon_fichier.write("(set-option :produce-models true)\n")
i=0
while i < Nbre_properties:
    mon_fichier.write("(declare-const p"+ str(i+1)+ " Bool)\n")
    i = i+1
mon_fichier.write("(assert  " + str_to_test_new_state +" )\n")
mon_fichier.write("(check-sat)\n")
mon_fichier.write("(get-model)\n")
mon_fichier.close()
print("#############################################################################################################\n")
print("Le fichier SMT est créé dans le répertoire actuel sous le nom fichier.smt")
print("#############################################################################################################\n")
print("Début du test du nouveau état")

os.system('cvc4 --lang smt fichier.smt 1> get_result.txt 2>>get_result.txt')
file_result = open("get_result.txt", "r", encoding='utf8')
for line in file_result:
    if str(line) == "sat":
        print(
            "#############################################################################################################\n")
        print("Résultat: le nouveau état est sécurisé.")
        mon_fichier.close()
    else:
        print(
            "#############################################################################################################\n")
        print("Le nouveau état est vulnérable.")
        list_security_functions = list(list_functions_smt_format)
        new_state = list(list_new_state)
        list_not_existant_element = list()
        for el in list_security_functions:
            if el not in new_state:
                list_not_existant_element.append(el)
        # print(list_not_existant_element)
        list_strip_not_existant_element = list()
        for e in list_not_existant_element:
            list_strip_not_existant_element.append(e.strip("not "))
        # print(list_strip_not_existant_element)
        for L in range(1, len(list_strip_not_existant_element) + 1):
            for subset in itertools.combinations(list_strip_not_existant_element, L):
                print("Voilà le subset: " + str(subset))
                print("Tester les fonction de sécurités:\n")
                for ele in subset:
                    print("not " + str(ele))
                #print("#####################################################################")
                i = 0
                j = 0
                new_state_provisoire = list(new_state)
                print("la "+str(i+1)+" itération pour tester les fonctions de sécurité: ")
                while i < len(subset):
                    j = 0
                    while j < len(new_state_provisoire):
                        if subset[i] == new_state_provisoire[j]:
                            new_state_provisoire[j] = "not " + str(new_state_provisoire[j])
                        j = j + 1
                    i = i + 1
                print("Voilà la nouvelle liste à tester:" + str(new_state_provisoire))
                str_new_test = ""
                for element in new_state_provisoire:
                    if element.startswith("not"):
                        element = "(" + element + ") "
                    else:
                        element = str(element) + " "
                    str_new_test = str_new_test + element
                str_new_test = "(and " + str_new_test + ")"
                print("La chaine SMT to : " + str_new_test)
                str_file_smt_input_with_new_smt = ""
                str_file_smt_input_with_new_smt = "(and" + str_smt_file_input + str_new_test + ")"
                print ("La chaine à injecter dans le fichier est: " + str_file_smt_input_with_new_smt + "pour le subset: " + str(subset))

                mon_fichier = open("fichier.smt", "w")
                mon_fichier.write("(set-logic ALL)\n")
                mon_fichier.write("(set-option :produce-models true)\n")
                i = 0
                while i < Nbre_properties:
                    mon_fichier.write("(declare-const p" + str (i + 1) + " Bool)\n")
                    i = i + 1
                mon_fichier.write("(assert  " + str_to_test_new_state + " )\n")
                mon_fichier.write("(check-sat)\n")
                mon_fichier.write("(get-model)\n")
                mon_fichier.close()
                print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print ("Le sésultat du SMT solver-cvc4:")
                os.system ('cvc4 --lang smt fichier.smt 1> get_result.txt 2>>get_result.txt')
                file_result = open("get_result.txt", "r", encoding='utf8')
                for line in file_result:
                    if str(line) == "sat":
                        print("Pour sécuriser le composant en question appliquer les fonctions de sécurité suivantes:")
                        for el in subset:
                            print("not " + str(el))
                print("Fin de la" + str(i+1) + "itération")
                mon_fichier.close()






