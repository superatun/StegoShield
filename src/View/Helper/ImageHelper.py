from PIL import Image, ImageTk, ImageDraw
import tkinter as tk

class ImageHelper():
    
    @staticmethod
    def get_eye_icon(image_path, width, height):
        eye = Image.open(image_path).convert("RGBA")
        eye = eye.resize((width, height), Image.LANCZOS)

        eye_white = eye.copy()
        pixels = eye_white.load()
        for y in range(eye_white.size[1]):
            for x in range(eye_white.size[0]):
                r, g, b, a = pixels[x, y]
                if a > 0:
                    pixels[x, y] = (255, 255, 255, a)

        eye_with_line = eye_white.copy()
        draw = ImageDraw.Draw(eye_with_line)
        draw.line((0, 0, 25, 25), fill=(255, 255, 255, 255), width=3)

        return ImageTk.PhotoImage(eye_white), ImageTk.PhotoImage(eye_with_line)