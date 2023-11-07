import tkinter as tk
from PIL import Image, ImageTk

class App:

    root: tk.Tk
    canvas: tk.Canvas

    def __init__(self, name: str, size: int, path_to_map: str, path_to_graph: str):
        self.root = tk.Tk()
        self.root.title(name)
        self.root.geometry(f"{size}x{size}")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=size, height=size)
        self.canvas.pack()

        self.set_map_as_bg(path_to_map)
        self.add_text_boxes()


    def add_text_boxes(self):
        # Add two input boxes that can be used to enter the start and end node

        # Function that creates a frame containing a label and an entry box
        # The content should be aligned horizontally
        # The function returns the entry box
        def create_input(label_text, pose: tuple[int, int], callback=lambda x: None):
            frame = tk.Frame(self.root)

            label = tk.Label(frame, text=label_text)
            label.pack(side=tk.LEFT, padx=2)

            sv = tk.StringVar()

            def on_change(var, index, mode):
                try:
                    callback(int(sv.get()))
                except ValueError:
                    callback(None)

            sv.trace("w", on_change)

            entry = tk.Entry(frame, textvariable=sv)
            entry.pack(side=tk.RIGHT, padx=2)

            frame.pack()
            frame.place(x=pose[0], y=pose[1])

            return sv

        self.start_node = None
        self.end_node = None
        
        def on_change(var_name, x):
            setattr(self, var_name, x)
            print(f"{self.start_node=} {self.end_node=}")

        self.root.start_input = create_input("Start node", (10, 10), lambda x: on_change("start_node", x))
        self.root.end_input = create_input("End node", (10, 40), lambda x: on_change("end_node", x))


    def set_map_as_bg(self, path_to_map: str):
        self.root.update_idletasks()

        image = Image.open(path_to_map)
        image = image.resize((self.root.winfo_width(), self.root.winfo_height()), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(image)
        
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        self.canvas.image = tk_image

    def on_click(self, callback):
        self.root.bind("<Button-1>", lambda e: callback(e, self.canvas))

    def set_pointer(self, pointer):
        self.pointer = pointer

        def on_update(x, y):
            self.mouse_x = x - 11 # Account for the border
            self.mouse_y = y - 45 # Account for the title bar

        self.pointer.on_update(on_update)

    def run(self):
        #self.pointer.start(self.root.title())

        self.root.mainloop()

        #self.pointer.stop()


# ============================================================


