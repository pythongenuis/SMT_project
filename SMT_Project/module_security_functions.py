
import time
rr=input("Tapez A pour commencer:\n")
if rr== "A":
    n = 20
    m = (2 * n) - 2
    for i in range(0, n):
        for j in range(0, m):
            print(end=" ")
        m = m - 1  # decrementing m after each loop
        for j in range(0, i + 1):
            # printing full Triangle pyramid using stars
            print("* ", end=' ')
        print(" ")
    print("Hello GHITA:")
    s="oui"
    r=input("Si tu souhaites connaitre ton avenir tapes oui: \n")
    if r == "oui":
        print("Tu crois vraiment que je connais ton avenir?????!!!!!!!!\n")
        time.sleep(3)
        l=input("Si tu crois vraiment que je connais ton avenir tapes OUI en majuscule.\n")
        m="oui"
        while l!= m.upper():
            l=input("J'ai dit oui en majuscule!!!!!!!!!!!!!!!\n")
        print(" Les grandes lignes s'afficheront dans 30 secondes.\n ")
        i=30
        while i>=0:
            print("Votre avenir sera affiché dans :"+ str(i) + " S.")
            time.sleep(1)
            i=i-1
        print("Alors le voilà ton avenir:\n")
        print("****************AMOUR****************\n")
        time.sleep(3)

        # printing full Triangle pyramid using stars
        size = 7
        m = (2 * size) - 2
        for i in range (0, size):
            for j in range (0, m):
                print (end=" ")
            # decrementing m after each loop
            m = m - 1
            for j in range (0, i + 1):
                print ("* ", end=' ')
            print (" ")
        print ("****************ARGENT****************\n")
        time.sleep(3)

        # printing full Triangle pyramid using stars
        size = 7
        m = (2 * size) - 2
        for i in range (0, size):
            for j in range (0, m):
                print (end=" ")
            # decrementing m after each loop
            m = m - 1
            for j in range (0, i + 1):
                print ("* ", end=' ')
            print (" ")
        print ("****************SANTE:****************\n")
        time.sleep(3)

        # printing full Triangle pyramid using stars
        size = 7
        m = (2 * size) - 2
        for i in range (0, size):
            for j in range (0, m):
                print (end=" ")
            # decrementing m after each loop
            m = m - 1
            for j in range (0, i + 1):
                print ("* ", end=' ')
            print (" ")
        time.sleep(1)
        print("----------------------------------------------------------------")
        print ("\n")
        print("Il est vraiment chiffré ton avenir")
        print ("\n")
        time.sleep (1)
        print ("\n")
        print ("---------------------------------------------------------------")
        print ("\n")
        print("Dès que nous aurons plus d'information, nous vous recontacterons.")
        time.sleep (1)
        print ("\n")
        print ("----------------------------------------------------------------")
        print ("\n")
        print("GOOD BYE.")



