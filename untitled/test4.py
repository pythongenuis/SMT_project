new_state=list()
Nbrepropnewstate=input("Donnez le nombre de propriétés de l'état du système après migration:")
Nbrepropnewstate = int(Nbrepropnewstate)
i=0
while i< Nbrepropnewstate:
    if i==0:
        prop=input("Donnez  la 1 ère propriété:")
    else:
        prop=input("Donnez la " + str(i+1) +" ème propriété:")
    new_state.insert(i, prop)
    i=i+1
print(new_state)
i=0
p=""
str_new_state=""
while i<len(new_state):
    if new_state[i].startswith("not") == True:
        p="(" + new_state[i] + ")"
    else:
        p=new_state[i]

    str_new_state=str_new_state+ " " +str(p)
    i = i + 1
new_state_smt="(and  "+str_new_state + ")"
print("The new state is :"+  new_state_smt)
