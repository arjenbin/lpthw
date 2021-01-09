import os
import time
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



def ui():
  Buildui = buildui


# Main
ui()
mainloop()


