import face_recognition
import imutils
import pickle
import time
import cv2
import tkinter
from imutils import paths
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import shutil
from pathlib import Path
import os
from subprocess import call
import ast

from PIL import ImageTk

from tkinter import messagebox


class Login:
    
    def __init__(self,root):

       self.root=root

       self.root.title("Criminal Identification System")

       self.root.geometry("925x500+20+20")
       self.root.configure(bg='#fff')

       self.root.resizable(False,False)
       
       self.homewindow()
    
    
    def registercriminal(self):
        call(["python", "registercriminal.py"])
        
    def detectCriminal(self):
        call(["python", "photomatch.py"])

    def regformclear(self):

       self.t1.delete(0,END)
       self.t2.delete(0,END)

    def detectformclear(self):

       self.t3.delete(0,END)


    def DetectPerson(self):

       frame1=Frame(self.root,width=500,height=420,bg='white')

       frame1.place(x=400,y=50)

       heading = Label(frame1,text='Detect Person',fg="#003366",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
       heading.place(x=90,y=5)
       
       self.lbl2 = Label(frame1, text='Video Path :',fg="#000000",bg='white',font=('Microsoft Yahei UI Light',12)).place(x=10,y=80)
      
       self.t3 = Entry(frame1,width=35,fg='black',bg='white',font=('Microsoft Yahei UI Light',12))
       self.t3.place(x=120,y=80)

       self.b1 = Button(frame1,width=20,pady=7,text='Choose a Video',bg='#0087bd',fg='white',border=0,command=self.select_file_vid).place(x=120,y=120)
       self.b3=Button(frame1,width=20,pady=7,text='clear',bg='#f0f8ff',fg='black',border=1,command=self.detectformclear).place(x=300,y=120)
       self.b2=Button(frame1,width=45,pady=7,text='Detect Person',bg='#0087bd',fg='white',border=0,command=self.train_).place(x=120,y=200)
       
       
       self.lbl7 = Label(frame1, text='Navigate to Criminal Identification System',bg='white',font=('Microsoft Yahei UI Light',10)).place(x=10,y=350)
       self.b9=Button(frame1,pady=7,text='Click here',bg='white',fg='#57a1f8',border=0,command=self.homewindow,font=('Microsoft Yahei UI Light',10)).place(x=260,y=343)
       

    def homewindow(self):
        
        frame3=Frame(self.root,width=500,height=420,bg='white')
        frame3.place(x=400,y=40)
        
        label_0 = Label(root, text="Criminal Face Identification System",width=50,font=("bold", 24),anchor=CENTER,bg="#386184",fg="white")
        label_0.place(x=0,y=0)

        Button(frame3, text='REGISTER PERSON',width=35,height=3,bg='#0f52ba',fg='white',font=("bold", 11),command=self.RegisterPerson).place(x=80,y=70)
        Button(frame3, text='REGISTER CRIMINAL',width=35,height=3,bg='#0f52ba',fg='white',font=("bold", 11),command=self.registercriminal).place(x=80,y=140)
        Button(frame3, text='IMAGE MATCH',width=35,height=3,bg='#0f52ba',fg='white',font=("bold", 11),command=self.detectCriminal).place(x=80,y=210)
        Button(frame3, text='VIDEO SURVEILLANCE',width=35,height=3,bg='#0f52ba',fg='white',font=("bold", 11),command=self.DetectPerson).place(x=80,y=280)
       
    def RegisterPerson(self):
       
       frame=Frame(self.root,width=500,height=420,bg='white')
       frame.place(x=420,y=50)

       heading = Label(frame,text='Register Person',fg="#003366",bg='white',font=('Microsoft Yahei UI Light',20,'bold'))
       heading.place(x=90,y=5)
       self.lbl1 = Label(frame, text='Person Name :',fg="#000000",bg='white',font=('Microsoft Yahei UI Light',12)).place(x=0,y=80)
       self.lbl2 = Label(frame, text='Image Path :',fg="#000000",bg='white',font=('Microsoft Yahei UI Light',12)).place(x=0,y=150)

       self.t1 = Entry(frame,width=35,fg='black',bg='white',font=('Microsoft Yahei UI Light',12))
       self.t1.place(x=120,y=80)
       self.t2 = Entry(frame,width=35,fg='black',bg='white',font=('Microsoft Yahei UI Light',12))
       self.t2.place(x=120,y=150)

       self.b3 = Button(frame,width=20,pady=7,text='Choose an Image',bg='#0087bd',fg='white',border=0,command=self.select_file).place(x=120,y=200)
       self.b3 = Button(frame,width=20,pady=7,text='Clear',bg='#f0f8ff',fg='black',border=1,command=self.regformclear).place(x=300,y=200)
       self.b4=Button(frame,width=45,pady=7,text='Add',bg='#0087bd',fg='white',border=0,command=self.runVid).place(x=120,y=260)
       
       self.lbl2 = Label(frame, text='Navigate to Criminal Identification System',bg='white',font=('Microsoft Yahei UI Light',10)).place(x=0,y=350)
       self.b5=Button(frame,pady=7,text='Click here',bg='white',fg='#57a1f8',border=0,command=self.homewindow,font=('Microsoft Yahei UI Light',10)).place(x=260,y=343)
      
    
       
    def select_file(self):
       
       if (len(self.t1.get()) < 1):
           showinfo(
               title='Error',
               message='Person Name Required!'
           )
           return
       
       filetypes = (
           ('image files', '*.jpg'),
           ('All files', '*.*')
       )
       
       filename = fd.askopenfilename(
           title='Open a file',
           initialdir='/',
           filetypes=filetypes)
       dir_path = os.path.dirname(os.path.realpath(__file__))
       Path(dir_path + "\\images\\" + self.t1.get()).mkdir(parents=True, exist_ok=True)
       shutil.move(filename, dir_path + "\\images\\" + self.t1.get() + "\\1.jpg")
       self.t2.insert(END, str(filename))
    

    def select_file_vid(self):
        filetypes = (
            ('image files', '*.mp4'),
            ('All files', '*.*')
        )
    
        filename = fd.askopenfilename(
            title='Open a Video file',
            initialdir='/',
            filetypes=filetypes)
        self.t3.insert(END, str(filename))
    
    def runVid(self):
        imagePaths = list(paths.list_images('Images'))
        knownEncodings = []
        knownNames = []
        # loop over the image paths
        for (i, imagePath) in enumerate(imagePaths):
            # extract the person name from the image path
            name = imagePath.split(os.path.sep)[-2]
            # load the input image and convert it from BGR (OpenCV ordering)
            # to dlib ordering (RGB)
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # Use Face_recognition to locate faces
            boxes = face_recognition.face_locations(rgb, model='hog')
            # compute the facial embedding for the face
            encodings = face_recognition.face_encodings(rgb, boxes)
            # loop over the encodings
            for encoding in encodings:
                knownEncodings.append(encoding)
                knownNames.append(name)
        # save emcodings along with their names in dictionary data
        data = {"encodings": knownEncodings, "names": knownNames}
        # use pickle to save data into a file for later use
        f = open("face_enc", "wb")
        f.write(pickle.dumps(data))
        f.close()
    
    
    def train_(self):
        cascPathface = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
        # load the harcaascade in the cascade classifier
        faceCascade = cv2.CascadeClassifier(cascPathface)
        # load the known faces and embeddings saved in last file
        data = pickle.loads(open('face_enc', "rb").read())
        print("Streaming started")
        video_capture = cv2.VideoCapture(self.t3.get())
      
                
        # loop over frames from the video file stream
        while True:
            # grab the frame from the threaded video stream
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray,
                                                 scaleFactor=1.1,
                                                 minNeighbors=5,
                                                 minSize=(60, 60),
                                                 flags=cv2.CASCADE_SCALE_IMAGE)
    
            # convert the input frame from BGR to RGB
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # the facial embeddings for face in input
            encodings = face_recognition.face_encodings(rgb)
            names = []
            # loop over the facial embeddings incase
            # we have multiple embeddings for multiple fcaes
            for encoding in encodings:
                # Compare encodings with encodings in data["encodings"]
                # Matches contain array with boolean values and True for the embeddings it matches closely
                # and False for rest
                matches = face_recognition.compare_faces(data["encodings"],
                                                         encoding)
                # set name =inknown if no encoding matches
                name = "Unknown"
                # check to see if we have found a match
                if True in matches:
                    # Find positions at which we get True and store them
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}
                    # loop over the matched indexes and maintain a count for
                    # each recognized face face
                    for i in matchedIdxs:
                        # Check the names at respective indexes we stored in matchedIdxs
                        name = data["names"][i]
                        # increase count for the name we got
                        counts[name] = counts.get(name, 0) + 1
                    # set name which has highest count
                    name = max(counts, key=counts.get)
    
                # update the list of names
                names.append(name)
                # loop over the recognized faces
                for ((x, y, w, h), name) in zip(faces, names):
                    # rescale the face coordinates
                    # draw the predicted face name on the image
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                                0.75, (0, 255, 0), 2)
            cv2.imshow("Frame", frame)
    
            if cv2.waitKey(33) == 27:
                break
        video_capture.release()
        cv2.destroyAllWindows()

   
root=Tk()

ob=Login(root)
img = PhotoImage(file='new1.png')
Label(root,width=350,height=400,image=img,border=0,bg='white').place(x=30,y=50)
root.mainloop()