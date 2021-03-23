import itertools
rest_security_functions=list()
unsecure_state=list()
rest_security_functions=["not p1", "not p2"]
unsecure_state=["p1", "p2", "p3"]



not_rest_security_functions=list()
i=0
while i<len(rest_security_functions):
    not_rest_security_functions.append(rest_security_functions[i].strip('not').strip())
    i=i+1

#Generate combinations
combination=list()
for L in range(0, len(not_rest_security_functions)+1):
    for subset in itertools.combinations(not_rest_security_functions, L):
        combination.append(subset)

i=1


while i<len(combination):
    #print("L'itération est :" + str(i))
    #print(combination[i])

    j = 0
    t = list()
    #print ("la tableau n°" + str (j + 1))
    while j < len(combination[i]):
        #print("L'élémnt à ajouter  au tableau :")
        #print(combination[i][j])
        t.append(combination[i][j])
        j = j+1
    print("le tableau N°" + str(i))
    print(t)


    # MON Algo commence ici
    print("Traitement pour le tableau " + str(i))
    k=0
    provisoire = [el for el in unsecure_state]
    #provisoire = unsecure_state
    while k<len(t):
        m=0
        while m<len(provisoire):
            if t[k] == provisoire[m]:
                provisoire[m] = "not " + provisoire[m]
                break
            m = m+1
        if provisoire != unsecure_state:
            print(provisoire)
        k = k+1
    #unsecure_state = hello
    # print("l'insecure state est:")
    # print(unsecure_state)
    # print("voila hello function")
    # print(hello)

    print ("++++++++++++++++++++++++++++++++++++++++++++++++")

    i = i+1












































