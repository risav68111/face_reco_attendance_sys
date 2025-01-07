from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import connection
from time import strftime
import cv2
import os
import numpy as np
from datetime import datetime


class Face:
    def __init__(self, root):
        self.root = root
        self.root.geometry("420x200")
        self.root.title("Attendance ")
        
        Label(self.root, text="To make attendance using face recognition",  height=1,
                            width=35, font=('segoe UI bold', 13, 'italic')).grid(row=0, column=0, padx=30, pady=10)
        btn_update = Button(self.root, text="Open Camera", activebackground='#df2121',command=faceReco, fg='black',
                     bg='#aa5656', height=1, width=12, font=('segoe UI bold', 13, 'italic'))
        btn_update.grid(row=1, column=0, padx=30, pady=10)

        Label(self.root, text="Press Q to close camera",  height=1,
                            width=35, font=('segoe UI bold', 13, 'italic')).grid(row=3, column=0, padx=30, pady=10)

def faceReco():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  
    recognizer.read("Trainner.xml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height
    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5,minSize = (int(minW), int(minH)), 
                    flags = cv2.CASCADE_SCALE_IMAGE)
        for(x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x+w, y+h), (10, 159, 255), 2)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            confidence= int(100*(1- conf/300))
            
            user= 'risav'
            user_pass= '1234'
            database_name='FACE_RECO_SYS_DB'
            try:
                # conn = mysql.connector.connect(host='localhost', username=user, password=user_pass, database=database_name)
                conn = connection.MySQLConnection(user = user, host = 'localhost', database = database_name)
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT name FROM user_data WHERE roll_no="+str(Id))
                nameSQL= my_cursor.fetchone()
                nameSQL= "+".join(nameSQL)
                # print(nameSQL)
                # print(Id)

                my_cursor.execute("SELECT dep FROM user_data WHERE roll_no="+str(Id))
                j= my_cursor.fetchone()[0]

                if confidence>80:
                    cv2.putText(im, f"name {nameSQL}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

                    with open("attend.csv", "r+", newline="\n") as f:
                        dataList= f.readlines()
                        name_list= []
                        for line in dataList:
                            entry= line.split((", "))
                            name_list.append(entry[0])
                        if((nameSQL not in name_list) and (Id not in name_list) and (j not in name_list)):
                            now = datetime.now()
                            d1= now.strftime("%d/ %m/ %Y")
                            dtStr= now.strftime("%H:%M:%S")
                            f.writelines(f"\n{nameSQL}, {Id}, {j}, {d1}, {dtStr}")

                else:
                    cv2.rectangle(im, (x, y),(x+w, y+h), (0, 0, 255), 2)
                    cv2.putText(im, "UNKNOWN", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

                # cord [x, y, w, h]
                conn.commit()
                conn.close()
            except Exception as es:
                    messagebox.showerror(f"ERROR", {str(es)})


        cv2.imshow('Attendance', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face(root)
    root.mainloop()