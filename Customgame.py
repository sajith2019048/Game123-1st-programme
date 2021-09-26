#Importing files
import easy
import medium
import hard

#creating veriables
NoQue=0
level=0
NoQue=0
def Customgame():
    
    #Main body of game
    while True:
        print("_________________________________________________")
        print("If you want to play easy level press 1")
        print("If you want to play medium level press 2")
        print("If you want to play hard level press 3")
        print("If you want to Exit the Game press 5")
        print("_________________________________________________")
        level=int(input("Please Enter the number (1,2,3,or 5)-"))
        print("-------------------------------------------------")
        if level==1:
            name=str(input("Enter the player name-"))
            NoQue=int(input("Enter the number of Question-"))
            easy.easy(name,NoQue)
            print("Game ends")
            print("-------------------------------------------------")
            break
        else:
            if level==2:
                name=str(input("Enter the player name-"))
                NoQue=int(input("Enter the number of Question you want answer-"))
                medium.medium(name,NoQue)
                print("Game ends")
                print("-------------------------------------------------")
                break
            else:
                if level==3:
                    name=str(input("Enter the player name-"))
                    NoQue=int(input("Enter the number of Question you want answer-"))
                    hard.hard(name,NoQue)
                    print("Game ends")
                    print("-------------------------------------------------")
                    break
                else:
                    if level==5:
                        break
                    else:
                        print("Pleace cheack your typing number,It is Invalied-")
                        print("-------------------------------------------------")
                        
        
    
    
