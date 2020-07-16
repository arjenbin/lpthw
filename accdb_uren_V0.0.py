import os
import time
import pyodbc
import sys
import datetime



laptopdbpath ='D:/Users/Gebruiker/Documents/Python/TestDB.accdb'
pcdbpath = 'C:/Users/Gebruiker/lpthw/TestDB.accdb'


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:/Users/Gebruiker/Documents/Python/Erp4.accdb')
cursor = conn.cursor()


def Insert(Table,Tijdnummer,PersoneelNaam,Date,Projectnummer,Activiteitnummer,Uren,Opmerking):
    
    currentTime = datetime.datetime.now()

    sql = r"""insert into TijdVerantwoording 
    (TijdNum, DateChanged, PersoneelNum, Datum, ProjectNum, 
    ActiviteitNum, Duur, Opmerking) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

    cursor.execute(sql, 
        Tijdnummer, currentTime, PersoneelNaam,Date,Projectnummer, 
        Activiteitnummer, Uren, Opmerking)
    conn.commit()

def deleteCar(LineRequest,Table,Collum):
	sql = ('''delete from %s where (%s) = (%s)''')%(Table,Collum,LineRequest)
	cursor.execute(sql)
	conn.commit()

def deleteName(LineRequest,Table,Collum):
	sql = ('''delete from %s where (%s) in ('%s')''')%(Table,Collum,LineRequest)
	cursor.execute(sql)
	conn.commit()


#Get car from array
def getCar(LineRequest):
    cls()
    CurrentCar = arrayCars[LineRequest]
    print(CurrentCar)
    EnterCommand()
    
#Write car to array
def setCar(LineRequest, NewCar):
    cls()
    #number = 234
    #rrayCars[LineRequest] = NewCar
    Insert(Table = 'names_table', Collum = 'First_Name', Value = NewCar)


    EnterCommand()
    
#Check if user input was correct    
def CheckCommand(Command,Check):
    return Command.lower() == Check.lower()

#Check if user input was correct    
def CheckLine(Command,Check):
    return int(Command) < Check

#Print total Array
def ShowList(Table,Collum):
    cls()

    sql = ('''select * from %s where %s = True''')%(Table,Collum)
    print(sql)
    #cursor.execute('select * from names_table')
    cursor.execute(sql)
    for row in cursor.fetchall():
        print (row.ProjectNummer,row.Omschrijving)    
    EnterCommand()

#Try again message
def TryAgain():
    print("Try again")
    time.sleep(0.5)
    cls()
    EnterCommand() 

def cls():
    os.system('cls')
#Get user command    
def EnterCommand():
    #-----Main screen-----#
    UserCommand = input(
    '\n'
    '-----------------\n'
    'Uren toevoegen = U\n'
    'Edit Car = E\n'
    'Delete Name = DN\n'
    'Delete Line = DL\n'
    'Show List = L\n')
    
    #-----Wait for user command-----#
    #TijdNum
    #DateChanged 7-1-2020 16:00:33
    #PersoneelNum
    #Datum
    #ProjectNum
    #ActiviteitNum
    #Duur
    #Opmerking

    if CheckCommand(UserCommand,'u'):
        tijdnummer = input('Voer tijdnummer (urensoort) in:')
        personeelNaam = input('Voer naam in(nummernu):')
        date = input('Voer datum in (7-1-2020):')
        projectnummer = input('Voer Projectnummer in:')
        activiteitnum = input('Voer Activiteitnummer in:')
        duur = input('Voer aantal uren in:')
        opmerking = input('Wat heb je gedaan?')

        Insert(Table = 'TijdVerantwoording',
               Tijdnummer = tijdnummer,
               PersoneelNaam = personeelNaam,
               Date = date,
               Projectnummer = projectnummer,
               Activiteitnummer = activiteitnum, 
               Uren = duur,
               Opmerking = opmerking,)


    if CheckCommand(UserCommand,'e'):
        LineRequest = input('enter line to edit:')
        if CheckLine(LineRequest,100):
            NewCar = input('enter new Car brand:')
            setCar(int(LineRequest),NewCar)
        else:
            TryAgain()
    if CheckCommand(UserCommand,'l'):
            ShowList(Table = 'Projecten',Collum ='Actief')
    if CheckCommand(UserCommand,'dl'):
        LineRequest = input('enter line to delete:')
        if CheckLine(LineRequest,100):
            deleteCar(LineRequest,Table='names_table',Collum ='Id')
        else:
            TryAgain()
    if CheckCommand(UserCommand,'dn'):
        LineRequest = input('enter name to delete:')
        deleteName(LineRequest,Table='names_table',Collum ='First_Name')
    else:
        TryAgain()

#Main    
EnterCommand()

