import os
import time
import pyodbc
import sys

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Gebruiker\lpthw\TestDB.accdb;')
cursor = conn.cursor()


def Insert(Table,Collum,Value):
    
    sql = ('''INSERT INTO %s (%s)
    	      VALUES(?)
    	      ''')%(Table,Collum)
    
    cursor.execute(sql,Value)             
    conn.commit()


def deleteCar(LineRequest,Table,Collum):
	sql = ('''delete from %s where (%s) = (%s)''')%(Table,Collum,LineRequest)
	cursor.execute(sql)
	conn.commit()

def deleteName(LineRequest,Table,Collum):
	sql = ('''delete from names_table where First_Name="Mike"''')
	print(sql)
	time.sleep(1)
	cursor.execute('''delete from names_table where First_Name="234"''')
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
def ShowList():
    cls()
    #for (index,item) in enumerate (arrayCars, start = 0):
    #    print(index,':',item)

    cursor.execute('select * from names_table')
    for row in cursor.fetchall():
        print (row.Id,row.First_Name)    
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
    'Request Car = R\n'
    'Edit Car = E\n'
    'Show List = L\n')
    
    #-----Wait for user command-----#
    if CheckCommand(UserCommand,'r'):
        LineRequest = input('enter line request:')
        if CheckLine(LineRequest,100):
            getCar(int(LineRequest))
        else:
            TryAgain()
    if CheckCommand(UserCommand,'e'):
        LineRequest = input('enter line to edit:')
        if CheckLine(LineRequest,100):
            NewCar = input('enter new Car brand:')
            setCar(int(LineRequest),NewCar)
        else:
            TryAgain()
    if CheckCommand(UserCommand,'l'):
            ShowList()

    if CheckCommand(UserCommand,'d'):
        LineRequest = input('enter line to delete:')
        if CheckLine(LineRequest,100):
            deleteCar(LineRequest,Table='names_table',Collum ='Id')
        else:
            TryAgain()
    if CheckCommand(UserCommand,'f'):
        LineRequest = input('enter name to delete:')
        deleteName(LineRequest,Table='names_table',Collum ='First_Name')
    else:
        TryAgain()

#Main    
EnterCommand()

