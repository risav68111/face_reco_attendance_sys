from tkinter import *
from tkinter import ttk
import tkinter as tk

class ContactDetail:
    def run(self):
        self.root= Tk()
        self.root.geometry("530x580")
        self.root.title("Compalint box")
        self.root.resizable(False, False)
        self.createUI()
        self.root.mainloop()
    
    def createUI(self):

        Frame(self.root, bg= 'gray',height= 1080, width= 1920 ).place(x=0, y= 0)
        


run_app= ContactDetail()
run_app.run()