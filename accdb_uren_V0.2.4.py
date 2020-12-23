import os
import time
import pyodbc
import sys
import datetime
import tkinter as tk
from tkinter import*
from tkinter import ttk
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from tkintertable import TableCanvas,TableModel

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


#def CurSelect2():
#    value=(mylistbox.get(mylistbox.curselection()))
#    for item in itemsforcode:
#            if value in item[0]:
#                 print(item[1])
#                 return item[1]

#def CurSelect(evt):
#   value= evt.widget
#    for item in itemsforcode:
#            if value in item[0]:
#                 print(item[1])
#                 return item[1]

#app = tk.Tk()

class Excel(tk.Frame):
    def __init__(self, master, rows, columns, width):
        super().__init__(master)

        #for i in range(columns):
            #self.make_entry(0, i+1, width, f'C{i}', False) 
        
        #for row in range(rows):
            #self.make_entry(row+1, 0, 5, f'R{row}', False)

      
        self.make_entry(0, 1, width, 'Opmerking', False) 
        self.make_entry(0, 2, width, 'Datum', False) 
        self.make_entry(0, 3, width, 'Aantal Uur', False) 
        #self.make_entry(0, 0, 5, 'row', False) 
               
        #for column in range(columns):
            #self.make_entry(1, column+1, width, '', True)

    def make_entry(self, row, column, width, text, state):
        e = tk.Entry(self, width=width)
        if text: e.insert(0, text)
        e['state'] = tk.NORMAL if state else tk.DISABLED
        e.coords = (row-1, column-1)
        e.grid(row=row, column=column)



def BuildUI():
    root= Tk()

    #Get pc screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    #Width and height of GUI
    uiWidth = 1200
    uiHeight = 600

    sizex = uiWidth
    sizey = uiHeight

    #position of GUI on screen
    posx  = (screen_width / 2) - uiWidth / 2
    posy  = (screen_height / 2) - uiHeight / 2



  
    root.Enterbutton=Button(root, text ="Enter", command = Enterwork)
    #root.Enterbutton.pack()

 
    root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
    


    frame = LabelFrame(root)
    frame.grid(row=2,column=0,padx=10,pady=10)
    #frame.pack(fill = "both", expand="false", pady=50, padx=50,)



    


    #Make a listbox with names
    itemsforcode=[]
    dates=[]

    cursor.execute("select * from TijdVerantwoording")

    for row in cursor.fetchall():
        itemsforcode.append ([row.Opmerking,row.Datum,row.Duur])

    cal = Calendar(font='Arial 14', selecmode='day',
        cursor="hand1", year=2019, month=1, day=1)
    cal.grid(row=0, column=0, padx=10, pady=10)

    def datesel():
            print(cal.selection_get())


    dateselbut = ttk.Button(text="Select Date", command= datesel)
    dateselbut.grid(row=1,column=0)

    

    def set_textstart(text):
        entry1.delete(0,END)
        entry1.insert(0,text)
        tester = entry1.get()
        #print("test",tester)
        #print("type",type(tester))
        return

    def set_textend(text):
        entry2.delete(0,END)
        entry2.insert(0,text)
        return

    entry1 = tk.Entry(root,width=20)
    entry2 = tk.Entry(root,width=20)
    entry1.grid(row=0,column=1)
    entry2.grid(row=1,column=1)

    entry1.insert(0,"1-1-2019")
    entry2.insert(0,"1-5-2019")

    ButtonStartDate = Button(root,text="Start Date",command=lambda:set_textstart(cal.selection_get()))
    ButtonStartDate.grid(row=0,column=2)

    ButtonEndDate = Button(root,text="End Date",command=lambda:set_textend(cal.selection_get()))
    ButtonEndDate.grid(row=1,column=2)

    mycanvas = Canvas(frame, width=850, height=300,bg='red')
    mycanvas.pack(side=LEFT)

    yscrollbar = ttk.Scrollbar(frame, orient="vertical", command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill="y")

    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

    myframe = Frame(mycanvas)
    mycanvas.create_window((0,0), window=myframe, anchor="n")

    #width = header column width
    ex = Excel(myframe, rows=100, columns=5, width=20)


    start_date = datetime.strptime(entry1.get(), '%d-%m-%Y')
    end_date = datetime.strptime(entry2.get(), '%d-%m-%Y')

    length = len(itemsforcode)

    for i in range(length):
        dates.append(itemsforcode[i][1])


    data = {'Record': {'Opmerking': itemsforcode[2][0],
    'Datum':str(itemsforcode[2][1]),
    'Aantal Uur': itemsforcode[2][2]},
    }  

    testdata = {'Record':{'Column1':'this is entry 1'}}
        
    

    tframe = Frame(root)
    tframe.grid(column=0, row=1)
    model = TableModel()
    model.importDict(testdata)
    

    table = TableCanvas(tframe,model,
    	cellwidth=100, cellbackgr='#e3f698',
    	thefont=('Arial',12),rowheight=25, rowheaderwidth=100,
    	rowselectedcolor='yellow', editable=True)
    table.show()

    #table.addRow(keyname,label=itemsforcode[0][0])
    #table.addRow(label=itemsforcode[0][1])
    #table = TableCanvas(frame, model=model,
	#		cellwidth=60, cellbackgr='#e3f698',
	#		thefont=('Arial',12),rowheight=18, rowheaderwidth=30,
	#		rowselectedcolor='yellow', editable=True)
    #table.show()

    #table = TableCanvas(tframe, model, cellwidth=60, cellbackgr='#e3f698',
    #	thefont=('Arial',12),rowheight=18,rowheaderwidth=3,
    #	rowselectedcolor='blue',editable=True)



    # for x in range(1000):
    #     if dates[x] >= start_date and dates[x] <= end_date:
    #         ex.make_entry(row=x, column=1, width=40, state = 'normal', text=itemsforcode[x][0])
    #         ex.make_entry(row=x, column=2, width=20, state = 'normal', text=itemsforcode[x][1])
    #         ex.make_entry(row=x, column=3, width=20, state = 'normal', text=itemsforcode[x][2])

    #     ex.pack(padx=10, pady=10)


    def redCircle():
    	pass


        

 

    

    

    def yelCircle():
    	root.update()

    

    #Right Frame and its contents
    rightFrame = LabelFrame(root, width=800, height = 600)
    rightFrame.grid(row=5, column=0, padx=10, pady=10)

    btnFrame = LabelFrame(rightFrame, width=100, height = 100)
    btnFrame.grid(row=5, column=0, padx=10, pady=2)

    redBtn = Button(btnFrame, text="Red", command=redCircle)
    redBtn.grid(row=5, column=0, padx=10, pady=2)

    yellowBtn = Button(btnFrame, text="Yellow", command=yelCircle)
    yellowBtn.grid(row=5, column=0, padx=10, pady=2)

    return








#Main
BuildUI()
mainloop()



