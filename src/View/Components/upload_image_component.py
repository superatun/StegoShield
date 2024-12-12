import tkinter as tk

from src.Model.Enum.ActionEnum import ActionEnum

class UploadImageComponent(tk.Frame):
    def __init__(self, parent, controller, file_name_var, bg_color, font_color, *arg, **kwargs):
        super().__init__(parent, *arg, **kwargs)
        self.controller = controller
        self.file_name_var = file_name_var
        self.bg_color = bg_color
        self.font_color = font_color
        self._initialize_component()
        
    def _initialize_component(self):
        self.configure(bg=self.bg_color)
        tk.Label(self, text="File name:", fg=self.font_color, background=self.bg_color).grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.dynamic_label = tk.Label(self, textvariable=self.file_name_var, bg=self.bg_color, fg=self.font_color)
        self.dynamic_label.grid(row=1, column=1, columnspan=4, sticky=tk.W, padx=10, pady=5)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        tk.Button(self, text="Upload Image", command=lambda: self.controller.manage_file(ActionEnum.SAVE), width=10).grid(row=2, column=0, sticky=tk.EW, pady=5, padx=30)
        tk.Button(self, text="Clear Image", width=10, command=lambda: self.controller.manage_file(ActionEnum.DELETE)).grid(row=2, column=1, sticky=tk.EW, pady=5, padx=30)