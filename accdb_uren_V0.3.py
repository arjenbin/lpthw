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


def Enterwork():
    tijdnummer = entrytimenumber.get()
    personeelnummer = CurSelect2()
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


def CurSelect2():
    value=root.mylistbox.get(mylistbox.curselection())
    for item in itemsforcode:
            if value in item[0]:
                 print(item[1])
                 return item[1]

def CurSelect(evt):
    value= r
    for item in itemsforcode:
            if value in item[0]:
                 print(item[1])
                 return item[1]

def make_a_listbox_with_names(root):

    mylistbox=Listbox(root,width=15,height=10,font=('times',13))
    mylistbox.bind('<<ListboxSelect>>',CurSelect)
    mylistbox.place(x=32,y=90)
    itemsforlistbox=[]
    itemsforcode=[]

    #Get usernames from database
    cursor.execute("select VoorNaam,Naam,PersoneelNum from Personeel")
    for row in cursor.fetchall():
        personeelsNaam = (row.VoorNaam)+(' ')+(row.Naam)
        itemsforlistbox.append(personeelsNaam)
        itemsforcode.append ([personeelsNaam,row.PersoneelNum])
    for items in itemsforlistbox:
        mylistbox.insert(END,items)

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
    #entrypersoneelNumber = Entry(root)
    #entrypersoneelNumber.pack()

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

  
    root.Enterbutton=Button(root, text ="Enter", command = Enterwork)
    root.Enterbutton.pack()

 
    root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

    root.mylistbox = make_a_listbox_with_names(root)

    return root
    return itemsforcode, mylistbox




#Main
itemsforcode, root = BuildUI()
mainloop()

