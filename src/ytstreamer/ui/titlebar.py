import ctypes
import customtkinter as ctk


class TitleBar(ctk.CTkFrame):
    HEIGHT = 32

    def __init__(self, master):

        font_family = ctk.CTkFont("Rockybilly", 9)
        super().__init__(
            master,
            height=self.HEIGHT,
            corner_radius=20,
            fg_color="#403f3f"
        )

        self.grid_propagate(False)

        # 🔹 Inner padding container
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=12, pady=6)

        # 🔹 Window drag (native, flicker-free)
        content.bind("<Button-1>", self._start_native_move)

        # 🔹 Title text
        ctk.CTkLabel(
            content,
            text="YTStreamer",
            font=font_family,
            text_color="#e5e7eb"
        ).pack(side="left")

        # 🔹 Window buttons
        btns = ctk.CTkFrame(content, fg_color="transparent")
        btns.pack(side="right")

        ctk.CTkButton(
            btns,
            text="—",
            width=36,
            height=24,
            fg_color="transparent",
            hover_color="#525252",
            command=self._minimize
        ).pack(side="left", padx=4)

        ctk.CTkButton(
            btns,
            text="✕",
            width=36,
            height=24,
            fg_color="transparent",
            hover_color="#991b1b",
            command=self._close
        ).pack(side="left")

    def _start_native_move(self, event):
        hwnd = ctypes.windll.user32.GetParent(self.winfo_toplevel().winfo_id())

        ctypes.windll.user32.ReleaseCapture()
        ctypes.windll.user32.PostMessageW(
            hwnd,
            0x00A1,  # WM_NCLBUTTONDOWN
            0x0002,  # HTCAPTION
            0
        )

    def _minimize(self):
        self.winfo_toplevel().iconify()

    def _close(self):
        self.winfo_toplevel().destroy()
