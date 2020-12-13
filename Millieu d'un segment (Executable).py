#python3
#Loïc Maurer 2nd1
jeu_lance = True
#OFF-st
print('''
    __  ____ ___               _____                                 __
   /  |/  (_) (_)__  __  __   / ___/___  ____ _____ ___  ___  ____  / /_
  / /|_/ / / / / _ \/ / / /   \__ \/ _ \/ __ `/ __ `__ \/ _ \/ __ \/ __/
 / /  / / / / /  __/ /_/ /   ___/ /  __/ /_/ / / / / / /  __/ / / / /_
/_/  /_/_/_/_/\___/\__,_/   /____/\___/\__, /_/ /_/ /_/\___/_/ /_/\__/
                                      /____/
(Loïc Maurer 2nd1)
''')

while jeu_lance:
    print('+-------------------------------------+')
    XA=float (input("Entre l'abscisse de A : "))
    YA=float (input("Entre l'ordonnée de A : "))
    print("Cordonées de A validé")
    print('+-------------------------------------+')
    print('')
    #Coordonées de A (entre)

    #Coordonées de B (entre)
    print('+-------------------------------------+')
    XB=float (input("Entre l'abscisse de B : "))
    YB=float (input("Entre l'ordonnée de B : "))
    print("Cordonées de B validé")
    print('+-------------------------------------+')

    #Calcul
    XM= (XA+XB)/2
    YM= (YA+YB)/2

    #Affichage des reponses
    print("")
    print("Abscisse de M (X) =", XM)
    print("Ordonnée de M (Y) =", YM)
    print('')