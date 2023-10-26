import mysql.connector
from tkinter import *
from tkinter import messagebox
from mysql.connector import Error
import os, sys
global py
py = sys.executable

#inintiating  the tkinter screen
root = Tk()
root.title('to do list')
root.config(bg = '#EE4E34')
root.geometry('720x720')

a =StringVar()
b =StringVar()
c =StringVar()
d=StringVar()

def b_q():
            if len(b.get()) == 0 or len(c.get()) == 0:
                messagebox.showerror("Error","Please Enter The Details")
            else:
                g = 'ongoing'
                try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='todolist',
                                         user='root',
                                         password='heelo.123')
                    myCursor = conn.cursor()
                    myCursor.execute("Insert into tasks(name,duedate,priority,ID,status) values (%s,%s,%s,%s,%s)",[b.get(),c.get(),d.get(),a.get(),'ongoing'])
                    conn.commit()
                    messagebox.showinfo('Info', 'Succesfully Added')
                    ask = messagebox.askyesno("Confirm", "Do you want to add another task?")
                    if ask:
                        root.destroy()
                        os.system('%s %s' % (py, 'add.py'))
                    else:
                        root.destroy()
                except Error:
                    print(a.get(),b.get(),c.get())
                    messagebox.showerror("Error","Check The Details")

#creating labels and input field

Label( text='Task details:',bg='#EE4E34',fg='#FCEDDA',font=('Courier new', 20, 'bold')).place(x=150, y=70)
Label( text='').pack()
Label( text='TASK ID(give a unique number)',bg='#EE4E34',fg='#FCEDDA', font=('Courier new', 10, 'bold')).place(x=60, y=180)
Entry( textvariable=a, width=30).place(x=170, y=200)
Label(text='TASK NAME:',bg='#EE4E34',fg='#FCEDDA', font=('Courier new', 10, 'bold')).place(x=60, y=230)
Entry( textvariable=b, width=30).place(x=170, y=232)
Label(text='DUE DATE(YYYY-MM-DD):',bg='#EE4E34',fg='#FCEDDA', font=('Courier new', 10, 'bold')).place(x=60, y=280)
Entry(textvariable=c, width=30).place(x=170, y=300)
Label(text='Task Priority',bg='#EE4E34',fg='#FCEDDA', font=('Courier new', 10, 'bold')).place(x=60, y=340)
Entry(textvariable=d, width=30).place(x=170, y=340)
Button(text="Submit",command = b_q).place(x=245, y=370)




root.mainloop()

