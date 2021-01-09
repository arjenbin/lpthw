import os
import time
import pyodbc
import sys
import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from tkintertable import TableCanvas, TableModel
from ConvertDate import convertdate
import buildui

laptopdbpath = 'D:/Users/Gebruiker/Documents/Python/TestDB.accdb'
pcdbpath = 'C:/Users/Gebruiker/lpthw/TestDB.accdb'

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:/Users/Gebruiker/Documents/Python/Erp4.accdb')
cursor = conn.cursor()


def Insert(Table, Tijdnummer, PersoneelNaam, Date, Projectnummer, Activiteitnummer, Uren, Opmerking):
    currentTime = datetime.datetime.now()

    sql = r"""insert into TijdVerantwoording 
    (TijdNum, DateChanged, PersoneelNum, Datum, ProjectNum, 
    ActiviteitNum, Duur, Opmerking) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

    cursor.execute(sql,
                   Tijdnummer, currentTime, PersoneelNaam, Date, Projectnummer,
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

    Insert(Table='TijdVerantwoording',
           Tijdnummer=tijdnummer,
           PersoneelNaam=personeelnummer,
           Date=datum,
           Projectnummer=projectnummer,
           Activiteitnummer=activiteitnum,
           Uren=duur,
           Opmerking=werk, )





def fillui():
    Buildui = buildui

    #Make a listbox with names
    itemsforcode = []
    cursor.execute("select * from TijdVerantwoording")
    for row in cursor.fetchall():
        itemsforcode.append([row.Opmerking, row.Datum, row.Duur])
    length = len(itemsforcode)


    key = 'key'
    itemdict = dict()

    dates = []
    date = '01-01-2020'
    for i in range(length):
        date = str(itemsforcode[i][1])[:-9]
        itemdict[key+str(i)]={'opmerking': itemsforcode[i][0], 'datum': date, 'aantal uur': itemsforcode[i][2]}

    return itemdict,itemsforcode


# Main
fillui()
mainloop()


