import os
import time
import pyodbc
import sys
import datetime
from tkinter import*
import csv


laptopdbpath ='D:/Users/Gebruiker/Documents/Python/TestDB.accdb'
pcdbpath = 'C:/Users/Gebruiker/lpthw/TestDB.accdb'


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:/Users/Gebruiker/Documents/Python/Erp4.accdb')
cursor = conn.cursor()


#Get bill data from database
cursor.execute("select RekeningVolgNummer,RekeningDatum,RekeningOmschrijving,RelatieNum,RekeningNummer,InitBedrag,TotaalBtw from Rekeningen")

with open('inkoopfacturen.csv', 'w', newline='') as file:
    writer = csv.writer(file) 
    for row in cursor.fetchall():
        writer.writerow(["Volgnummer:",row.RekeningVolgNummer,"Rekening Datum:",row.RekeningDatum,"Rekeningnummer:",row.RekeningNummer])

