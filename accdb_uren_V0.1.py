import os
import time
import pyodbc
import sys
import datetime
from tkinter import*



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
    return


def BuildUI():
    root= Tk()

    #Get pc screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    #Width and height of GUI
    uiWidth = 800
    uiHeight = 600

    sizex = uiWidth
    sizey = uiHeight

    #position of GUI on screen
    posx  = (screen_width / 2) - uiWidth / 2
    posy  = (screen_height / 2) - uiHeight / 2

    #Enter name and work description
    
    root.label=Label(root,text="Voer tijdnummer (urensoort) in:")
    root.label.pack()
    entrytimenumber = Entry(root)
    entrytimenumber.pack()

    root.label=Label(root,text="Voer personeel nummer in")
    root.label.pack()
    entrypersoneelNumber = Entry(root)
    entrypersoneelNumber.pack()

    root.label=Label(root,text="Voer datum in (d-m-yyy)")
    root.label.pack()
    entrydate = Entry(root)
    entrydate.pack()

    root.label=Label(root,text="Voer Projectnummer in")
    root.label.pack()
    entryprojectnumber = Entry(root)
    entryprojectnumber.pack()   

    root.label=Label(root,text="Enter Activity number")
    root.label.pack()
    entryactiviteitnum = Entry(root)
    entryactiviteitnum.pack()

    root.label=Label(root,text="Aantal uur")
    root.label.pack()
    entryduur = Entry(root)
    entryduur.pack()

    root.label=Label(root,text="Wat heb je gedaan?")
    root.label.pack()
    entrywerk = Entry(root)
    entrywerk.pack()


    def Enterwork():


        tijdnummer = entrytimenumber.get()
        personeelnummer = entrypersoneelNumber.get()
        datum = entrydate.get()
        projectnummer = entryprojectnumber.get()
        activiteitnum = entryactiviteitnum.get()
        duur = entryduur.get()
        werk = entrywerk.get()


        Insert(Table = 'TijdVerantwoording',
               Tijdnummer = tijdnummer,
               PersoneelNaam = personeelnummer,
               Date = datum,
               Projectnummer = projectnummer,
               Activiteitnummer = activiteitnum, 
               Uren = duur,
               Opmerking = werk,)

        
      
  
    #Insert(Table,Tijdnummer,PersoneelNaam,Date,Projectnummer,Activiteitnummer,Uren,Opmerking):

    root.Enterbutton=Button(root, text ="Enter", command = Enterwork)
    root.Enterbutton.pack()



    root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
    itemsforlistbox=[]
    itemsforcode=[]

    #Get usernames from database
    cursor.execute("select VoorNaam,Naam,PersoneelNum from Personeel")
    for row in cursor.fetchall():
        personeelsNaam = (row.VoorNaam)+(' ')+(row.Naam)
        itemsforlistbox.append(personeelsNaam)
        itemsforcode.append ([personeelsNaam,row.PersoneelNum])

    #Select a name
    def CurSelet(evt):
        value=str((mylistbox.get(mylistbox.curselection())))
        for item in itemsforcode:    
            if value in item[0]:
                print(item[1])

    #Make a listbox with names
    mylistbox=Listbox(root,width=15,height=10,font=('times',13))
    mylistbox.bind('<<ListboxSelect>>',CurSelet)
    mylistbox.place(x=32,y=90)

    for items in itemsforlistbox:
        mylistbox.insert(END,items)

    #root.mainloop()

     


    return


#Main
BuildUI()
EnterCommand()


