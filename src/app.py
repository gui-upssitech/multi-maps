import tkinter as tk
from PIL import Image, ImageTk

class App:

    root: tk.Tk
    canvas: tk.Canvas

    def __init__(self, name: str, size: int, path_to_map: str):
        self.root = tk.Tk()
        self.root.title(name)
        self.root.geometry(f"{size}x{size}")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=size, height=size)
        self.canvas.pack()

        self.set_map_as_bg(path_to_map)


    def set_map_as_bg(self, path_to_map: str):
        self.root.update_idletasks()

        image = Image.open(path_to_map)
        image = image.resize((self.root.winfo_width(), self.root.winfo_height()), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(image)
        
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        self.canvas.image = tk_image

    def on_click(self, callback):
        self.root.bind("<Button-1>", lambda e: callback(e, self.canvas))


    def run(self):
        self.root.mainloop()


# ============================================================


