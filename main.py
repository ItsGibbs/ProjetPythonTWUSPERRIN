from complement import complement
from mdl import mdl
from sujet import sujet
from verb import verb
from bon import bon
from mauvais import mauvais
from ennemy import Liste, Bryan, Pierre_Menhir, Eren_Yeager, Michel, Tiger_King, Elongated_Musketeer
import random
import time

dmg = 0

tour = 1

  # -------------------------------------- code des personnages ----------------------------------------
print("Bienvenue dans le jeu \n\n")

print("Pour commencer, veuillez chacun votre tour choisir un personnage :\n")
for i in range (6):
        print(Liste[i],"\n")

print("Joueur 1 :")
J1 = input()
i=0
while i!=8:
    if J1 != Liste[i]:
            
        i+=1
        if i == 5:
            print("vous vous etes trompé, veuillez rechoisir :")
            i=0
            J1 = input()
    else:
        i=8
if J1 == "Bryan" :
    J1weakness = Bryan.weakness
    Liste.remove(Liste[int(0)])
if J1 == "Pierre_Menhir":
    J1weakness = Pierre_Menhir.weakness
    Liste.remove(Liste[int(1)])
if J1 == "Eren_Yeager":
    J1weakness = Eren_Yeager.weakness
    Liste.remove(Liste[int(2)])
if J1 == "Michel":
    J1weakness = Michel.weakness
    Liste.remove(Liste[int(3)])
if J1 == "Tiger_King":
    J1weakness = Tiger_King.weakness
    Liste.remove(Liste[int(4)])
if J1 == "Elongated_Musketeer":
    J1weakness = Elongated_Musketeer
    Liste.remove(Liste[int(5)])
print("vous avez choisi :",J1)
print("\n\n")
time.sleep(2.0)
print("Maintenant, au tour du second joueur de choisir un personnage :\n")
for i in range (5):
    print(Liste[i],"\n")

print("Joueur 2 :")
J2 = input()
i=0
while i!=8:
    if J2 != Liste[i]:       
        i+=1
        if i == 4:
            print("vous vous etes trompé, veuillez rechoisir :")
            i=0
            J2 = input()
    else:
        i=8

if J2 == "Bryan" :
    J2weakness = Bryan.weakness
if J2 == "Pierre_Menhir":
    J2weakness = Pierre_Menhir.weakness
if J2 == "Eren_Yeager":
    J2weakness = Eren_Yeager.weakness
if J2 == "Michel":
    J2weakness = Michel.weakness
if J2 == "Tiger_King":
    J2weakness = Tiger_King.weakness
if J2 == "Elongated_Musketeer":
    J2weakness = Elongated_Musketeer
print("vous avez choisi :",J2)
time.sleep(1.0)

print("La partie peut commencer !\n\n")

time.sleep(1.0)
vieJ1 = 20
vieJ2 = 20
while vieJ1 > 0 or vieJ2 > 0:
    choix1 = random.choice(sujet)
    choix2 = random.choice(sujet)
    choix3 = random.choice(verb)
    choix4 = random.choice(verb)
    choix5 = random.choice(complement)
    choix6 = random.choice(complement)
    choix7 = random.choice(mdl)
    choix8 = random.choice(mdl)
    choix9 = random.choice(complement)
    choix10 = random.choice(complement)
    array = [choix1, choix2, choix3, choix4, choix5, choix6, choix7, choix8, choix9, choix10]


  
  






    # -------------------------------------- Code du jeu --------------------------------------------
    print("tour:",tour)
    tour = tour + 1
    print("choisir chacun leur tours un chiffre correspondant à un mot/groupe de mot pour former une phrase :")
    count = count1 = count2 = count3 = count4 = count5 = count6 = count7 = count8 = count9 = count10 = 0

    while count < 10:
        print(count, ":", array[count])
        count = count + 1
        
    resJ1 = []
    resJ2 = [] 

    input1 = input()

    if int(input1) < 11:
        # faire en sorte de retourner le resultat et de l'identifier par rapport a la liste de mot de sujet.
        resJ1.append(array[int(input1)])
        print("Voici votre phrase actuelle :")
        for i in range (1):
            print(resJ1[i])
        array.remove(array[int(input1)])
        print()
        print("Maintenant au tour du second joueur de choisir un mot/groupe de mot :")
        while count1 < 9:
            print(count1, ":", array[count1])
            count1 = count1 + 1





    input2 = input()
    if int(input2) < 10:
        resJ2.append(array[int(input2)])
        print("Voici votre phrase actuelle :")
        for i in range (1):
            print(resJ2[i])
        array.remove(array[int(input2)])
        print()
        print("Maintenant au tour du premier joueur de choisir un mot/groupe de mot :")
        while count2 < 8:
            print(count2, ":", array[count2])
            count2 = count2 + 1



    input3 = input()
    if int(input3) < 9:
        resJ1.append(array[int(input3)])
        print("Voici votre phrase actuelle :")
        for i in range (2):
            print(resJ1[i], end=' ')
        array.remove(array[int(input3)])
        print()
        print()
        print("Maintenant au tour du second joueur de choisir un mot/groupe de mot :")
        while count3 < 7:
            print(count3, ":", array[count3])
            count3 = count3 + 1


    input4 = input()
    if int(input4) < 8:
        resJ2.append(array[int(input4)])
        print("Voici votre phrase actuelle :")
        for i in range (2):
            print(resJ2[i], end=' ')
        array.remove(array[int(input4)])
        print()
        print()
        print("Maintenant au tour du premier joueur de choisir un mot/groupe de mot :")
        while count4 < 6:
            print(count4, ":", array[count4])
            count4 = count4 + 1


    input5 = input()
    if int(input5) < 7:
        resJ1.append(array[int(input5)])
        print("Voici votre phrase actuelle :")
        for i in range (3):
            print(resJ1[i], end=' ')
        array.remove(array[int(input5)])
        print()
        print()
        print("Maintenant au tour du second joueur de choisir un mot/groupe de mot :")
        while count5 < 5:
            print(count5, ":", array[count5])
            count5= count5 + 1

    input6 = input()
    if int(input6) < 6:
        resJ2.append(array[int(input6)])
        print("Voici votre phrase actuelle :")
        for i in range (3):
            print(resJ2[i], end=' ')
        array.remove(array[int(input6)])
        print()
        print()
        print("Maintenant au tour du premier joueur de choisir un mot/groupe de mot :")
        while count6 < 4:
            print(count6, ":", array[count6])
            count6 = count6 + 1

    input7 = input()
    if int(input7) < 5:
        resJ1.append(array[int(input7)])
        print("Voici votre phrase actuelle :")
        for i in range (4):
            print(resJ1[i], end=' ')
        array.remove(array[int(input7)])
        print()
        print()
        print("Maintenant au tour du second joueur de choisir un mot/groupe de mot :")
        while count7 < 3:
            print(count7, ":", array[count7])
            count7 = count7 + 1

    input8 = input()
    if int(input8) < 4:
        resJ2.append(array[int(input8)])
        print("Voici votre phrase actuelle :")
        for i in range (4):
            print(resJ2[i], end=' ')
        array.remove(array[int(input8)])
        print()
        print()
        print("Maintenant au tour du premier joueur de choisir un mot/groupe de mot :")
        while count8 < 2:
            print(count8, ":", array[count8])
            count8 = count8 + 1

    input9 = input()
    if int(input9) < 3:
        resJ1.append(array[int(input9)])
        print("Voici votre phrase actuelle :")
        for i in range (5):
            print(resJ1[i], end=' ')
        array.remove(array[int(input9)])
        print()
        print()
        print("Maintenant au tour du second joueur de choisir un mot/groupe de mot :")
        while count9 < 1:
            print(count9, ":", array[count9])
            count9 = count9 + 1

    input10 = input()
    resJ2.append(array[int(input10)])
    print("Voici votre phrase actuelle :")
    for i in range (5):
            print(resJ2[i], end=' ')
            
    print()
    print()
    time.sleep(3.0)

    print("Place au resultat !!!\n")
    time.sleep(2.0)
    print("La phrase du premier joueur est :")
    time.sleep(2.0)
    for i in range (5):
            print(resJ1[i], end=' ')
    print()
    if resJ1[0] in sujet and resJ1[1] in verb and resJ1[2] in complement and resJ1[3] in mdl and resJ1[4] in complement:
        print("Votre phrase est bien structurée !")
        dmg = 2

    else :
        print("Vous auriez pu mieux structurer votre phrase !")
    time.sleep(1.0)
    print()
    
    # a ajouter en plus des faiblesses des personnages
    print("maintenant voyons voir les degats causée par votre phrase !")
    for i in range (5):
        if resJ1[i] in J2weakness:
            print("ouch, vous avez touché un point sensible avec une partie de votre phrase!")
            time.sleep(1.0)
            dmg = dmg + 2
        else : 
            time.sleep(1.0)
            dmg = dmg + 1
            print("une partie de votre phrase lui a fait un peu de degat")
    vieJ2 = vieJ2 - dmg
    if vieJ2 > 0:
        print("le joueur 1 a causé ", dmg," degat au joueur 2 ! Il ne lui reste plus que ", vieJ2, " point de vie !")
    else :
        print("le joueur 1 a causé ", dmg," degat au joueur 2 ! Il semblerais que le joueur 2 ne soit plus capable de se battre. Victoire au Joueur 1 !!")
        exit()
    
    time.sleep(3.0)
    dmg = 0
    for i in range (3):
        print()
    print("Maintenant, place à la phrase du second joueur :")
    time.sleep(2.0)
    for i in range (5):
            print(resJ2[i], end=' ')
    print()
    print()
    if resJ2[0] in sujet and resJ2[1] in verb and resJ2[2] in complement and resJ2[3] in mdl and resJ2[4] in complement:
        print("Votre phrase est bien structurée !")
        dmg = 2
        
    else :
        print("Vous auriez pu mieux structurer votre phrase !")
    time.sleep(1.0)
    print("maintenant voyons voir les degats causée par votre phrase !")
    for i in range (5):
        if resJ2[i] in J1weakness:
            print("ouch, vous avez touché un point sensible avec une partie de votre phrase!")
            time.sleep(1.0)
            dmg = dmg + 2
        else : 
            time.sleep(1.0)
            dmg = dmg + 1
            print("une partie de votre phrase lui a fait un peu de degat")
    vieJ1 = vieJ1 - dmg
    if vieJ1 > 0:
        print("le joueur 2 a causé ", dmg," degat au joueur 1 ! Il ne lui reste plus que ", vieJ1, " point de vie !")
    else :
        print("le joueur 2 a causé ", dmg," degat au joueur 1 ! Il semblerais que le joueur 1 ne soit plus capable de se battre. Victoire au Joueur 1 !!")
        exit()