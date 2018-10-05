"""
GUI for Taylor Coats Database

Samuel taylor
"""

from tkinter import *
from TaylorCoats import FamDB

database=FamDB("Family.db")

#Function to get the all data of the row selected by user and enter it into entry fields
def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    e5.delete(0,END)
    e5.insert(END,selected_tuple[5])
    e6.delete(0,END)
    e6.insert(END,selected_tuple[6])
    e7.delete(0,END)
    e7.insert(END,selected_tuple[7])
 
#Function to clear data entered into the entry fields
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)

#Function to clear displayed data in entry fields and displayed data in listbox
def clearall():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    list1.delete(0,END)

#Function to call the view function in TaylorCoats.py and list data into the listbox
def view_command():
    list1.delete(0,END)
    for row in database.view():
	    list1.insert(END,row)
	
#Function to call the search function in TaylorCoats.py and display results  in listbox
def search_command():
    list1.delete(0,END)
    for row in database.search(name_text.get(),phone_text.get(), email_text.get(),street_text.get(),city_text.get(),state_text.get(),zip_text.get()):
        list1.insert(END,row)

#Function to call the add function in TaylorCoats.py to add entry into database
def add_command():
    database.insert(name_text.get(),phone_text.get(), email_text.get(),street_text.get(),city_text.get(),state_text.get(),zip_text.get())
    list1.delete(0,END)
    list1.insert(END,(name_text.get(),phone_text.get(), email_text.get(),street_text.get(),city_text.get(),state_text.get(),zip_text.get()))
    view_command()
    clear()
    
#Function to call the delete function in TaylorCoats.py to delete entry into database
def delete_command():
    database.delete(selected_tuple[0])
    view_command()

#Function to call the update function in TaylorCoats.py to update entry into database
def update_command():
    database.update(selected_tuple[0],name_text.get(),phone_text.get(), email_text.get(),street_text.get(),city_text.get(),state_text.get(),zip_text.get())
    view_command()


window=Tk()

#Show title of window for database
window.wm_title("Taylor/Coats Famliy Database")

#Entry label creation
l1=Label(window,text="Name")
l1.grid(row=0,column=0)

l2=Label(window,text="Phone")
l2.grid(row=0,column=2)

l3=Label(window,text="Email")
l3.grid(row=0,column=4)

l4=Label(window,text="Street")
l4.grid(row=1,column=0)

l5=Label(window,text="City")
l5.grid(row=1,column=2)

l6=Label(window,text="State")
l6.grid(row=1,column=4)

l7=Label(window,text="Zip")
l7.grid(row=1,column=6)
#End of entry label creation

#Entry textbox creation
name_text=StringVar()
e1=Entry(window,textvariable=name_text)
e1.grid(row=0,column=1)

phone_text=StringVar()
e2=Entry(window,textvariable=phone_text)
e2.grid(row=0,column=3)

email_text=StringVar()
e3=Entry(window,textvariable=email_text)
e3.grid(row=0,column=5)

street_text=StringVar()
e4=Entry(window,textvariable=street_text)
e4.grid(row=1,column=1)

city_text=StringVar()
e5=Entry(window,textvariable=city_text)
e5.grid(row=1,column=3)

state_text=StringVar()
e6=Entry(window,textvariable=state_text)
e6.grid(row=1,column=5)

zip_text=StringVar()
e7=Entry(window,textvariable=zip_text)
e7.grid(row=1,column=7)
#End of entry textbox creation

#Listbox creation for database display
list1=Listbox(window,height=36,width=155)
list1.grid(row=3,column=0,rowspan=6,columnspan=11)
#End of listbox creation

#Scrollbar creation for database display
sb1=Scrollbar(window)
sb1.grid(row=3,column=11,rowspan=5)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)
#End of scrollbar creation

#Button creation
b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=4,column=12)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=4,column=13)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=5,column=12)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=5,column=13)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=6,column=12)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=12)

b7=Button(window,text="Clear All", width=12,command=clearall)
b7.grid(row=6,column=13)
#End button creation

window.mainloop()