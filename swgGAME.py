# ---------------------------snake water gun game-------------------------------
i=0
while i <10: 
    import random


    def gamewin(player,comp):
        if player==comp:
            return None
        
        elif comp=="snake":
            if player=="w":
                return False
            if player=="g":
                return True
        
        elif comp=="water":
            if player=="g":
                return False
            if player=="s":
                return True

        elif comp=="gun":
            if player=="s":
                return False
            if player=="w":
                return True
        

    print("Computers Turn...Computer have choosen!")
    rand=random.randint(1,3)
    if rand==1:
        comp="snake"
    elif rand==2:
        comp="water"
    else:
        comp="gun"

    player=input("Your Turn! Choose from these three: Snake(s), Water(w), Gun(g) --> ")

    print(f"You have Choosen {player}\n")
    print(f"Computer have Choosen {comp}\n")

    a=gamewin(player,comp)

    if a==True:
        print("YOU WON THE GAME!!\n***************************")
    if a==False:
        print("YOU LOST..,\nBETTER LUCK NEXT TIME :)\n***************************")
    if a==None:
        print("THIS IS A TIE!!\n***************************")

    i+=1