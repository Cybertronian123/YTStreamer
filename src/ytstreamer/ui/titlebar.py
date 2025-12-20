import customtkinter as ctk


class TitleBar(ctk.CTkFrame):
    HEIGHT = 36

    def __init__(self, master):
        super().__init__(master, height=self.HEIGHT, corner_radius=0, fg_color="#403f3f")

        self.master = master
        self.pack(fill="x")
        self.pack_propagate(False)

        self._bind_drag()

        # App title
        ctk.CTkLabel(
            self,
            text="YTStreamer",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(side="left", padx=12)

        # Window buttons
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(side="right")

        ctk.CTkButton(
            btn_frame,
            text="—",
            width=36,
            height=28,
            corner_radius=2,
            command=self.minimize,
            fg_color="#3094ff",
            hover_color="#6dadf2",
        ).pack(side="left", padx=4)

        ctk.CTkButton(
            btn_frame,
            text="✕",
            width=36,
            height=28,
            corner_radius=2,
            hover_color="#d14343",
            fg_color="#db2323",
            command=self.close
        ).pack(side="left", padx=(0, 6))

    def minimize(self):
        self.master.update_idletasks()
        self.master.iconify()

    def close(self):
        self.master.destroy()

    def _bind_drag(self):
        self.bind("<Button-1>", self._start_move)
        self.bind("<B1-Motion>", self._on_move)

    def _start_move(self, event):
        self.master.title_bar_offset_x = event.x
        self.master.title_bar_offset_y = event.y

    def _on_move(self, event):
        x = event.x_root - self.master.title_bar_offset_x
        y = event.y_root - self.master.title_bar_offset_y
        self.master.geometry(f"+{x}+{y}")
