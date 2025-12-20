import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(self, master, on_navigate):
        super().__init__(master, width=220)
        self.on_navigate = on_navigate
        self.pack_propagate(False)

        # ctk.CTkLabel(
        #     self,
        #     text="YTStreamer",
        #     font=ctk.CTkFont(size=20, weight="bold")
        # ).pack(pady=(30, 20))

        self._nav_button("Stemmer", "landing")

    def _nav_button(self, text, page):
        ctk.CTkButton(
            self,
            text=text,
            height=40,
            corner_radius=8,
            command=lambda: self.on_navigate(page)
        ).pack(fill="x", padx=20, pady=40)
