from tkinter import * 
from tkinter import ttk
import shutil
from PIL import ImageTk,Image
import sqlite3
from tkinter import filedialog
import tkinter.messagebox as tmsg
import cv2,os
import face_recognition as fr
import numpy as np
import math
import winsound

if __name__ == "__main__":
   root = Tk()
   root.geometry('1300x750')
   root.configure(bg='#fff')
   root.title("Criminal Face Identification System")
   
image=Image.open("images.jpg")


image = image.resize((400,400), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
photo_label=Label(image=photo,width=400,height=400).place(x=90,y=110)
photo_label

label_1 = Label(root, text="Select an Image",bg='#382273',fg='white',width=50,font=("bold", 15))
label_1.place(x=30,y=60)
label_177 = Label(root, text="Results",bg='#fff',fg='black',width=50,font=("bold", 15))
label_177.place(x=700,y=48)

label_0 = Label(root, text="Criminal Face Identification System",width=85,font=("bold", 20),anchor=CENTER,bg="#386184",fg="white")
label_0.place(x=0,y=0)



def viewdetail(a):
   conn = sqlite3.connect("criminal.db")
   cur = conn.cursor()
   cur.execute("SELECT * FROM people where Id="+str(a))
   rows = cur.fetchall()
   print(rows)
   frame=Frame(root,width=500,height=420,bg='white')
   frame.place(x=850,y=350)
   
   for row in rows:
      label_n = Label(frame, text=row[1],bg="white",fg='white',width=20,font=("bold", 12))
      label_n.place(x=120,y=10)
      label_g = Label(frame, text=row[2],bg="white",fg='black',width=20,font=("bold", 12))
      label_g.place(x=120,y=70)
      label_bl = Label(frame, text=row[6],bg="white",fg='black',width=20,font=("bold", 12))
      label_bl.place(x=120,y=140)
      label_b = Label(frame, text=row[7],bg="white",fg='black',width=20,font=("bold", 12))
      label_b.place(x=120,y=210)
      label_n = Label(frame, text=row[8],bg="white",fg='black',width=20,font=("bold", 12))
      label_n.place(x=120,y=280)
      label_c = Label(frame, text=row[9],width=70,bg="white",font=("bold", 15),fg="red")
      label_c.place(x=120,y=350)
     
   conn.close()
 
    
   label_name = Label(frame, text="Name :",bg="white",fg='black',width=20,font=("bold", 12))
   label_name.place(x=0,y=10)
   label_gender = Label(frame, text="Gender :",bg="white",fg='black',width=20,font=("bold", 12))
   label_gender.place(x=0,y=70)
   label_bloodgroup = Label(frame, text="Blood Group :",bg="white",fg='black',width=20,font=("bold", 12))
   label_bloodgroup.place(x=0,y=140)
   label_body = Label(frame, text="BodyMark :",bg="white",fg='black',width=20,font=("bold", 12))
   label_body.place(x=0,y=210)
   label_nat = Label(frame, text="NIC :",bg="white",fg='black',width=20,font=("bold", 12))
   label_nat.place(x=0,y=280)
   label_crime = Label(frame, text="Crime :",bg="white",width=20,font=("bold", 12),fg="red")
   label_crime.place(x=0,y=350)


   x='user.'+str(a)+".png"
   image=Image.open('image/'+x)
   image = image.resize((200,200), Image.ANTIALIAS)
   photo=ImageTk.PhotoImage(image)
   photo_l=Label(image=photo,width=200,height=200).place(x=650,y=400).pack()


def mfileopen():
   cleartree()
   file1=filedialog.askopenfilename()
   print(file1)
   newPath = shutil.copy(file1, 'temp/1.png')
   image=Image.open('temp/1.png')
   image = image.resize((400,400), Image.ANTIALIAS)
   photo=ImageTk.PhotoImage(image)
   photolbl=Label(image=photo,width=400,height=400).place(x=90,y=110).pack()

def cleartree():
   records=tree.get_children()
   for el in records:
      tree.delete(el)
                                                            
   
def doubleclick(event):
   item=tree.selection()
   itemid=tree.item(item,"values")
   ide=itemid[0]
   ide=(int(ide))
   viewdetail(ide)
    
def load_images_from_folder(folder):
    images=[]
    for filename in os.listdir(folder):
      images.append(filename)
    return images

def showPercentageMatch(face_distance,face_match_threshold=0.6):
    if face_distance > face_match_threshold:
      range = (1.0 - face_match_threshold)
      linear_val = (1.0 - face_distance) / (range * 2.0)
      return linear_val
    else:
      range = face_match_threshold
      linear_val = 1.0 - (face_distance / (range * 2.0))
      return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))


def View():
    cleartree()
    frame =cv2.imread("temp/1.png")

    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)

 
    rgb_small_frame=small_frame[:,:,::-1]


    if process_this_frame:
     
        face_locations=fr.face_locations(rgb_small_frame)
        face_encodings=fr.face_encodings(rgb_small_frame,face_locations)
        face_names=[]
        for face_encoding in face_encodings:
         
          matches=fr.compare_faces(encodings,face_encoding)
          print(matches)
          Id=0
          face_distances=fr.face_distance(encodings,face_encoding)
          best_match_index=np.argmin(face_distances)
          percent=showPercentageMatch(face_distances[best_match_index])

          if matches[best_match_index]:
            Id=known_face_names[best_match_index]
          face_names.append(Id)

          confidence=str(round(percent*100,2))+"%"

          conn = sqlite3.connect("criminal.db")
          cur = conn.cursor()
          cur.execute("SELECT ID,name,crime,nationality FROM people where ID="+str(Id))
          rows = cur.fetchall()
          print(rows)

          if(len(rows)>0):
            row=rows[0]
            a="Matching "+str(percent*100)+"%"
            tree.insert("", 'end', values=row)
            tree.bind("<Double-1>",doubleclick)
    

          else:
            a="No Matching Faces Found!"


          label_Match = Label(root, text=a,bg="#003399",fg='yellow',width=35,font=("bold", 15))
          label_Match.place(x=20,y=690)
         
          conn.close()
    
Fullname=StringVar()
father=StringVar()
var = IntVar()
c=StringVar()
d=StringVar()
var1= IntVar()
file1=""

btn=Button(text="Select photo",bg='#c4d8e2',width=20,command=mfileopen).place(x=200,y=550)

tree= ttk.Treeview(root, column=("column1", "column2", "column3","column4"), show='headings')
ttk.Style().configure("Treeview.Heading",font=('Microsoft Yahei UI Light',11,'bold') ,fg="#00008b", relief="flat")

tree.heading("#1", text="Criminal-ID")
tree.column("#1", minwidth=0, width=120, stretch=NO)

tree.heading("#2", text="NAME")
tree.column("#2", minwidth=0, width=220, stretch=NO)

tree.heading("#3", text="CRIME")
tree.column("#3", minwidth=0, width=150, stretch=NO)

tree.heading("#4", text="NIC")
tree.column("#4", minwidth=0, width=130, stretch=NO)

tree.place(x=640,y=90)


images=load_images_from_folder("image")

    #get image names
images_name=[]
for img in images:
      images_name.append(fr.load_image_file(os.path.join("image",img)))
    
    #get their encodings
encodings=[]
for img in images_name:
      encodings.append(fr.face_encodings(img)[0])


    #get id from images
known_face_names=[]
for name in images:
      known_face_names.append((os.path.splitext(name)[0]).split('.')[1])


face_locations=[]
face_encodings=[]
face_names=[]
process_this_frame=True



b2=Button(text="View Matching Records",width=35,height=2,command=View,bg='#003399',fg="white").place(x=165,y=620)


root.mainloop()