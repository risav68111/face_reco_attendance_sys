from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
from tkinter import messagebox
import mysql.connector
from mysql.connector import connection
import cv2
from Train import Train
import os

class SignUpPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("840x400")
        self.root.title("To sign up")

        #    ^^^^^^^^^^^^ Variables declaring   ^^^^^^^^^^^^^^^^^^^
        var_name = StringVar(self.root)
        var_roll = StringVar(self.root)
        var_reg = IntVar(self.root)
        var_phone = StringVar(self.root)
        var_email = StringVar(self.root)
        var_dep = StringVar(self.root)
        var_sem = StringVar(self.root)
        var_day = IntVar(self.root)
        var_month = IntVar(self.root)
        var_year = IntVar(self.root)
        var_sex = StringVar(self.root)
        var_photo = BooleanVar(self.root)

        # |||||||||||||||||||||||||   Frames |||||||||||||||||||||||||||||

        main_frame = Label(self.root, bd=0, width=1950, height=1900, bg='#141414').place(x=0, y=0)
        sign_up_F = LabelFrame(self.root, width=860, height=420, bd=2, text="Fill below details to sign up",
                               font=("magneto", 16, 'underline'), fg="#f0f8ff", bg="#141414")
        sign_up_F.place(x=0, y=0)

        form_F = LabelFrame(self.root, bd=1, bg='#141414', relief=RIDGE)
        form_F.place(x=4, y=30, width=599, height=240)

        form_F0 = LabelFrame(self.root, bd=1, bg='#141414', relief=RIDGE)
        form_F0.place(x=454, y=30, width=400, height=240)

        form_F1 = LabelFrame(self.root, bd=1, bg='#141414', relief=RIDGE)
        form_F1.place(x=584, y=144, width=200, height=30)

        form_F2 = LabelFrame(self.root, bd=1, bg='#141414', relief=RIDGE)
        form_F2.place(x=584, y=234, width=96, height=28)

        frame_1 = LabelFrame(self.root, bd=1, bg='#141414', relief=RIDGE)
        frame_1.place(x=8, y=275, width=846, height=60)

        # frame_2= LabelFrame(self.root, bd= 1, bg= '#141414',text= 'Search your detail', font=
        #                       ("magneto", 14, 'underline'),fg= "#f0f8ff", relief=RIDGE)
        # frame_2.place(x= 4, y= 340, height= 80, width= 850)

        # frame_3= LabelFrame(self.root, bd= 1, bg= '#141414',fg= "#f0f8ff", relief=RIDGE)
        # frame_3.place(x= 4, y= 425, height= 380, width= 1200)

        #  ************   name fill **************
        Label(form_F, text="Name", font=("segoe UI bold", 13, 'italic'), fg='#f0f8ff', bd=0, 
                     bg="#141414").grid(row=0, column=0, padx=5, pady=10)
        name_entry = Entry(form_F, textvariable=var_name, width=40)
        name_entry.grid(row=0, column=1, padx=5, pady=10)

        #  ************   rollno fill **************
        Label(form_F, text="Roll no.", font=("segoe UI bold", 13, 'italic'), fg='#f0f8ff',
         bd=0, bg="#141414").grid(row=1, column=0, padx=5, pady=0)
        rollno_entry = Entry(form_F, textvariable=var_roll, width=30).grid(row=1, column=1, padx=5, pady=10)

        #  ************   reg fill **************
        Label(form_F, text="Registration no.", font=("segoe UI bold", 13, 'italic'), fg='#f0f8ff', bd=0,
              bg="#141414").grid(row=2, column=0, padx=5, pady=10)
        reg_entry = Entry(form_F, textvariable=var_reg, width=30).grid(row=2, column=1, padx=5, pady=10)

        #  ************   phone fill **************
        Label(form_F, text="Phone No.", font=("segoe UI bold", 13, 'italic'), fg='#f0f8ff', bd=0, bg="#141414").grid(
            row=3, column=0, padx=5, pady=10)
        phone_entry = Entry(form_F, textvariable=var_phone, width=40).grid(row=3, column=1, padx=5, pady=10)

        #  ************   email fill **************
        Label(form_F, text="Email", font=("segoe UI bold", 13, 'italic'), fg='#f0f8ff', bd=0, 
                   bg="#141414").grid(row=4, column=0, padx=5, pady=10)
        email_entry = Entry(form_F, textvariable=var_email, width=40).grid(row=4, column=1, padx=5, pady=10)

        #   *************** Dropdown menu options list ************

        opt_dep = ['Computer Application', 'IT', 'Physics', 'chemistry', 'micro bio']
        var_dep.set('Select department')

        opt_sem = list(range(1, 7))
        var_sem.set('X')

        opt_day = list(range(1, 32))
        var_day.set('XX')

        opt_month = list(range(1, 13))
        var_month.set('XX')

        opt_year = list(range(1950, 2015))
        var_year.set('XXXX')

        opt_sex = ['male', 'female', 'trans']
        var_sex.set('male')

        # FFFFFFFFFFFFFF    FONT  FFFFFFFFFFFFFFFFFFFFF
        drop_font = font.Font(family='segoe UI semibold', size=10)
        drop_font8 = font.Font(family='segoe UI bold', size=8)

        #   OOOOOOOOOOOOOOOOOOO   Option menu   OOOOOOOOOOOOOOOO
        Label(form_F0, text='Department', font=('segoe UI bold', 13, 'italic'), fg='#f0f8ff',
                bd=0, bg="#141414").grid(row=0, column=0, padx=5, pady=10)
        opt_dep = OptionMenu(form_F0, var_dep, *opt_dep)
        menu = root.nametowidget(opt_dep.menuname)
        menu.config(font=drop_font8)
        opt_dep.config(font=drop_font)
        opt_dep.grid(row=0, column=1, padx=5, pady=10)

        #    %%%%%%%%%%%%    Semester %%%%%%%%%%%%%%%%%%%%%%
        Label(form_F0, text='Semester', font=('segoe UI bold', 13, 'italic'), fg='#f0f8ff', bd=0,
                     bg="#141414").grid(row=1, column=0, padx=5, pady=10)
        sem = OptionMenu(form_F0, var_sem, *opt_sem)
        menu = root.nametowidget(sem.menuname)
        menu.config(font=drop_font8)
        sem.config(font=drop_font)
        sem.grid(row=1, column=1, padx=5, pady=10)

        #  &&&&&&&&&&&&&&&   DATE OF BIRTH &&&&&&&&&&&&&&
        Label(form_F0, text='Date of birth', font=('segoe UI bold', 13, 'italic'), fg='#f0f8ff', bd=0,
              bg="#141414").grid(row=2, column=0, padx=5, pady=10)

        day = OptionMenu(form_F1, var_day, *opt_day)
        menu0 = root.nametowidget(day.menuname)
        menu0.config(font=drop_font8)
        day.config(font=drop_font)
        day.grid(row=0, column=0, padx=0, pady=0)

        month = OptionMenu(form_F1, var_month, *opt_month)
        menu1 = root.nametowidget(month.menuname)
        menu1.config(font=drop_font8)
        month.config(font=drop_font)
        month.grid(row=0, column=1, padx=5, pady=0)

        year = OptionMenu(form_F1, var_year, *opt_year)
        menu2 = root.nametowidget(year.menuname)
        menu2.config(font=drop_font8)
        year.config(font=drop_font)
        year.grid(row=0, column=3, padx=0, pady=0)

        Label(form_F0, text='sex', font=('segoe UI bold', 13, 'italic'), fg='#f0f8ff',
                   bd=0, bg="#141414").grid(row=3, column=0, padx=5, pady=10)
        sex = OptionMenu(form_F0, var_sex, *opt_sex)
        menu3 = root.nametowidget(sex.menuname)
        menu3.config(font=drop_font8)
        sex.config(font=drop_font)
        sex.grid(row=3, column=1, padx=0, pady=0)

        #  ^^^^^^^^^^^^^^^^^  for photo sample   ^^^^^^^^^^^^^^^^^^^^^^^
        Label(form_F0, text='photo sample', font=('segoe UI bold', 13, 'italic'), fg='#f0f8ff', bd=0,
              bg="#141414").grid(row=4, column=0, padx=5, pady=10)

        btn_1 = Radiobutton(form_F2, text='yes', variable=var_photo, value='Yes').grid(row=0, column=0)

        btn_2 = Radiobutton(form_F2, text='no', variable=var_photo, value='no').grid(row=0, column=1, padx=5)

        def start():
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    face_cropped = img[y:y + h, x:x + h]
                    return face_cropped

            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if not ret:
                    messagebox.showerror('error', 'failed to grab image')
                    break
                if face_cropped(my_frame) is not None:
                    img_id += 1
                face = cv2.resize(my_frame,(600, 600), interpolation = cv2.INTER_AREA)
                file_name_path = "cam_cap/user." +str(var_roll.get()) + "." + str(img_id) + ".jpg"
                cv2.imwrite(file_name_path, my_frame)
                cv2.putText(face, 'face detected', (80, 80), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                if ret:
                    cv2.imshow("Crop", face)
                    if cv2.waitKey(1) == 13 & 0xff or int(img_id) == 100:
                        break
            cap.release()
            cv2.destroyAllWindows()
            Train.def_train()
            
        btn_3 = Button(form_F0, text="Enter sample", command=start).grid(row=4, column=3)

        # &&&&&&&&&&&&&&&&&&&&&&   to reset form
        def reset_data():
            var_name.set("")
            var_roll.set('')
            var_reg.set('')
            var_phone.set("")
            var_email.set('')
            var_dep.set('Select department')
            var_sem.set('X')
            var_day.set('XX')
            var_month.set('XX')
            var_year.set("XXXX")
            var_sex.set('male')

        # sign up#     *******************Adding data to mySQL 

        user= 'risav'
        user_pass= '1234'
        database_name='FACE_RECO_SYS_DB'
        def add_data():
            if var_name.get() == "" or var_roll.get() == "" or var_phone.get() == "" or var_email.get() == '':
                messagebox.showerror("ERROR!! ", "Fill all the details")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost', username=user, password=user_pass, database=database_name)
                    # conn = connection.MySQLConnection(user = user, host = 'localhost', database = database_name)
                    my_cursor = conn.cursor()
                    my_cursor.execute('INSERT INTO user_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                        var_name.get(),
                        var_roll.get(),
                        var_reg.get(),
                        var_phone.get(),
                        var_email.get(),
                        var_dep.get(),
                        var_sem.get(),
                        var_day.get(),
                        var_month.get(),
                        var_year.get(),
                        var_sex.get(),
                        var_photo.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('Sucess', 'all data added.')
                except mysql.connector.Error as err:
                    messagebox.showerror("Database Error", f"Error: {err}")
                except Exception as es:
                    messagebox.showerror("Unexpected Error", f"Error: {es}")


        # &&&&&&&&&&&&    button &&&&&&&&&&&
        btn_save = Button(frame_1, text="sign up", command=add_data, activebackground='#df2121', fg='black',
                          bg='#aa5656', height=1, width=12, font=('segoe UI bold', 13, 'italic'))
        btn_save.grid(row=0, column=0, padx=30, pady=10)

        btn_update = Button(frame_1, text="update", activebackground='#df2121', fg='black', bg='#aa5656', height=1,
                            width=12, font=('segoe UI bold', 13, 'italic'))
        btn_update.grid(row=0, column=1, padx=30, pady=10)

        btn_delete = Button(frame_1, text="delete", activebackground='#df2121', fg='black', bg='#aa5656', height=1,
                            width=12, font=('segoe UI bold', 13, 'italic'))
        btn_delete.grid(row=0, column=2, padx=30, pady=10)

        btn_reset = Button(frame_1, text="reset", activebackground='#df2121', fg='black', bg='#aa5656', height=1,
                           width=12, command=reset_data, font=('segoe UI bold', 13, 'italic'))
        btn_reset.grid(row=0, column=3, padx=30, pady=10)

        # #   $$$$$$$$$$$$$$$$$$$$$$   search bar   $$$$$$$$$$$$$$$$$$$$$$$$$$$$

        # Label(frame_2, text='enter roll no.', font= ("segoe UI semibold", 13,'italic'), fg= '#f0f8ff',bd= 0, bg="#141414").grid(row=0, column= 0, padx= 5, pady=10)
        # serch_entry= Entry(frame_2, textvariable=var_roll, width= 30,).grid(row= 0, column= 1,padx= 5, pady= 10)

        # search_btn= Button(frame_2, text="Search", font=('segoe UI bold', 13), activebackground= '#df2121',fg= 'black', bg= '#aa5656', height=1, width=12)
        # search_btn.grid(row= 0, column= 3)

        # showall= Button(frame_2, text= 'show all', font= ('segoe UI bold', 13), activebackground= '#df2121',fg= 'black', bg= '#aa5656', height=1, width=12)
        # showall.grid(row= 0, column= 4, padx= 40)

        # # ************************  canavas
        # canvas_1= Canvas(frame_3)
        # canvas_1.pack(side= LEFT, fill= BOTH, expand= 1)

        # scr_x= ttk.Scrollbar(frame_3, orient= VERTICAL, command= canvas_1.yview)
        # scr_x.pack(side= RIGHT, fill= Y)

        # canvas_1.configure(yscrollcommand=scr_x.set)
        # canvas_1.bind('<Configure>', lambda e: canvas_1.configure(scrollregion= canvas_1.bbox("all")))

        # frame_x= LabelFrame(canvas_1)

        # canvas_1.create_window((0,0), window= frame_x, anchor= 'nw')

        # #    &&&&&&&&&&&&&&&&&&&&&&    table showing detail
        # scroll_x= tk.Scrollbar(frame_3, orient=HORIZONTAL)
        # scroll_y= tk.Scrollbar(frame_3, orient= VERTICAL)

        # table_1T= ttk.Treeview(frame_3)
        # table_1T['column']=("name", "rollno", "regno", "phone","email", "dep", "sem", "dob", "sex", "photo sample")
        # table_1T.column("#0",anchor=W, width= 0, minwidth= 0)
        # table_1T.column("name",anchor=W, width= 120)
        # table_1T.column("rollno",anchor=W, width= 70)
        # table_1T.column("regno",anchor=W, width= 70)
        # table_1T.column("phone",anchor=W, width= 120)
        # table_1T.column("email",anchor=W, width= 120)
        # table_1T.column("dep",anchor=W, width= 120)
        # table_1T.column("sem",anchor=W, width= 80)
        # table_1T.column("dob",anchor=W, width= 100)
        # table_1T.column("sex",anchor=W, width= 80)
        # table_1T.column("photo sample",anchor=W, width= 60)

        # table_1T.insert(parent='', index='end', iid=0, text= "Parent")

        # scroll_x.config(command= table_1T.xview)
        # scroll_y.config(command= table_1T.yview)

        # scroll_x.pack(side= BOTTOM, fill= X)
        # scroll_y.pack(side= RIGHT, fill=Y)

        # table_1T.heading('#0', text='S.No. ',anchor=W)
        # table_1T.heading('name', text='Name',anchor=W)
        # table_1T.heading('rollno', text='RollNo',anchor=W)
        # table_1T.heading('regno', text='RegNo',anchor=W)
        # table_1T.heading('phone', text='phone no',anchor=W)
        # table_1T.heading('email', text='email',anchor=W)
        # table_1T.heading('dep', text='department',anchor=W)
        # table_1T.heading('sem', text='sem',anchor=W)
        # table_1T.heading('dob', text='dob',anchor=W)
        # table_1T.heading('sex', text='sex',anchor=W)
        # table_1T.heading('photo sample', text='sample',anchor=W)

        # # table_1T["show"]= "heading"
        # table_1T.pack(fill=BOTH,side="left", expand=1)

        def close():
            self.root.destroy()
            self.root.quit()
            
        Button(self.root, text= "Close the Window", font=("Calibri",14,"bold"),
                      command=close).pack(side='bottom', pady=10)

if __name__ == "__main__":
    root = Tk()
    obj = sign_up_page(root)
    root.mainloop()
