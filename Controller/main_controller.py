from Model.Enum.ActionEnum import ActionEnum
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
            
            file_path = filedialog.askopenfilename(
                filetypes=[("Image files", "*.png *.jpg *.jpeg")],
            )
            if not file_path:
                messagebox.showerror("Error", "No file selected")
                return
            
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

        self.image_converter_model.encrypt_image(password.strip())
        
    def execute(self):
        self.image_converter_view.mainloop()
    