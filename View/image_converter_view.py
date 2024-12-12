import os
import tkinter as tk
from tkinter import Image, messagebox
from tkinter import ttk

from View.Components.decrypt_image_component import DecryptImageComponent
from View.Components.insert_password_component import InserPasswordComponent
from View.Components.upload_image_component import UploadImageComponent
from View.Helper.ClipboardHelper import ClipboardHelper

class ImageConverterView(tk.Tk):
    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.title("Image Password Generator")
        self.geometry("700x200")
        self.resizable(False,False)
        self.file_name = tk.StringVar(value=f"No file selected")
        self.top_padding = 10
        self.side_padding = 35
        self.bg_color = "#1C1C3C"
        self.font_color = "#32CD32"
        self.configure(bg=self.bg_color)
    
    def encrypt_window(self):
            
        column_weights = [5, 1, 1, 1, 1, 2, 2]

        row_weights = [1, 2] 

        for i in range(7):
            self.grid_columnconfigure(index=i, weight=column_weights[i])
        for i in range(2):
            self.grid_rowconfigure(index=i, weight=row_weights[i])

        UploadImageComponent(
            parent=self,
            controller=self.controller,
            file_name_var=self.file_name,
            bg_color=self.bg_color,
            font_color=self.font_color
        ).grid(row=0, column=0, columnspan=5, sticky=tk.NSEW, pady=self.top_padding, padx=self.side_padding)

        InserPasswordComponent(
            parent=self,
            controller=self.controller,
            bg_color=self.bg_color,
            font_color=self.font_color
        ).grid(row=1, column=0, columnspan=5, sticky=tk.NSEW, pady=self.top_padding, padx=self.side_padding)

        DecryptImageComponent(
            parent=self, 
            controller=self.controller,
            bg_color=self.bg_color
        ).grid(row=0, column=5, rowspan=2, sticky=tk.NSEW, pady=self.top_padding, padx=self.side_padding) 

    def show_success_window(self,key):
        success_window = tk.Toplevel()
        success_window.title("Success")
        success_window.geometry("300x150")
        success_window.resizable(False, False)
    
        success_window.grab_set()

        def on_close():
            if messagebox.askyesno("Warning","If you close this window you will lose the decrypt key permanently. Are you sure?"):
                success_window.destroy()
        
        success_window.protocol("WM_DELETE_WINDOW", on_close)
        
        tk.Label(success_window, text="Decrypt key generated", font=("Arial", 12)).pack(pady=20)
        tk.Button(success_window, text="Download key", command=lambda:self.controller.download_key_txt(key.decode(),success_window)).pack(pady=10)
        
    def insert_decrypt_token_window(self):
        decrypt_token_window = tk.Toplevel()
        decrypt_token_window.title("Insert decrypt token")
        decrypt_token_window.geometry("300x150")
        decrypt_token_window.resizable(False, False)
        
        decrypt_token = tk.StringVar()
        
        decrypt_token_window.grab_set()
        
        tk.Label(decrypt_token_window, text="Insert decrypt token", font=("Arial", 12)).pack(pady=20)
        tk.Entry(decrypt_token_window, textvariable=decrypt_token, width=40).pack(pady=10)
        tk.Button(decrypt_token_window, text="Decrypt", command=lambda: decrypt_token_window.destroy()).pack(pady=10)
        
        decrypt_token_window.wait_window()
        return decrypt_token.get()
        
    def show_decrypted_pwd_window(self, pwd):
        decrypted_pwd_window = tk.Toplevel()
        decrypted_pwd_window.title("Decrypted password")
        decrypted_pwd_window.geometry("300x150")
        decrypted_pwd_window.resizable(False, False)
        
        decrypted_pwd_window.grab_set()
        
        tk.Label(decrypted_pwd_window, text="Decrypted password", font=("Arial", 12)).pack(pady=20)
        tk.Label(decrypted_pwd_window, text=pwd, font=("Arial", 12)).pack(pady=10)
        tk.Button(decrypted_pwd_window, text="Copy to clipboard", command=lambda: ClipboardHelper.copy(decrypted_pwd_window,pwd)).pack(pady=10)
        tk.Button(decrypted_pwd_window, text="Close", command=lambda: decrypted_pwd_window.destroy()).pack(pady=10)
        
    def update_file_name(self, file_name):
        self.file_name.set(os.path.basename(file_name))
    