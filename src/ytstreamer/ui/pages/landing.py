import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path


class LandingPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0)

        self.audio_path: Path | None = None
        self.output_dir: Path | None = None

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        outer = ctk.CTkFrame(self, corner_radius=0)
        outer.grid(row=0, column=0, padx=40, pady=40)
        outer.grid(padx=40, pady=40)

        content = ctk.CTkFrame(outer, fg_color="transparent", corner_radius=0)
        content.grid(row=0, column=0, padx=30, pady=30)
        content.grid(padx=30, pady=30)

        # Title
        ctk.CTkLabel(
            content,
            text="Generate Music Stems",
            font=ctk.CTkFont(size=26, weight="bold")
        ).grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Audio file picker
        ctk.CTkLabel(content, text="Audio File").grid(row=1, column=0, sticky="w")
        self.audio_entry = ctk.CTkEntry(content, width=400)
        self.audio_entry.grid(row=2, column=0, columnspan=2, pady=6, sticky="ew")

        ctk.CTkButton(
            content,
            text="Browse",
            command=self.pick_audio,
            corner_radius=5,
        ).grid(row=2, column=2, padx=(10, 0))

        # Output folder picker
        ctk.CTkLabel(content, text="Output Folder").grid(row=3, column=0, sticky="w", pady=(16, 0))
        self.output_entry = ctk.CTkEntry(content, width=400)
        self.output_entry.grid(row=4, column=0, columnspan=2, pady=6, sticky="ew")

        ctk.CTkButton(
            content,
            text="Browse",
            command=self.pick_output,
            corner_radius=5,
        ).grid(row=4, column=2, padx=(10, 0))

        # Stem selector
        ctk.CTkLabel(content, text="Stems").grid(row=5, column=0, sticky="w", pady=(16, 0))
        self.stems = ctk.CTkOptionMenu(
            content,
            values=["2", "4", "5"],
            corner_radius=5,
        )
        self.stems.set("2")
        self.stems.grid(row=6, column=0, sticky="w")

        # Run button
        self.run_button = ctk.CTkButton(
            content,
            text="Generate Stems",
            height=44,
            corner_radius=10,
            command=self.on_run
        )
        self.run_button.grid(row=7, column=0, columnspan=3, pady=(30, 10))

        # Status
        self.status = ctk.CTkLabel(content, text="")
        self.status.grid(row=8, column=0, columnspan=3)

    def pick_audio(self):
        path = filedialog.askopenfilename(
            title="Select Audio File",
            filetypes=[("Audio Files", "*.mp3 *.wav *.flac")]
        )
        if path:
            self.audio_path = Path(path)
            self.audio_entry.delete(0, "end")
            self.audio_entry.insert(0, path)

    def pick_output(self):
        path = filedialog.askdirectory(title="Select Output Folder")
        if path:
            self.output_dir = Path(path)
            self.output_entry.delete(0, "end")
            self.output_entry.insert(0, path)

    def on_run(self):
        if not self.audio_path or not self.output_dir:
            self.status.configure(text="Please select audio file and output folder")
            return

        self.status.configure(
            text=f"Ready to separate into {self.stems.get()} stems"
        )
