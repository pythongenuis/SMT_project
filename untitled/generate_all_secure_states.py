faux="false"
vrai="true"
table=list()
f = open("result.txt", "r")
for x in f:
    if faux in str (x) or  vrai in str(x):
        table.append(x)
print(table)
table2=list()
secure_state=list()
unsecure_state=list()
i=0;
s_state=""
uns_state=""
while i<len(table):
    if vrai in str(table[i]):
        secure_state.append(" p"+ str(i+1))
        unsecure_state.append ("(not p" + str (i + 1) + " )")
    else:
        secure_state.append ("(not p" + str (i + 1)+" )")
        unsecure_state.append (" p" + str (i + 1))
    i=i+1
print(secure_state)
print(unsecure_state)

