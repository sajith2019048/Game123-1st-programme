def Gameresult():
    import mysql.connector

    # open database connectition with a dictionery.
    conDict = {'host': 'localhost', 'database': 'game123', 'user': 'root', 'password': ''}

    db = mysql.connector.connect(**conDict)

    # prepare a cursor obeject using cursor() method
    cursor = db.cursor()
    #execute sql query using execute() method.
    cursor.execute("SELECT * FROM game123table")

    #fetch result using fetchall() method.
    data=cursor.fetchall()
    print("_____________________________________________________")
    print(":    Name     : Correct :Total Qestions :Percentage :")
    print("_____________________________________________________")
    
    for item in data:
        print(":",item[0]," "*(10-len(item[0])),":",item[1]," "*(6-len(str(item[1]))),":",item[2]," "*(12-len(str(item[2]))),":",item[3]," "*(8-len(str(item[3]))),":")

    #discount from sever
    db.close()



    


    
