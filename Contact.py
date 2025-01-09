from tkinter import *
from tkinter import ttk
import tkinter as tk
import webbrowser

class ContactDetail:
    def run(self):
        self.root= Tk()
        self.root.geometry("500x400")
        self.root.title("Compalint box")
        self.root.resizable(False, False)
        self.createUI()
        self.root.mainloop()
    
    def createUI(self):

        Frame(self.root, bg= 'white',height= 1080, width= 1920 ).place(x=0, y= 0)

        contact_lbl= Label(self.root, text='Contact No : 1234576890 ', font= ("segoe UI semibold", 20,'italic'), fg= 'black',bd= 0, bg="white")
        contact_lbl.grid(row=1, column= 1, padx= 90, pady=30)

        email_btn= Label(self.root, text='Email: risav@mail.com ', font= ("segoe UI semibold", 20,'italic'), fg= 'black',bd= 0, bg="white")
        email_btn.grid(row=2, column= 1, padx= 90, pady=30)

        github_link_btn = Label(self.root, text="Click to visit my GitHub", fg="blue", cursor="hand2", font=("Arial", 20, "underline"))
        github_link_btn.grid(row=3, column= 1, padx= 90, pady=30)
        
        github_link_btn.bind("<Button-1>", lambda e: self.open_url())


    def open_url(self):
        webbrowser.open("https://www.github.com/risav68111")


run_app= ContactDetail()
run_app.run()