class Pointer:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.callback = lambda x, y: None

    def on_update(self, callback=lambda x, y: None):
        self.callback = callback

    def start(self):
        raise NotImplementedError()
    
    def stop(self):
        raise NotImplementedError()