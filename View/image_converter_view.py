import os
import tkinter as tk

from View.Components.insert_password_component import InserPasswordComponent
from View.Components.upload_image_component import UploadImageComponent

class ImageConverterView(tk.Tk):
    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.title("Image Password Generator")
        self.geometry("700x200")
        self.file_name = tk.StringVar(value=f"No file selected")
    
    def encrypt_window(self):
        self.title_label = tk.Label(self, text="pwdGen", justify=tk.CENTER)
        self.title_label.grid(row=0, column=0, columnspan=6, sticky=tk.EW)
        
        for col in range(6):
            self.grid_columnconfigure(col, weight=1)
            
        self.upload_image_view = UploadImageComponent(
            parent=self,
            controller=self.controller,
            file_name_var=self.file_name
        ).grid(row=1,column=0,sticky=tk.NSEW)
        
        self.insert_password_view = InserPasswordComponent(
            parent=self,
            controller=self.controller
        ).grid(row=2,column=0,sticky=tk.NSEW)
        
    def update_file_name(self, file_name):
        self.file_name.set(os.path.basename(file_name))
    