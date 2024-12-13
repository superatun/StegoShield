import tkinter as tk
from PIL import Image, ImageTk

class DecryptImageComponent(tk.Frame):
    def __init__(self, parent, controller, bg_color, font_family, font_size, font_color,*arg, **kwargs):
        super().__init__(parent, *arg, **kwargs)
        self.controller = controller
        self.bg_color = bg_color
        self.font_family = font_family
        self.font_size = font_size
        self.font_color = font_color
        self._initialize_component()   
        
    def _initialize_component(self):
        frame = tk.Frame(self)
        frame.configure(bg=self.bg_color)
        frame.grid(sticky="NSEW")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)

        imagen = Image.open("src\\View\\resources\\unlock_icon.png")
        imagen = imagen.resize((100, 100), Image.LANCZOS)
        self.imagen_tk = ImageTk.PhotoImage(imagen)

        label = tk.Label(frame, text="Decrypt Image", font=(self.font_family, self.font_size, "bold"), bg=self.bg_color, fg=self.font_color)
        label.grid(row=0, column=0, pady=(10, 3))

        boton = tk.Button(
            frame,
            image=self.imagen_tk,
            borderwidth=0,
            relief="flat",
            background=self.bg_color,
            activebackground=self.bg_color,
            command=lambda: self.controller.get_encrypted_img()
        )
        boton.grid(row=1, column=0, pady=(5, 10))
