from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database

# import db
win = Tk()
win.geometry('550x350')

db1= database.Database('d:/mydata.db')

# ======Function 
def add_item():
    fname = name_entry.get()
    lname = family_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    db1.insert(fname, lname, address, phone)
    show_list()
    clear()

def show_list():
    contact_list.delete(0,END)
    records =db1.select()
    for rec in records:
        contact_list.insert(END,rec)

def clear():
    name_entry.delete(0,END)
    family_entry.delete(0,END)
    address_entry.delete(0,END)
    phone_entry.delete(0,END)
    name_entry.focus_set()

def remove_item():
    global data
    # index = contact_list.curselection()
    # data = contact_list.get(index)
    result = messagebox.askquestion('Delete',f'Are you sure deleted {data[1]} {data[2]}?')
    if result == 'yes':
        db1.delete(data[0])
        show_list()

def select_item(event):
    global data
    clear()
    index = contact_list.curselection()
    data = contact_list.get(index)
    name_entry.insert(0,data[1])
    family_entry.insert(0,data[2])
    address_entry.insert(0,data[3])
    phone_entry.insert(0,data[4])
    
def update_item():
    global data
    db1.update(data[0],name_entry.get(),family_entry.get(),address_entry.get(),phone_entry.get())
    show_list()
    clear()

def search_item():
    records = db1.search(search_entry.get())
    contact_list.delete(0,END)
    if len(records)==0:
        contact_list.configure(fg='#ff0000',font='arial 18 bold')
        contact_list.insert(0,'Record Not Found!!!')
    else:    
        for rec in records:
            contact_list.insert(END,rec)

def cancel():
    win.destroy()
    
    
# buttons and enry=====================================================================
name_text = StringVar()
name_label = Label(win, text = "Name:",bg='red', font = ('Tahoma 14'))
name_label.place(x =10 , y = 5)
name_entry = Entry(win, textvariable = name_text, bd = 3, relief = GROOVE)
name_entry.place(x = 90 , y =10)
print('***************')

address_text = StringVar()
address_label = Label(win, text = "Address:",bg='#F8B195', font = ('Tahoma', 14))
address_label.place(x = 275 , y = 5)
address_entry = Entry(win, textvariable = address_text, bd = 3, relief = GROOVE)
address_entry.place(x = 360 , y = 5)


family_text = StringVar()
family_label = Label(win, text = "Family:",bg='#F8B195', font = ('Tahoma', 14))
family_label.place(x = 10 , y = 35)
family_entry = Entry(win, textvariable = family_text, bd = 3, relief = GROOVE)
family_entry.place(x = 90 , y = 35)


phone_text = StringVar()
phone_label = Label(win, text = "Phone:",bg='#F8B195', font = ('Tahoma', 14))
phone_label.place(x = 275 , y = 35)
phone_entry = Entry(win, textvariable = phone_text, bd = 3, relief = GROOVE)
phone_entry.place(x = 360 , y = 35)


fetch_btn=Button(win,text='Show',bg='#F8B195',command=show_list,width=18)
fetch_btn.place(x=650,y=100)



contact_list = Listbox(win, height = 10, width =120  ,bd = 3)    
contact_list.place(x = 10 , y = 180)





scrollbar = Scrollbar(win)
scrollbar.place(x = 750 , y = 180,height=165)


contact_list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = contact_list.yview)


add_btn = Button(win, text = "insert",bg='#F8B195', width = 18, command = add_item)
add_btn.place(x = 500 , y = 20)

remove_btn = Button(win, text = "delete",bg='#F8B195', width = 18, command =remove_item)
remove_btn.place(x = 500 , y = 55)

update_btn = Button(win, text = "update",bg='#F8B195', width = 18, command = update_item)
update_btn.place(x = 650 , y = 20)

clear_btn = Button(win, text = "delete inputs",bg='#F8B195', width = 18, command = clear)
clear_btn.place(x = 650 , y = 55)

search_btn = Button(win, text="search",bg='#F8B195', width=18, command=search_item)
search_btn.place(x=120, y=100) 
search_text = StringVar()
search_entry = Entry(win, textvariable = search_text, bd = 3, relief = GROOVE)
search_entry.place(x = 275 , y = 100)

exit_a = Button(win, text = "cancel",bg='#F8B195', width = 18, command = cancel)
exit_a.place(x = 500 , y = 100)

search_label = Label(win)
search_label.grid(row= 3, column= 3)
win.title("contact manager")
win.geometry('800x400')
win.resizable(0, 0)
win.configure(bg = '#6C5B7B')


contact_list.bind('<<ListboxSelect>>', select_item)
win.mainloop()
