
#importing
import Customgame
import Quickgame
import Gameresult

#variables

number=0

#display
print("+++---xxx+++---xxx+++---xxx+++---xxx")
print(".....Welcome to  the Calcu Champ.....")
print(".....Production of Game Zombia......")
print("+++---xxx+++---xxx+++---xxx+++---xxx")
print("_________________________________")
print("_________________________________")
print("Type 1 to go to Quick Game.")
print("Type 2 to go to Custom Game.")
print("Type 3 to go to Past Game Result.")
print("Type 4 to Exit the Game.")
print("_________________________________")

number=int(input("Type your choice-"))
print("---------------------------------")

if (number==1):
    Quickgame.Quickgame()
elif(number==2):
    Customgame.Customgame()
elif(number==3):
    Gameresult.Gameresult()
elif(number==4):
    print("You Exit the Game")



