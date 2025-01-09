from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from SignUpPage import SignUpPage
from Face import Face
from TakeComp import TakeComp
from ShowRegisteredUserData import ShowRegisteredUserData
from ShowAttendance import ShowAttendance

class Main:
    def __init__(self, root):
        self.root= root
        self.root.geometry("1000x520")
        self.root.title("Attendence system")
        
        self.root.resizable(True, True)

        self.img= ImageTk.PhotoImage(file="bg_img/bg.jpg")
        Label(self.root, image=self.img).place(x= 0, y= 0, width=1920, height=1080)
        Label(self.root,text="Attendence Management System",font=("magneto", 38, "bold"),
                     bg="black", fg= "white").place(x= 40, y= 20)

        sign_up_frame= LabelFrame(self.root, text="For Registration form",font=("magneto", 13, "italic"),
                                fg="white", bg= "black",bd= 6, height= 150, width= 220).place(x= 40, y= 100)

        attend_frame= LabelFrame(self.root, text="For Making attendance",font=("magneto", 13, "italic"),
                                fg="white", bg= "black",bd= 6, height= 150, width= 250).place(x= 340, y= 100)
        
        reg_user= LabelFrame(self.root, text="Show Registered student",font=("magneto", 13, "italic"),
                                fg="white", bg= "black",bd= 6, height= 150, width= 250).place(x= 650, y= 100)

        btn_1= Button(sign_up_frame,text="REGISTER",font=("segoe UI bold", 13), bg= "blue", 
        activebackground="red",height= 2, width= 15, command=self.register1, fg= "white").place(x= 70, y= 150)

        btn_2= Button(attend_frame,text="To make attendence",font=("segoe UI bold", 13), bg= "blue", 
        activebackground="red",height= 2, width= 20, command=self.attend, fg= "white").place(x= 360, y= 150)

        reg_btn= Button(reg_user,text="Show Users",font=("segoe UI bold", 13), bg= "blue", 
        activebackground="red",height= 2, width= 20, command=self.showUsers, fg= "white").place(x= 670, y= 150)

        help_frame= LabelFrame(self.root, text="HELP DESK",font=("magneto", 13, "italic"),
                                fg="white", bg= "black",bd= 6, height= 130, width= 470).place(x= 30, y= 300)
        
        show_attendance= LabelFrame(self.root, text="Show Attendance",font=("magneto", 13, "italic"),
                                fg="white", bg= "black",bd= 6, height= 130, width= 250).place(x= 650, y= 300)

        btn_3= Button(help_frame,text="contact for help",font=("segoe UI bold", 13, "bold"), bg= "blue", 
        activebackground="red",height= 2, width= 18, fg= "white").place(x= 55, y= 340)

        btn_4= Button(help_frame,text="Enter Written comment",font=("segoe UI bold", 13), bg= "blue", 
        activebackground="red", command=self.compl, height= 2, width= 21, fg= "white").place(x= 255, y= 340)

        btn_close= Button(self.root, text= "Close the Window", font=("Calibri",14,"bold"), bg= "orange",
                      command=self.close).pack(side='bottom', pady=20)

                      
        show_attendance_btn= Button(show_attendance,text="Show Attendance",font=("segoe UI bold", 13, "bold"), bg= "blue", 
        activebackground="red",command= self.ShowAttendance ,height= 2, width= 18, fg= "white").place(x= 680, y= 340)


    def close(self):
        self.root.destroy()
        self.root.quit()
            
    def register1(self):
        self.new_win= Toplevel(self.root)
        self.app= SignUpPage(self.new_win)
        
    def attend(self):
        self.new_win= Toplevel(self.root)
        self.app= Face(self.new_win)

    def compl(self):
        take_comp = TakeComp()
        take_comp.run()

    def showUsers(self):
        self.app= ShowRegisteredUserData()
        self.app.run()
        
    def ShowAttendance(self):
        self.app= ShowAttendance()
        self.app.run()

if __name__ == "__main__":
    root = Tk()
    obj = Main(root)
    root.mainloop()
    