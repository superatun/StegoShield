import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageOps

from src.View.Helper.ImageHelper import ImageHelper

class InserPasswordComponent(tk.Frame):
    def __init__(self, parent, controller, bg_color, font_color, btn_bg, btn_fontcolor, pwd_box_bg, font_size, font_family, pwd_text_color = "#000", *arg, **kwargs):
        super().__init__(parent, *arg, **kwargs)
        self.controller = controller
        self.password_visible = False
        self.bg_color = bg_color
        self.font_color = font_color
        self.btn_bg = btn_bg
        self.btn_fontcolor = btn_fontcolor
        self.pwd_box_bg = pwd_box_bg
        self.pwd_text_color = pwd_text_color
        self.font_size = font_size
        self.font_family = font_family
        self._initialize_component()
        
    def _initialize_component(self):
        self.configure(bg=self.bg_color)
        self.grid_columnconfigure(0, weight=1)  # Columna 1 (1/6)
        self.grid_columnconfigure(1, weight=4)  # Columna 2 (4/6)
        self.grid_columnconfigure(2, weight=2)  # Columna 3 (2/6)
        tk.Label(
            self, text="Password:", fg=self.font_color, background=self.bg_color,font=(self.font_family, self.font_size)
        ).grid(row=0, column=0, sticky=tk.W, padx=(10, 5), pady=5) 

        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(
            self,
            textvariable=self.password_var,
            show="*",
            font=(self.font_family, self.font_size),
            fg=self.pwd_text_color,
            insertbackground="#000",
            highlightthickness=2,
            highlightbackground=self.pwd_box_bg,
            background=self.pwd_box_bg,
        )
        self.password_entry.grid(row=0, column=1, sticky=tk.EW, padx=(5, 5), pady=5)
        
        self.eye_white_tk, self.eye_with_line_tk = ImageHelper.get_eye_icon("src/View/resources/eye_icon.png", 30, 30)
        self.toggle_btn = tk.Button(
            self,
            image=self.eye_with_line_tk,
            command=self.toggle_password_visibility,
            bg=self.bg_color,
            borderwidth=0,
            activebackground=self.bg_color,
        )
        self.toggle_btn.grid(row=0, column=2, sticky=tk.W, padx=5)

        self.toggle_btn.image = self.eye_white_tk
        self.is_visible = False
        
        tk.Button(
            self,
            text="Encrypt",
            command=lambda: [
                self.controller.encrypt_image_with_pwd(self.password_entry.get()),
                self.password_entry.delete(0, tk.END)
            ],
            background=self.btn_bg,
            fg=self.btn_fontcolor,
            font=(self.font_family, self.font_size, "bold"),
            borderwidth=2,
            activebackground=self.btn_bg,
            activeforeground=self.btn_fontcolor
        ).grid(row=1, column=0, columnspan=3, sticky=tk.EW, padx=30, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
    def toggle_password_visibility(self):
        if self.is_visible:
            self.password_entry.configure(show="*")
            self.toggle_btn.configure(image=self.eye_with_line_tk)
            self.toggle_btn.image = self.eye_with_line_tk
        else:
            self.password_entry.configure(show="")
            self.toggle_btn.configure(image=self.eye_white_tk)
            self.toggle_btn.image = self.eye_white_tk
        self.is_visible = not self.is_visible