from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from main import sign_up_page
from face import face_reco_attend
from complaint import take_comp

class home:
    def __init__(self, root):
        self.root= root
        self.root.geometry("800x600")
        self.root.title("Attendence system")
        
        self.root.resizable(True, True)

        self.img= ImageTk.PhotoImage(file="bg_img/bg.jpg")
        Label(self.root, image=self.img).place(x= 0, y= 0, width=1920, height=1080)
        Label(self.root,text="Attendence Management System",font=("magneto", 38, "bold"),
                     bg="black", fg= "white").place(x= 40, y= 20)

        sign_up_frame= LabelFrame(self.root, text="For Registration form",font=("magneto", 13, "italic"),
                                fg="white", bg= "black",bd= 6, height= 180, width= 250).place(x= 30, y= 100)

        btn_1= Button(sign_up_frame,text="REGISTER",font=("segoe UI bold", 13), bg= "blue", 
        activebackground="red",height= 2, width= 15, command=self.register1, fg= "white").place(x= 80, y= 160)

        attend_frame= LabelFrame(self.root, text="For Making attendance",font=("magneto", 13, "italic"),
                                fg="white", bg= "black",bd= 6, height= 180, width= 250).place(x= 330, y= 100)

        btn_2= Button(attend_frame,text="To make attendence",font=("segoe UI bold", 13), bg= "blue", 
        activebackground="red",height= 2, width= 20, command=self.attend, fg= "white").place(x= 350, y= 160)
                            
        help_frame= LabelFrame(self.root, text="HELP DESK",font=("magneto", 13, "italic"),
                                fg="white", bg= "black",bd= 6, height= 130, width= 470).place(x= 30, y= 300)

        btn_3= Button(help_frame,text="contact for help",font=("segoe UI bold", 13, "bold"), bg= "blue", 
        activebackground="red",height= 2, width= 18, fg= "white").place(x= 55, y= 340)

        btn_4= Button(help_frame,text="Enter Written comment",font=("segoe UI bold", 13), bg= "blue", 
        activebackground="red",height= 2, width= 21, fg= "white").place(x= 255, y= 340)

        btn_close= Button(self.root, text= "Close the Window", font=("Calibri",14,"bold"), 
                      command=self.close).pack(side='bottom', pady=20)


    def close(self):
        self.root.destroy()
        self.root.quit()
            
    def register1(self):
        self.new_win= Toplevel(self.root)
        self.app= sign_up_page(self.new_win)
        
    def attend(self):
        self.new_win= Toplevel(self.root)
        self.app= face_reco_attend(self.new_win)

        
    def compl(self):
        self.new_win= Toplevel(self.root)
        self.app= take_comp(self.new_win)


if __name__ == "__main__":
    root = Tk()
    obj = home(root)
    root.mainloop()
    