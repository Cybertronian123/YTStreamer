import customtkinter as ctk
from ytstreamer.theme.appearance import setup_theme
from ytstreamer.ui.layout import AppLayout

class YTStreamerApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        setup_theme()

        self.title("YTStreamer")
        self.geometry("1000x650")
        self.minsize(900, 600)

        self.layout = AppLayout(self)
        self.layout.pack(fill="both", expand=True)
