from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


#basic screen gui
root = Tk()
root.title('to do list')
root.config(bg = '#EE4E34')
root.geometry('1280x920')

f = StringVar() # to store data entered by the user
g = StringVar() # to select input from drop down menu

# creating a function for tabel view
def handle(event):
    if listTree.identify_region(event.x,event.y) == "separator":
        return "break"






#creating the tabel view
l1=Label(root,text="Search Tasks",bg='#EE4E34', font=("Courier new",20,'bold')).place(x=600,y=20)
l = Label(root, text="Search By",bg='#EE4E34', font=("Courier new", 15, 'bold')).place(x=60, y=96)

listTree = ttk.Treeview(height=13,columns=('Task Name', 'Due Date', 'Availability','Priority', 'Task ID'))
vsb = ttk.Scrollbar(orient="vertical",command=listTree.yview)
listTree.configure(yscrollcommand=vsb.set)
listTree.heading("#0", text='Task ID', anchor='center')
listTree.column("#0", width=120, anchor='center')
listTree.heading("#1", text='Task Name')
listTree.column("#1", width=200, anchor='center')
listTree.heading("#2", text='Availability')
listTree.column("#2", width=200, anchor='center')
listTree.heading("#3", text='Priotity')
listTree.column("#3", width=200, anchor='center')
listTree.heading("#4", text='Due Date')
listTree.column("#4", width=200, anchor='center')
listTree.bind('<Button-1>', handle)
listTree.place(x=40, y=200)
vsb.place(x=1000,y=200,height=287)
ttk.Style().configure("Treeview", font=('Times new Roman', 15))

#creating the main program that checks and prints stuff

# creating a function to insert data into the tabelview
def insert(x):
    listTree.delete(*listTree.get_children())
    for row in x:
        listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))

#main function that check the input and does all the linkage with database
def ge():
    if (len(g.get())) == 0:
        messagebox.showinfo('Error', 'First select a item')
    elif (len(f.get())) == 0:
        messagebox.showinfo('Error', 'Enter the '+g.get())
    elif g.get() == 'Task Name':
        try:
            conn = mysql.connector.connect(host='localhost',
                                    database='todolist',
                                    user='root',
                                    password='heelo.123')
            mycursor =conn.cursor()
            mycursor.execute("Select * from tasks where name LIKE %s",['%'+f.get()+'%'])
            pc = mycursor.fetchall()
            if pc:
                insert(pc)
            else:
                messagebox.showinfo("Oop's","Either Task Name is incorrect or it is not available")
        except Error:
            messagebox.showerror("Error","Something goes wrong")
    elif g.get().lower() =='due date':
        try:
            conn = mysql.connector.connect(host='localhost',
                                    database='todolist',
                                    user='root',
                                    password='heelo.123')
            mycursor = conn.cursor()
            mycursor.execute("Select * from tasks where duedate LIKE %s", ['%'+f.get()+'%'])
            pc = mycursor.fetchall()
            if pc:
                insert(pc)
            else:
                messagebox.showinfo("Oop's","No such details found")
        except Error:
            messagebox.showerror("Error","Something goes wrong")
    elif g.get() == 'Task Id':
        try:
            conn = mysql.connector.connect(host='localhost',
                                    database='todolist',
                                    user='root',
                                    password='heelo.123')
            mycursor = conn.cursor()
            mycursor.execute("Select * from tasks where ID LIKE %s", ['%'+f.get()+'%'])
            pc = mycursor.fetchall()
            print(pc)
            if pc:
                insert(pc)
                print(pc)
            else:
                messagebox.showinfo("Oop's","Either Task Id is incorrect or it is not available")
        except Error:
            messagebox.showerror("Error","Something goes wrong")
    elif g.get() == 'Availability':
        try:
            conn = mysql.connector.connect(host='localhost',
                                    database='todolist',
                                    user='root',
                                    password='heelo.123')
            mycursor = conn.cursor()
            mycursor.execute("Select * from tasks where status LIKE %s", ['%'+f.get()+'%'])
            pc = mycursor.fetchall()
            if pc:
                insert(pc)
            else:
                messagebox.showinfo("Oop's","No such details available")
        except Error:
            messagebox.showerror("Error","Something goes wrong")
find = Button(root,text="Find",width=15,bg='gray',font=("Courier new",10,'bold'),command=ge).place(x=460,y=148)
en = Entry(root,textvariable=f,width=43).place(x=180,y=155)
la = Label(root, text="Enter",bg='#EE4E34', font=("Courier new", 15, 'bold')).place(x=100, y=150)
#creating a drop down menu box
c=ttk.Combobox(textvariable=g,values=["Task Name","Due Date","Task Id", "Availability"],width=40,state="readonly").place(x = 180, y = 100)

#creating a function to handel table view


root.mainloop()