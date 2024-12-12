from tkinter import filedialog, messagebox

from Model.Enum.FileTypeEnum import FileTypeEnum

class FileHelper():
    
    @staticmethod
    def save_file(type):
        if type == FileTypeEnum.TXT:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt")],
                title="Save key as",
                initialfile="key.txt"
            )
            if not file_path:
                messagebox.showwarning("Cancelled", "No file selected")
                return
            return file_path
        
        return None
    
    @staticmethod
    def get_file(type):
        if type == FileTypeEnum.IMG:
            file_path = filedialog.askopenfilename(
                filetypes=[("Image files", "*.png *.jpg *.jpeg")],
            )
            if not file_path:
                messagebox.showerror("Error", "No file selected")
                return
            return file_path
        
        return None