from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

#creating window

root = Tk()
root.title('Remove detaisl')
root.configure(bg = '#EE4E34')
root.geometry('500x300')
#creating the main function of the entire program that executes commands
a = StringVar()
b= StringVar()
def ent():

    if len(a.get()) ==0:
        messagebox.showinfo("Error","Please Enter A Valid Id")
    else:
        d = messagebox.askyesno("Confirm", "Are you sure you want to change records?")
        if d:
            try:
                conn = mysql.connector.connect(host='localhost',
                                    database='todolist',
                                    user='root',
                                    password='heelo.123')
                myCursor = conn.cursor()
                myCursor.execute("update tasks set status = %s where ID = %s",[b.get(),a.get()])
                conn.commit()
                myCursor.close()
                conn.close()
                messagebox.showinfo("Confirm","Data Changed Successfully")
                a.set("")
            except:
                messagebox.showerror("Error","Something goes wrong")
Label(root,text = "Task Id: ",bg='#EE4E34',fg='black',font=('Courier new', 15, 'bold')).place(x = 5,y = 40)
Entry(root,textvariable = a,width = 37).place(x = 160,y = 44)
Label(root,text = "Status of the task(On-going/done):",bg='#EE4E34',fg='black',font=('Courier new', 15, 'bold')).place(x = 5,y = 100)
Entry(root,textvariable = b,width = 37).place(x = 5,y = 130)
Button(root,text='Remove', width=15, font=('arial', 10),command = ent).place(x=200, y = 190)

root.mainloop()