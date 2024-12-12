import tkinter as tk

class InserPasswordComponent(tk.Frame):
    def __init__(self, parent, controller, bg_color, font_color,*arg, **kwargs):
        super().__init__(parent, *arg, **kwargs)
        self.controller = controller
        self.password_visible = False
        self.bg_color = bg_color
        self.font_color = font_color
        self._initialize_component()
        
    def _initialize_component(self):
        self.configure(bg=self.bg_color)
        tk.Label(
            self, text="Password:", fg=self.font_color, background=self.bg_color,font=("Arial", 12)
        ).grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(
            self,
            textvariable=self.password_var,
            show="*",
            font=("Arial", 12),
            fg="#00ff00",
            insertbackground="#00ff00",
            highlightthickness=2,
            highlightbackground="#00ff00",
        )
        self.password_entry.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
        self.toggle_btn = tk.Button(
            self,
            text="👁️",
            command=self.toggle_password_visibility,
            bg=self.bg_color,
            fg="#00ff00",
            font=("Arial", 10),
            borderwidth=0,
            activebackground=self.bg_color,
        )
        self.toggle_btn.grid(row=0, column=2, sticky=tk.W, padx=5)
        
        tk.Button(
            self,
            text="Encrypt",
            command=lambda: [
                self.controller.encrypt_image_with_pwd(self.password_entry.get()),
                self.password_entry.delete(0, tk.END)
            ],
            bg=self.bg_color,
            fg="#00ff00",
            font=("Arial", 12),
            activebackground=self.bg_color,
            activeforeground="#1e1e1e",
            borderwidth=2,
            highlightbackground="#00ff00",
        ).grid(row=1, column=0, columnspan=3, sticky=tk.EW, padx=30, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
    def toggle_password_visibility(self):
        if self.password_visible:
            self.password_entry.config(show="*")
            self.toggle_btn.config(text="👁️")
        else:
            self.password_entry.config(show="")
            self.toggle_btn.config(text="🙈")
        self.password_visible = not self.password_visible