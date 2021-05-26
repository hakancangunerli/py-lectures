from tkinter import *

root = Tk()
root.geometry('400x400')
# root.config(bg='Red')
root.title("Address Book")

#resizable tkinter
root.resizable(0,0)

contactlist = [
    ['can','978465321'],
    ['awm','321465978'],
    ['test','716573253'],
    ['rqw','256416584'],
    ['random','716573253'],
]

frame = Frame(root)
frame.pack()

scroll = Scrollbar(frame)
select = Listbox(frame,yscrollcommand=scroll.set,height=12)
scroll.config(command=select.yview) #What does config mean?

Name = StringVar()
number = StringVar()

Label(root,text="Name").place(x=30,y=20)
Entry(root,textvariable=Name ).place(x=140,y=20)
Label(root,text="Phone Number").place(x=30,y=70)
Entry(root,textvariable= number).place(x=140,y=70)

def Selected():
  return int()


def addContact():
  contactlist.append([Name.get(),number.get()])
  #adding name and number to contact
  print('Contact added')
  selectSet()

def selectSet():
  contactlist.sort()
  select.delete(0,END)
  for name,phone in contactlist:
    select.insert(END,name)
selectSet()
def editContact():
  contactlist[Selected()] = [Name.get(),number.get()]
  selectSet()

def deleteContact():
  del contactlist #del means delete
  selectSet()

def viewContact():
  NAME,PHONE = contactlist[Selected()]
  Name.set(NAME)
  number.set(PHONE) #sorts name and number to view

def exitContact():
  root.destroy()

def resetContact():
  Name.set('')
  number.set('')

Button(root,text="ADD",command= addContact).place(x=50,y=120)
Button(root,text="EDIT",command= editContact).place(x=50,y=150)
Button(root,text="DELETE",command= deleteContact).place(x=50,y=180)
Button(root,text="VIEW",command= viewContact).place(x=50,y=210)
Button(root,text="EXIT",command= exitContact).place(x=50,y=240)
Button(root,text="RESET",command= resetContact).place(x=50,y=270)
root.mainloop()