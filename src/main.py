import tkinter as tk
from PIL import Image, ImageTk
from os import path

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
        self.root.bind("<Button-1>", self.on_mouse_pressed)


    def set_map_as_bg(self, path_to_map: str):
        self.root.update_idletasks()

        image = Image.open(path_to_map)
        image = image.resize((self.root.winfo_width(), self.root.winfo_height()), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(image)
        
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        self.canvas.image = tk_image

    def on_mouse_pressed(self, event: tk.Event):
        x, y = event.x, event.y
        self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")

    def run(self):
        self.root.mainloop()

# ============================================================

def main():
    assets_dir = path.abspath(path.join(path.dirname(__file__), "../assets"))
    map_path = path.join(assets_dir, "map.png")

    app = App("Map", 500, map_path)
    app.run()


if __name__ == "__main__":
    main()
