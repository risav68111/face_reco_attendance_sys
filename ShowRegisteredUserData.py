from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
# import mysql.connector
from mysql.connector import connection

class ShowRegisteredUserData :
    def run(self):
        self.root= Tk()
        self.root.geometry("1400x500")
        self.root.title("Registered Users")
        self.root.resizable(True, True)
        self.createUI()
        self.root.mainloop()

    def fetchData(self):
        user= 'risav'
        user_pass= '1234'
        database_name='FACE_RECO_SYS_DB'
        try:
            # conn = mysql.connector.connect(host='localhost', username=user, password=user_pass, database=database_name)
            conn = connection.MySQLConnection(user = user, host = 'localhost', database = database_name)
            my_cursor = conn.cursor()
            query= "SELECT * FROM user_data"
            my_cursor.execute(query)
            data= my_cursor.fetchall()
            conn.commit()
            conn.close()
            print("Data fetched from dataabase.")
            messagebox.showinfo('Sucess', 'all data Fetched.')
            return data
        except Exception as es:
            print(f"error ", es)
            messagebox.showerror(f"ERROR", {str(es)})
    
    def dataClean(self):
        data = self.fetchData()
        processed_data = []
        for row in data:
            name, roll_no, reg_no, phone, email, dep, sem, day, month, year, sex, photo = row
            dob = f"{day}-{month}-{year}"  # Combine into a single string
            processed_data.append((name, roll_no, reg_no, phone, email, dep, sem, dob, sex))
            
        # print(processed_data)
        return processed_data

    def createUI(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=1)

        # Create a Canvas
        canvas = tk.Canvas(frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add a Scrollbar to the Canvas
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create another frame inside the canvas
        table_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=table_frame, anchor="nw")

        # Add Table Headers
        headers = [ "Name", "Roll No", "Registeration Name", "Phone No.", "Email", "Department", "Semester", "Date Of Birth", "Sex"]
        for col, header in enumerate(headers):
            tk.Label(table_frame, text=header, font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=15).grid(row=0, column=col)

        # Fetch and Display Data
        data = self.dataClean()
        for row_index, row in enumerate(data, start=1):
            for col_index, value in enumerate(row):
                tk.Label(table_frame, text=value, font=("Arial", 10), borderwidth=1, relief="solid", width=15).grid(row=row_index, column=col_index)

        # Configure the canvas scroll region
        table_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        
        btn_close= Button(self.root, text= "Close the Window", font=("Calibri",14,"bold"), 
                      command=self.close).pack(side='bottom', pady=20)
    
    def close(self):
        self.root.destroy()
        self.root.quit()




# root = Tk()
# run_app= ShowRegisteredUserData()
# run_app.run()


# run_app.dataClean()
