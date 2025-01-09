from tkinter import *
from tkinter import Tk, ttk,messagebox
import tkinter as tk
import mysql


class TakeComp:
    def run(self):
        self.root= Tk()
        self.root.geometry("530x580")
        self.root.title("Compalint box")
        self.root.resizable(False, False)
        self.createUI()
        self.root.mainloop()
    
    def createUI(self):
        
        self.var_name= StringVar(self.root)
        self.var_roll= StringVar(self.root)
        self.var_dep= StringVar(self.root)
        self.var_email= StringVar(self.root)
        self.var_complaint= StringVar(self.root)

        Frame(self.root, bg= 'gray',height= 1080, width= 1920 ).place(x=0, y= 0)
        
        Label(self.root, text= "Complaint window",font=("magneto", 26), bg= "black", fg= "white").place(x= 80, y= 10)
        
        # main_frame= LabelFrame(self.root, bg= "dark gray", bd= 1, height= 500, width= 500).place(x= 10, y= 58)

        # input_frame= Frame(self.root, bg= "gray", bd= 1, height= 150, width= 498).place(x= 12, y= 60)

        cmnt_frame= LabelFrame(self.root,text= 'enter your complaint in detail', font= ("segoe UI", 13), bg= "dark gray",
                                bd= 1, height= 350, width= 600).place(x= 0, y= 210)


        Label(self.root, text= "enter your name", font=("segoe UI ", 13), bg= "gray", bd= 3).place(x=14, y= 70)
        self.entry_name= Entry(self.root,textvariable=self.var_name, width= 30, bd= 2).place(x= 150, y= 70)

        Label(self.root, text= "enter your roll no. ", font=("segoe UI ", 13), bg= "gray", bd= 3).place(x=14, y= 103)
        self.entry_roll= Entry(self.root,textvariable=self.var_roll, width= 20, bd= 2).place(x= 150, y= 105)
        
        Label(self.root, text= "enter your department ", font=("segoe UI ", 13), bg= "gray", bd= 3).place(x=14, y= 138)
        self.entry_dep= Entry(self.root,textvariable=self.var_dep, width= 25, bd= 2).place(x= 190, y= 140)
        
        Label(self.root, text= "enter your email ", font=("segoe UI ", 13), bg= "gray", bd= 3).place(x=14, y= 168)
        self.entry_email= Entry(self.root, textvariable=self.var_email, width= 25, bd= 2).place(x= 150, y= 170)

        self.text_complaint= Text(self.root, width= 60, bd= 2, bg= "light gray")
        self.text_complaint.place(x= 14, y= 235, height= 200, width=490)



        Button(self.root,text="Submit", font=("segoe UI", 13), bg= "green", activebackground= "red", height= 1, width= 9,
                command=self.submit_complaint).place(x= 100, y= 470)
        
        Button(self.root,text="clear", font=("segoe UI", 13), bg= "green", activebackground= "red", height= 1, width= 9,
                command=self.clearInputs).place(x= 200, y= 470)
        
        Button(self.root,text="close", font=("segoe UI", 13), bg= "red", activebackground= "red", height= 1, width= 9, 
                command=self.close).place(x= 300, y= 470)
    
    
    def submit_complaint(self):
        # Extract inputs
        name = self.var_name.get()
        roll_no = self.var_roll.get()
        department = self.var_dep.get()
        email = self.var_email.get()
        complaint = self.text_complaint.get("1.0", END).strip()

        if not (name and roll_no and department and email ):
            print("All fields are required!")
            return

        print("Complaint Submitted:")
        print(f"Name: {name}")
        print(f"Roll No: {roll_no}")
        print(f"Department: {department}")
        print(f"Email: {email}")
        print(f"Complaint: {complaint}")

        if not name or not roll_no or not department or not email or not complaint:
            messagebox.showerror("Error", "All fields are required!")
        
        user= 'risav'
        user_pass= '1234'
        database_name='FACE_RECO_SYS_DB'
        try:
            conn = mysql.connector.connect( host="localhost", user=user, password=user_pass, database=database_name )
            cursor = conn.cursor()

            query = "INSERT INTO complaints (name, roll_no, department, email, complaint) VALUES (%s, %s, %s, %s, %s)"
            values = (name, roll_no, department, email, complaint)
            cursor.execute(query, values)
            conn.commit()

            # Show success message and clear fields
            messagebox.showinfo("Success", "Data uploaded successfully!")
            self.clearInputs()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


    def clearInputs(self):
        # Clear all input fields
        self.var_name.set("")
        self.var_roll.set("")
        self.var_dep.set("")
        self.var_email.set("")
        self.var_complaint.set("")

    def close(self):
        self.root.destroy()
        self.root.quit()



# run_app= TakeComp()
# run_app.run()


# if __name__ == "__main__":
#     root = Tk()
#     obj = take_comp(root)
#     root.mainloop()

