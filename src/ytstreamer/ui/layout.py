import customtkinter as ctk
from ytstreamer.ui.sidebar import Sidebar
from ytstreamer.ui.pages.landing import LandingPage

class AppLayout(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.sidebar = Sidebar(self, self.show_page)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.content = ctk.CTkFrame(self, corner_radius=0)
        self.content.grid(row=0, column=1, sticky="nsew")

        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        self.pages = {}
        self._init_pages()

        self.show_page("landing")

    def _init_pages(self):
        self.pages["landing"] = LandingPage(self.content)


    def show_page(self, name):
        for page in self.pages.values():
            page.grid_forget()

        self.pages[name].grid(row=0, column=0, sticky="nsew")