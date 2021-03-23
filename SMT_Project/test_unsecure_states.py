import itertools
#list_security_functions=['not p1', 'not p2']
#new_state=['p1', 'p2', 'p3',"p4"]

list_security_functions=list(list_functions_smt_format)
new_state=list(list_new_state)

list_not_existant_element = list()
for el in list_security_functions:
    if el not in new_state:
        list_not_existant_element.append(el)
#print(list_not_existant_element)
list_strip_not_existant_element=list()
for e in list_not_existant_element:
    list_strip_not_existant_element.append(e.strip("not "))
#print(list_strip_not_existant_element)
#print("heloooooooooooooooooooooo")

for L in range(1, len(list_strip_not_existant_element)+1):
    for subset in itertools.combinations(list_strip_not_existant_element, L):
        print("Voil le subset: " + str(subset))
        print("#####################################################################")
        i=0
        j=0
        new_state_provisoire=list(new_state)
        while i < len(subset):
            j=0
            while j < len(new_state_provisoire):
                if subset[i] == new_state_provisoire[j]:
                    new_state_provisoire[j] = "not " + str(new_state_provisoire[j])
                j=j+1
            i = i + 1

        print("Voila la liste a tester:" + str(new_state_provisoire))
        str_new_test = ""
        for element in new_state_provisoire:
            if element.startswith("not"):
                element = "(" +element + ") "
            else:
                element = str(element) + " "
            str_new_test = str_new_test+element
        str_new_test = "(and " + str_new_test+ ")"
        print("La chaine qui devrai alimenter le cvc4: "+str_new_test)
        str_file_smt_input_with_new_smt = ""
        str_file_smt_input_with_new_smt = "(and"+ str_smt_file_input +str_new_test+")"
        print("La chaine à injecter dans le fichier est"+ str_file_smt_input_with_new_smt+ "pour le subset "+str(subset))

        mon_fichier = open("fichier.smt", "w")
        mon_fichier.write("(set-logic ALL)\n")
        mon_fichier.write("(set-option :produce-models true)\n")
        i = 0
        while i < Nbre_properties:
            mon_fichier.write("(declare-const p" + str(i + 1) + " Bool)\n")
            i = i + 1
        mon_fichier.write("(assert  " + str_to_test_new_state + " )\n")
        mon_fichier.write("(check-sat)\n")
        mon_fichier.write("(get-model)\n")
        mon_fichier.close()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Le sésultat du SMT solver-cvc4:")
        os.system('cvc4 --lang smt fichier.smt 1> get_result.txt 2>>get_result.txt')
        file_result = open("get_result.txt", "r", encoding='utf8')
        for line in file_result:
            if str (line) == "sat":
                print("Pour sécuriser le composant en question appliquer les fonctions de sécurité suivantes:")
                for el in subset:
                    print("not " + str(el))
        mon_fichier.close()






