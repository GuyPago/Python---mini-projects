import tkinter as tk
from data.Project_4_classes import *
import Project_4_Guys_Company
import glob
import re
from data.pics import *
from tkinter import messagebox,simpledialog
def find_emps():
    e.delete(0,'end')
    list = [(i.id, i.fullname) for i in Employee.staff if i.lv!=0]
    list_box.delete(0,'end')
    for id,word in list:
        list_box.insert('end','. '.join([str(id),word]))

def search_command(event=None):
    list = [(i.id, i.fullname) for i in Employee.staff if i.lv!=0]

    if event is None:
        if len(e.get()) == 0:
            return find_emps()
        else:
            text = e.get().lower()

    elif event.keysym != 'BackSpace':
        text = e.get().lower() + event.char
    else:
        text = e.get()[:-1].lower()
    list_box.delete(0, 'end')

    if text: # search only if text is not empty
        for id,word in list:
            if re.search(text,word.lower()):
                list_box.insert('end','. '.join([str(id),word]))

def app_raise():
    try:

        simpledialog.askfloat('how much?','hey',maxvalue=500,parent=list_box)

        click = list_box.curselection()
        id = list_box.get(click)
        emp = list(filter(lambda x:x.lv!=0 and x.id==int(id[0]),Employee.staff))[0]
        emp.apply_raise()
        search_command()
    except tk.TclError:
        print("Can't give a raise to 'None'")
def test():
    try:
        click = list_box.curselection()
        id = list_box.get(click)
        emp = list(filter(lambda x:x.lv!=0 and x.id==int(id[0]),Employee.staff))[0]
        if messagebox.askyesno(title='Fire ' + emp.first,
        message='Are you sure you want to fire ' +emp.fullname+'?' ):
            emp.fire()
            search_command()
        else:
            print('{} is saved!'.format(emp.first))


    except tk.TclError:
        print("Can't fire 'None'")



root = tk.Tk()
img = tk.PhotoImage(file='data\pics\HR_logo.png')
HR = tk.Label(image=img,bg='lightgray')
HR.grid(row=0,column = 3,sticky='nsew')
root.configure(background='lightgray')
root.geometry('640x480')
root.title('Pago-Corp HR')
mylabel_1 = tk.Label(root,text='Welcome to Pago-corp HR system.')
# mylabel_1.pack()
# mylabel_1.grid(row=0,column=0)

#Button:
my_button = tk.Button(root,text='Print Employees',padx=30,pady=30,
            command=Employee.print_workers,fg='blue',bg='gray',width=12)
my_button_2 = tk.Button(root,text='Print Salaries',padx=30,pady=30,
            command=Employee.print_salaries,fg='blue',bg='gray',width=12)
my_button.grid(row=2,column=2,pady=5,padx=50)
my_button_2.grid(row=3,column=2,pady=5,padx=50)






frame = tk.Frame(root)
frame.configure(background='lightgray')
frame.grid(row=1,column=3)


e = tk.Entry(frame)
# title = tk.Label(image=)
e.insert(0,'')
e.bind(sequence='<Key>',func=search_command)
e.grid(row=1)
test_button = tk.Button(frame,command=find_emps,text='All')
test_button.grid(row=1,column=3)

emp_buttons = tk.Frame(root)
emp_buttons.grid(row=1,column=4)
test_button_3 = tk.Button(emp_buttons,command=test,text='Fire')
test_button_3.grid(row=0,column=0)
test_button_4 = tk.Button(emp_buttons,command=app_raise,text='Raise')
test_button_4.grid(row=0,column=1)

list_box = tk.Listbox(frame,selectmode=True)

list_box.grid()

#Run program
root.mainloop()
