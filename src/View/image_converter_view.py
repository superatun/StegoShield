from ctypes import windll
import os
import tkinter as tk
from tkinter import messagebox

from src.View.Components.decrypt_image_component import DecryptImageComponent
from src.View.Components.insert_password_component import InserPasswordComponent
from src.View.Components.upload_image_component import UploadImageComponent
from src.View.Helper.ClipboardHelper import ClipboardHelper
from src.View.Helper.Versioning import Versioning

class ImageConverterView(tk.Tk):
    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.version = Versioning.get_version()
        self.title(f"StegoShield v{self.version}")
        self.geometry("700x200")
        self.resizable(False,False)
        self.iconbitmap("src\\View\\resources\\Ico\\unlock_icon.ico")
        windll.shell32.SetCurrentProcessExplicitAppUserModelID("StegoShieldApp")
        self.iconbitmap("src\\View\\resources\\Ico\\unlock_icon.ico")
        self.file_name = tk.StringVar(value=f"No file selected")
        self.top_padding = 10
        self.side_padding = 35
        self.bg_color = "#2C3E50"
        self.font_color = "#ECF0F1",
        self.btn_bg = "#1ABC9C"
        self.btn_fontcolor = "#FFFFFF"
        self.pwd_box_bg = "#ECF0F1"
        self.font_family = "Roboto"
        self.font_size = 12
        self.configure(bg=self.bg_color)
    
    def encrypt_window(self):
            
        column_weights = [1, 4, 2]

        row_weights = [1, 1]

        for i in range(len(column_weights)):
            self.grid_columnconfigure(index=i, weight=column_weights[i])

        for i in range(len(row_weights)):
            self.grid_rowconfigure(index=i, weight=row_weights[i])

        UploadImageComponent(
            parent=self,
            controller=self.controller,
            file_name_var=self.file_name,
            bg_color=self.bg_color,
            font_color=self.font_color,
            bg_btn=self.btn_bg,
            btn_fontcolor=self.btn_fontcolor,
            font_family=self.font_family,
            font_size=self.font_size
        ).grid(row=0, column=0, columnspan=5, sticky=tk.NSEW, pady=self.top_padding, padx=self.side_padding)

        InserPasswordComponent(
            parent=self,
            controller=self.controller,
            bg_color=self.bg_color,
            font_color=self.font_color,
            btn_bg=self.btn_bg,
            btn_fontcolor=self.btn_fontcolor,
            pwd_box_bg=self.pwd_box_bg,
            font_family=self.font_family,
            font_size=self.font_size
        ).grid(row=1, column=0, columnspan=5, sticky=tk.NSEW, pady=self.top_padding, padx=self.side_padding)

        DecryptImageComponent(
            parent=self, 
            controller=self.controller,
            bg_color=self.bg_color,
            font_color=self.font_color,
            font_family=self.font_family,
            font_size=self.font_size,
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
        tk.Button(success_window, text="Download key", command=lambda:self.controller.download_key_txt(key,success_window)).pack(pady=10)
        
    def insert_decrypt_token_window(self):
        decrypt_token_window = tk.Toplevel()
        decrypt_token_window.title("Insert decrypt token")
        decrypt_token_window.geometry("300x150")
        decrypt_token_window.resizable(False, False)
        decrypt_token = tk.StringVar()
        decrypt_token_window.grab_set()

        self.window_closed_with_x = False

        def on_close():
            self.window_closed_with_x = True
            decrypt_token_window.destroy()

        decrypt_token_window.protocol("WM_DELETE_WINDOW", on_close)

        tk.Label(decrypt_token_window, text="Insert decrypt token", font=("Arial", 12)).pack(pady=20)
        tk.Entry(decrypt_token_window, textvariable=decrypt_token, width=40).pack(pady=10)
        tk.Button(decrypt_token_window, text="Decrypt", command=lambda: decrypt_token_window.destroy()).pack(pady=10)

        decrypt_token_window.wait_window()

        if self.window_closed_with_x:
            return None

        return decrypt_token.get()
        
    def show_decrypted_pwd_window(self, pwd):
        decrypted_pwd_window = tk.Toplevel()
        decrypted_pwd_window.title("Decrypted password")
        decrypted_pwd_window.geometry("300x150")
        decrypted_pwd_window.resizable(False, False)
        decrypted_pwd_window.grab_set()
        
        def on_close():
            decrypted_pwd_window.destroy()

        decrypted_pwd_window.protocol("WM_DELETE_WINDOW", on_close)
        
        tk.Label(decrypted_pwd_window, text="Decrypted password", font=("Arial", 12)).pack(pady=20)
        tk.Label(decrypted_pwd_window, text=pwd, font=("Arial", 12)).pack(pady=10)
        tk.Button(decrypted_pwd_window, text="Copy to clipboard", command=lambda: ClipboardHelper.copy(decrypted_pwd_window,pwd)).pack(pady=10)
        tk.Button(decrypted_pwd_window, text="Close", command=lambda: decrypted_pwd_window.destroy()).pack(pady=10)
        
    def update_file_name(self, file_name):
        self.file_name.set(os.path.basename(file_name))
    