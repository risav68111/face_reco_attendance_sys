from tkinter import *
from tkinter import Tk
import tkinter as tk
import mysql

class take_comp:
    def __init__(self, root):
        self.root= root 
        self.root.geometry("530x580")
        self.root.title("Compalint box")

        Frame(self.root, bg= 'gray',height= 1080, width= 1920 ).place(x=0, y= 0)
        
        Label(self.root, text= "Complaint window",font=("magneto", 26), bg= "black", fg= "white").place(x= 60, y= 10)
        
        frame_1= LabelFrame(self.root, bg= "dark gray", bd= 1, height= 500, width= 500).place(x= 10, y= 58)

        min_frame_1= Frame(self.root, bg= "gray", bd= 1, height= 150, width= 498).place(x= 12, y= 60)

        frame_2= LabelFrame(frame_1,text= 'enter your complaint in detail', font= ("segoe UI", 13), bg= "dark gray",
                                bd= 1, height= 350, width= 500).place(x= 10, y= 210)


        Label(min_frame_1, text= "enter your name", font=("segoe UI ", 13), bg= "gray", bd= 3).place(x=14, y= 70)
        entry_name= Entry(frame_1, width= 30, bd= 2).place(x= 150, y= 70)

        Label(min_frame_1, text= "enter your roll no. ", font=("segoe UI ", 13), bg= "gray", bd= 3).place(x=14, y= 103)
        entry_roll= Entry(frame_1, width= 20, bd= 2).place(x= 150, y= 105)
        
        Label(min_frame_1, text= "enter your department ", font=("segoe UI ", 13), bg= "gray", bd= 3).place(x=14, y= 138)
        entry_dep= Entry(frame_1, width= 25, bd= 2).place(x= 190, y= 140)
        
        Label(min_frame_1, text= "enter your email ", font=("segoe UI ", 13), bg= "gray", bd= 3).place(x=14, y= 168)
        entry_email= Entry(frame_1, width= 25, bd= 2).place(x= 150, y= 170)

        
        text_compliant= Text(frame_2, width= 60, bd= 2, bg= "light gray").place(x= 14, y= 235, height= 200, width=490)

        Button(frame_2,text="Submit", font=("segoe UI", 13), bg= "green", activebackground= "red").place(x= 100, y= 470)

        Button(frame_2,text="clear", font=("segoe UI", 13), bg= "green", activebackground= "red").place(x= 200, y= 470)



if __name__ == "__main__":
    root = Tk()
    obj = take_comp(root)
    root.mainloop()