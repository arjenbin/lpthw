import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from tkintertable import TableCanvas, TableModel
from makedata import *

root = Tk()

# Get pc screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Width and height of GUI
uiWidth = 1200
uiHeight = 600

sizex = uiWidth
sizey = uiHeight

# position of GUI on screen
posx = (screen_width / 2) - uiWidth / 2
posy = (screen_height / 2) - uiHeight / 2


root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

frame = LabelFrame(root)
frame.grid(row=2, column=0, padx=10, pady=10)

cal = Calendar(font='Arial 14', selecmode='day',
               cursor="hand1", year=2019, month=1, day=1)

cal.grid(row=0, column=0, padx=10, pady=10)

def datesel():
    pass

dateselbut = ttk.Button(text="Select Date", command=datesel)
dateselbut.grid(row=1, column=0)

entry1 = tk.Entry(root, width=20)
entry2 = tk.Entry(root, width=20)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

entry1.insert(0, "1-1-2019")
entry2.insert(0, "1-5-2019")


ButtonStartDate = Button(root, text="Start Date", command=lambda: set_textstart(newdate))
ButtonStartDate.grid(row=0, column=2)

ButtonEndDate = Button(root, text="End Date", command=lambda: set_textend(cal.selection_get()))
ButtonEndDate.grid(row=1, column=2)

mycanvas = Canvas(frame, width=850, height=300, bg='red')
mycanvas.pack(side=LEFT)

yscrollbar = ttk.Scrollbar(frame, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0, 0), window=myframe, anchor="n")

start_date = datetime.strptime(entry1.get(), '%d-%m-%Y')
end_date = datetime.strptime(entry2.get(), '%d-%m-%Y')

tframe = Frame(root)
tframe.grid(column=0, row=1)
model = TableModel()


Makedata = makedata()
itemdict = Makedata.dictitems()

model.importDict(itemdict)

table = TableCanvas(tframe, model,
                    cellwidth=100, cellbackgr='#e3f698',
                    thefont=('Arial', 12), rowheight=25, rowheaderwidth=100,
                    rowselectedcolor='yellow', editable=True)
table.show()

