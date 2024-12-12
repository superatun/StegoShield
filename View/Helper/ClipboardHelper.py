from tkinter import messagebox

class ClipboardHelper():

    @staticmethod
    def copy(window, text):
        try:
            window.clipboard_clear()
            window.clipboard_append(text)
            window.update()
            messagebox.showinfo("Copied", "Text copied to clipboard")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy text: {str(e)}")