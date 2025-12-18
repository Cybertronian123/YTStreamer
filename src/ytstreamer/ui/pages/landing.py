import customtkinter as ctk


class LandingPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.grid(row=0, column=0)

        ctk.CTkLabel(
            container,
            text="Welcome to YTStreamer",
            font=ctk.CTkFont(size=28, weight="bold")
        ).grid(row=0, column=0, pady=(0, 12))

        ctk.CTkLabel(
            container,
            text="Separate vocals and music from audio files",
            font=ctk.CTkFont(size=14)
        ).grid(row=1, column=0)
