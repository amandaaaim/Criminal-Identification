from tkinter import *
import shutil
import time
from PIL import ImageTk,Image
import sqlite3
from tkinter import filedialog
import tkinter.messagebox as tmsg
import cv2
from subprocess import call


if __name__ == "__main__":
   root = Tk()
   root.geometry('1200x700')
   root.configure(bg='#fff')
   root.resizable(False,False)
   root.title("Criminal Face Identification System")


Name=StringVar()
Bodymark=StringVar()
NIC=StringVar()
Crime=StringVar()
Gender = IntVar()
blood=StringVar()
file1=""

image=Image.open("images.jpg")
photo=ImageTk.PhotoImage(image)
photo_label=Label(image=photo,width=500,height=500).place(x=640,y=140)
photo_label
   
def warningwindow():
   value=tmsg.askquestion("WARNING !","Select all mandatory(*) fields.\n If completed, please continue.")
   if value=="yes":
      x=databaseEnter()
      if(x==1):
         tmsg.showinfo("Success","New Criminal has been added Successfully")
         root.destroy()
      else:
         tmsg.showinfo("Warning","Please enter all (*) marked details")


def getid():
   conn = sqlite3.connect('criminal.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('select max(ID) from People')
   conn.commit()
   for row in cursor:
    for elem in row:
        x = elem
   return x
   
def databaseEnter():
   name=Name.get()
   bl=blood.get()
   if(bl=="Select Blood Group"):
      bl=None
   body=Bodymark.get()
   nic=NIC.get()
   crime=Crime.get()
   Dob=dob.get()
   gen1=""
   gender=Gender.get()
   if(gender==1):
      gen1='Male'
   if(gender==2):
      gen1='Female'

   
   if(name!="" and crime!="" and gen1!=""):
      conn = sqlite3.connect('criminal.db')
      with conn:
         cursor=conn.cursor()
     
      cursor.execute('INSERT INTO People (Name,Gender,Blood,Bodymark,Nationality,Crime) VALUES(?,?,?,?,?,?)',(name,gen1,bl,body,nic,crime))
      conn.commit()
      x=getid()
      file="image/user." + str(x) + ".png"
      newPath = shutil.copy('temp/1.png',file)
   else:
      return 0
   return 1


def openfile():
   file1=filedialog.askopenfilename()
   newPath = shutil.copy(file1, 'temp/1.png')
   image=Image.open('temp/1.png')
   image = image.resize((500,500), Image.ANTIALIAS)
   photo=ImageTk.PhotoImage(image)
   photo_label=Label(image=photo,width=500,height=500).place(x=640,y=140).pack()
   label_ = Label(root, text=file1,width=70,font=("bold", 8))
   label_.place(x=200,y=630)
   
label_10 = Label(root, text="Criminal Face Identification System",width=80,font=("bold", 20),anchor=CENTER,bg="#386184",fg="white")
label_10.place(x=0,y=0)

heading = Label(root,text='Register Criminal',fg="#003366",width=80,anchor=CENTER,bg='white',font=('Microsoft Yahei UI Light',20,'bold'))
heading.place(x=0,y=47)
             


# Register Form

label_1 = Label(root, text='Criminal Name* :',fg="#000000",bg='white',font=('Microsoft Yahei UI Light',12))
label_1.place(x=70,y=150)

entry_1 = Entry(root,width=35,fg='black',bg='white',textvar=Name,font=('Microsoft Yahei UI Light',12))
entry_1.place(x=260,y=150)

label_3 = Label(root, text='Gender* :',fg="#000000",bg='white',font=('Microsoft Yahei UI Light',12))
label_3.place(x=70,y=200)

Radiobutton(root, text="Male",padx = 0,bg='white', variable=Gender, font=('Microsoft Yahei UI Light',12),value=1).place(x=260,y=200)
Radiobutton(root, text="Female",padx = 20, bg='white',variable=Gender,font=('Microsoft Yahei UI Light',12), value=2).place(x=325,y=200)

label_7 =  Label(root, text='NIC :',fg="#000000",bg='white',font=('Microsoft Yahei UI Light',12))
label_7.place(x=70,y=250)

entry_7 = Entry(root,width=35,textvar=NIC,fg="#000000",bg='white',font=('Microsoft Yahei UI Light',12))
entry_7.place(x=260,y=250)

label_5 = Label(root, text='Blood Group :',fg="#000000",bg='white',font=('Microsoft Yahei UI Light',12))
label_5.place(x=70,y=340)

list2 = ['A+','A-','B+','B-','AB+','AB-','O+','O-','Not known'];

droplist=OptionMenu(root,blood, *list2)
droplist.config(width=30,fg="#000000",bg='white',border=1,font=('Microsoft Yahei UI Light',12))
blood.set('Select Blood Group') 
droplist.place(x=260,y=340)

label_6 = Label(root, text='Body Mark :',fg="#000000",bg='white',font=('Microsoft Yahei UI Light',12))
label_6.place(x=70,y=300)

entry_6 = Entry(root,width=35,textvar=Bodymark,fg="#000000",bg='white',font=('Microsoft Yahei UI Light',12))
entry_6.place(x=260,y=300)


label_8= Label(root, text="Crime Scene :",fg="#000000",bg='white',font=('Microsoft Yahei UI Light',12))
label_8.place(x=70,y=390)

entry_8 = Entry(root,width=35,textvar=Crime,fg="#000000",bg='white',font=('Microsoft Yahei UI Light',12))
entry_8.place(x=260,y=390)

label_9 =  Label(root, text='Face Image* :',fg="#000000",bg='white',font=('Microsoft Yahei UI Light',12))
label_9.place(x=70,y=440)

btn=Button(root,width=20,pady=7,text='Choose an Image',bg='#c4d8e2',fg='black',border=0,command=openfile).place(x=260,y=440)

Button(root,width=50,pady=7,text='Register',bg='#0087bd',fg='white',border=0,command=warningwindow).place(x=170,y=530)

root.mainloop()
