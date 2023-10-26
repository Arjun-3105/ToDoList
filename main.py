from tkinter import *
import os, sys
import mysql.connector

global py
py = sys.executable


#connecting to the database:
try: 
    conn = mysql.connector.connect(host='localhost',
                                            database='todolist',
                                            user='root',
                                            password='heelo.123')
except:
    print('error')

# creating the window
root = Tk()
root.title('to do list')
root.config(bg = '#EE4E34')
root.geometry('1080x720')
#creating and linking the database


label = Label(root, text = ' TO DO LIST', font  = ('Arial', 50), bg = '#EE4E34', fg = '#FCEDDA')
label.pack()

def add():
    # root.destroy()
    global py
    os.system('%s %s' % (py, 'add.py'))
    
    

def remove():
    
    # global py
    root.destroy()
    os.system('%s %s' % (py, 'remove.py'))
    

    

def display():
    # root.destroy()
    global py
    os.system('%s %s' % (py, 'show.py'))

def mark():
    global py
    os.system('%s %s' % (py,'mark.py'))
    
    

#creating buttons
button_frame = Frame(root, bg = '#EE4E34')
button_frame.pack()

button_add = Button(button_frame, text = 'Add tasks', bg = '#EE4E34', fg = '#FCEDDA', font = ('arial', 20), command = add)
button_display = Button(button_frame, text = 'Display', bg = '#EE4E34', fg = '#FCEDDA', font = ('arial', 20), command = display)
button_remove = Button(button_frame, text = 'remove task', bg = '#EE4E34', fg = '#FCEDDA', font = ('arial', 20), command = remove)
button_quit = Button(button_frame, text = 'QUIT', bg = '#EE4E34', fg = '#FCEDDA', font = ('arial', 20), command = root.quit)
button_mark = Button(root, text='Mark Tasks', bg = '#EE4E34',fg= '#FCEDDA',font = ('arial', 20), command = mark)

button_add.pack(pady =20)
button_display.pack(pady =20 )
button_remove.pack(pady=20)
button_mark.pack(pady=20)
button_quit.pack(pady=20)



root.mainloop()