#importing random genarator

import random

#create veriables

rand1=0
rand2=0
result=0
Uanswer=0

#esay level.
def easy(name,NoQue):
    count = 0
    correctAnswers = []
    Uanswers = []
    print("-------------------------------------------------")
    for i in range(1,NoQue+1):
        rand1=random.randrange(10)
        rand2=random.randrange(10)
        print(rand1,"+",rand2,"=","?")
        correctAnswers.append(rand1+rand2)
        urAnswer = int(input())
        Uanswers.append(urAnswer)
    print("-------------------------------------------------")
    for i in range(NoQue):
        if  correctAnswers[i]==Uanswers[i]:
            print("[Answer is-", correctAnswers[i],"]",end=" ")
            print("[Correct]")
            count=count+1
        else:
            print("[Answer is-", correctAnswers[i],"]",end=" ")
            print("[Incorrect]")
    percentage=(count/NoQue)*100
    print("-------------------------------------------------")
    print("Player name is-",name)
    print("Number of Question-",NoQue)
    print("Number of Correct Answer-",count)
    print("Percentage of Questions-",percentage)
    print("You played the game with easy.")
    print("-------------------------------------------------")
    

    import mysql.connector

    # open database connectition with a dictionery.
    conDict = {'host': 'localhost', 'database': 'game123', 'user': 'root','password': ''}

    db = mysql.connector.connect(**conDict)

    # prepare a cursor obeject using cursor() method
    cursor = db.cursor()

   #execute sql query using execute() method.
    mySQLText="INSERT INTO game123table (Name,Correct,Total_Questions,Percentage) VALUES (%s,%s,%s,%s)"
    myValues=((name,count,NoQue,percentage))
    cursor.execute(mySQLText,myValues)

    #commit the change.
    db.commit()

    print(cursor.rowcount,"Record Added To Database")
    print("-------------------------------------------------")

    #discount from sever
    db.close()
        


  
    
    

    
    
