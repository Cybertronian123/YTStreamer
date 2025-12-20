import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(self, master, on_navigate):
        super().__init__(master, width=220, corner_radius=0)
        self.pack_propagate(False)

        # 🔹 Inner padding container
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=16, pady=16)

        ctk.CTkButton(
            content,
            text="Stemmer",
            height=40,
            corner_radius=10,
            command=lambda: on_navigate("landing")
        ).pack(fill="x", pady=6)
