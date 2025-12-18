import customtkinter as ctk
from ytstreamer.theme.appearance import setup_theme

class YTStreamerApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        setup_theme()

        self.title("YTStreamer")
        self.geometry("900x600")

