import base64
from Model.Enum.ActionEnum import ActionEnum
from Model.Enum.FileTypeEnum import FileTypeEnum
from Model.Helper.FileHelper import FileHelper
from Model.image_converter_model import ImageConverterModel
from View.image_converter_view import ImageConverterView
from tkinter import filedialog,messagebox

class MainController:
    def __init__(self):
        self.image_converter_model = ImageConverterModel()
        self.image_converter_view = ImageConverterView(self)
        self.image_converter_view.encrypt_window()
        self.temp_file_path=None
        self.image=None
       
    def manage_file(self,action):
        
        if action == ActionEnum.SAVE:
            
            if self.temp_file_path is not None:
                self.image_converter_model.process_file(self.temp_file_path,ActionEnum.DELETE)
                pass
            
            file_path = FileHelper.get_file(FileTypeEnum.IMG)
            
            try:
                self.temp_file_path = self.image_converter_model.process_file(file_path,action)
                if self.temp_file_path is None:
                    raise RuntimeError("Error processing file")
                
                self.image_converter_view.update_file_name(file_path)
            except RuntimeError as e:
                messagebox.showerror("Error", str(e))
                
        if action == ActionEnum.DELETE:
            try:
                self.image_converter_model.process_file(self.temp_file_path,action)
                self.image_converter_view.update_file_name("No file selected")
            except RuntimeError as e:
                messagebox.showerror("Error", str(e))
        
    def encrypt_image_with_pwd(self,password):
        if self.temp_file_path is None:
            messagebox.showerror("Error", "No file selected")
            return

        if not password or password.strip() == "":
            messagebox.showerror("Error", "No password entered")
            return

        key = self.image_converter_model.encrypt_image(password.strip())
        if key is not None:
            self.image_converter_view.show_success_window(key)
        
    def download_key_txt(self,key, success_window):
        if not key:
            messagebox.showerror("Error", "Key is empty")
            return
        file_path = FileHelper.save_file(FileTypeEnum.TXT)
        try:
            with open(file_path, "w") as file:
                file.write(key)
            self.image_converter_model.process_file(self.temp_file_path,ActionEnum.DELETE)
            self.image_converter_view.update_file_name("No file selected")
            success_window.destroy()
                                
        except Exception as ex:
            messagebox.showerror("Error", f"Failed to save key: {str(ex)}")
        
    def get_encrypted_img(self):
        file_path = FileHelper.get_file(FileTypeEnum.IMG)
        if file_path is None:
            return

        decrypt_token = self.image_converter_view.insert_decrypt_token_window()
        if decrypt_token is None or decrypt_token.strip() == "":
            messagebox.showerror("Error", "You must insert a valid decrypt token")
            return
        
        decryped_pwd = self.image_converter_model.decrypt_image(file_path, decrypt_token)
        if decryped_pwd is None:
            messagebox.showerror("Error", f"Error decrypting image")
            return
        
        self.image_converter_view.show_decrypted_pwd_window(decryped_pwd)
        
    def execute(self):
        self.image_converter_view.mainloop()
    