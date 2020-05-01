import os
import time
import pyodbc
import sys

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Users\Gebruiker\Documents\Python\TestDB.accdb;')
cursor = conn.cursor()


def Insert(Table,Collum,Value):
    #{Table} = "dddkd"

    #cursor.execute("INSERT INTO %s (Collum) VALUES(?)",(Shepherd,'djkdfhg'))        
    #cursor.execute("INSERT INTO {0}(Table)VALUES({1});".format(Table,Value))   
    
    sql = '''INSERT INTO %s (%s) VALUES(%s)''' %(Table,Collum,Value)
    print("printing", sql)
    cursor.execute(sql)


    #cursor.execute("INSERT INTO names_table (First_Name,Age) VALUES(?, ?)",(number, NewCar))              
    conn.commit()

#Make array with some standard cars in it
arrayCars = ['merc', 'volvo', 'bmw']

#Get car from array
def getCar(LineRequest):
    cls()
    CurrentCar = arrayCars[LineRequest]
    print(CurrentCar)
    EnterCommand()
    
#Write car to array
def setCar(LineRequest, NewCar):
    cls()
    number = 234
    arrayCars[LineRequest] = NewCar
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
    for (index,item) in enumerate (arrayCars, start = 0):
        print(index,':',item)

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
        if CheckLine(LineRequest, len(arrayCars)):
            getCar(int(LineRequest))
        else:
            TryAgain()
    if CheckCommand(UserCommand,'e'):
        LineRequest = input('enter line to edit:')
        if CheckLine(LineRequest, len(arrayCars)):
            NewCar = input('enter new Car brand:')
            setCar(int(LineRequest),NewCar)
        else:
            TryAgain()
    if CheckCommand(UserCommand,'l'):
            ShowList()
    else:
        TryAgain()
        
#Main    
EnterCommand()

