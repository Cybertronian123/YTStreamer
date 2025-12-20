import ctypes
import customtkinter as ctk

from ytstreamer.ui.layout import AppLayout
from ytstreamer.theme.appearance import setup_theme

# Win32 constants
GWL_STYLE = -16
WS_CAPTION = 0x00C00000
WS_THICKFRAME = 0x00040000
WS_MINIMIZEBOX = 0x00020000
WS_SYSMENU = 0x00080000

SWP_FRAMECHANGED = 0x0020
SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001
SWP_NOZORDER = 0x0004


class YTStreamerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        setup_theme()

        self.title("YTStreamer")
        self.geometry("1000x650")
        self.minsize(900, 600)

        # Apply Win32 borderless AFTER window creation
        self.after(10, self._apply_borderless)

        self.layout = AppLayout(self)
        self.layout.pack(fill="both", expand=True)

    def _apply_borderless(self):
        hwnd = ctypes.windll.user32.GetParent(self.winfo_id())

        style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)

        style &= ~WS_CAPTION
        style &= ~WS_THICKFRAME
        style |= WS_MINIMIZEBOX | WS_SYSMENU

        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)
        ctypes.windll.user32.SetWindowPos(
            hwnd,
            None,
            0, 0, 0, 0,
            SWP_FRAMECHANGED | SWP_NOMOVE | SWP_NOSIZE | SWP_NOZORDER
        )
