import os
from tkinter import Image, messagebox
import numpy as np
import cv2
from tkinter import *
from PIL import Image
import shutil

# class sign_up_page:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("420x200")
#         self.root.title("To sign up")

        
#         btn_update = Button(self.root, text="update", activebackground='#df2121',command=def_train, fg='black', bg='#aa5656', height=1,
#                             width=12, font=('segoe UI bold', 13, 'italic'))
#         btn_update.grid(row=0, column=0, padx=30, pady=10)
class Train:
    def def_train():
        img_dir= ('cam_cap')
        self.createFolder(img_dir)
        path= [os.path.join(img_dir, file) for file in os.listdir(img_dir)]
        
        faces = []
        ids= []
        idx= []
        for imag in path:
            img= Image.open(imag).convert('L')
        # img = cv2.imread(f'{path}/{img}')
            imgnp = np.array(img, 'uint8') 
            id= int(os.path.split(imag)[-1].split('.')[1])
            faces.append(imgnp)
            ids.append(id)            
            cv2.imshow("training", imgnp)
            cv2.waitKey(1)== 13
        idx= np.array(ids)

        #   train classifier 
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, idx)
        clf.write("Trainner.xml")
        cv2.destroyAllWindows()
        self.deleteFolder(img_dir)

        messagebox.showinfo("RESULT", "trained the image")

    def createFolder(folder_path):
        try:
            # Check if the folder already exists
            if not os.path.exists(folder_path):
                # Create the folder
                os.makedirs(folder_path)
                print(f"Folder '{folder_path}' created successfully!")
            else:
                print(f"Folder '{folder_path}' already exists.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def deleteFolder(folder_path):
        try:
            # Check if the folder exists
            if os.path.exists(folder_path):
                # Delete the folder and its contents
                shutil.rmtree(folder_path)
                print(f"Folder '{folder_path}' deleted successfully!")
            else:
                print(f"Folder '{folder_path}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")


# if __name__ == "__main__":
#     root = Tk()
#     obj = sign_up_page(root)
#     root.mainloop()
