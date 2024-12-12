import tkinter as tk
import tkinter as tk
from PIL import Image, ImageTk

class DecryptImageComponent(tk.Frame):
    def __init__(self, parent, controller, bg_color,*arg, **kwargs):
        super().__init__(parent, *arg, **kwargs)
        self.controller = controller
        self.bg_color = bg_color
        self._initialize_component()   
        
    def _initialize_component(self):
        frame = tk.Frame(self)
        frame.configure(bg=self.bg_color)
        frame.grid(sticky="NSEW")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

        imagen = Image.open("View\\resources\\unlock_icon.png")
        imagen = imagen.resize((100, 100), Image.LANCZOS)
        self.imagen_tk = ImageTk.PhotoImage(imagen)

        boton = tk.Button(frame, image=self.imagen_tk, borderwidth=0, relief="flat" ,background=self.bg_color,activebackground=self.bg_color ,command=lambda: self.controller.get_encrypted_img())
        
        boton.grid(row=0, column=0)