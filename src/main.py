from app import App
from apath import get_asset_path
from modal.mouse_pointer import MousePointer

title = "Ma super map vocale"

pointer = MousePointer()
# vocal = Vocal()

app = App(title, 600, get_asset_path("map.png"), get_asset_path("city.graph"))
app.set_pointer(pointer)
# app.set_vocal(vocal)

app.run()