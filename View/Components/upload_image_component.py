import tkinter as tk

from Model.Enum.ActionEnum import ActionEnum

class UploadImageComponent(tk.Frame):
    def __init__(self, parent, controller, file_name_var, *arg, **kwargs):
        super().__init__(parent, *arg, **kwargs)
        self.controller = controller
        self.file_name_var = file_name_var
        self._initialize_component()
        
    def _initialize_component(self):
        tk.Label(self, text="File name:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.dynamic_label = tk.Label(self, textvariable=self.file_name_var)
        self.dynamic_label.grid(row=1, column=1, columnspan=4, sticky=tk.W, padx=10, pady=5)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        tk.Button(self, text="Upload file", command=lambda: self.controller.manage_file(ActionEnum.SAVE), width=10).grid(row=2, column=0, sticky=tk.EW, pady=5, padx=30)
        tk.Button(self, text="Clear", width=10, command=lambda: self.controller.manage_file(ActionEnum.DELETE)).grid(row=2, column=1, sticky=tk.EW, pady=5, padx=30)