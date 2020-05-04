import os
import time
import pyodbc
import sys

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Users\Gebruiker\Documents\Python\TestDB.accdb;')
cursor = conn.cursor()


def Insert(Table,Collum,Value,Id):
    
    sql = ('''INSERT INTO %s (%s)
    	      VALUES(?)
    	      ''')%(Table,Collum)

    cursor.execute(sql,Value)             
    conn.commit()


def deleteRow(Id):
	sql = ('''delete from names_table where Id = ?''','Id')
	print(sql)
	cursor.execute(sql,Id)
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
    'Delete Car = D\n'
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
    if CheckCommand(UserCommand,'d'):
        LineRequest = input('enter line request:')
        if CheckLine(LineRequest,100):
            deleteRow(int(LineRequest))
        else:
            TryAgain()
    if CheckCommand(UserCommand,'l'):
            ShowList()
    else:
        TryAgain()
        
#Main    
EnterCommand()
