import tkinter as tk
from tkinter import filedialog, ttk
import os
import threading
from converter import convert_audio_files
from ui_components import DragDropArea, log_message

input_files = []

def browse_files():
    files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3 *.wav *.m4a *.flac *.aac *.ogg *.wma *.alac")])
    if files:
        file_listbox.add_files(files)

def select_output_dir():
    path = filedialog.askdirectory()
    if path:
        output_dir_var.set(path)

def start_conversion():
    if not input_files:
        log_message(log_area, "請先加入音訊檔案")
        return

    output_format = format_var.get()
    output_dir = output_dir_var.get() or None

    progress_bar["maximum"] = len(input_files)
    progress_bar["value"] = 0

    def run():
        for i, path in enumerate(input_files):
            convert_audio_files([path], output_format, output_dir, lambda msg: log_message(log_area, msg))
            progress_bar["value"] += 1

    threading.Thread(target=run).start()

app = tk.Tk()
app.title("音訊轉檔器 GUI")
app.geometry("600x500")

file_frame = tk.Frame(app)
file_frame.pack(padx=10, pady=10, fill="x")

file_listbox = DragDropArea(file_frame, input_files, bg="#f0f0f0")
file_listbox.pack(fill="both", expand=True)

tk.Button(app, text="加入音訊檔", command=browse_files).pack(pady=5)

options_frame = tk.Frame(app)
options_frame.pack(padx=10, pady=5, fill="x")

tk.Label(options_frame, text="輸出格式：").pack(side="left")
format_var = tk.StringVar(value="wav")
ttk.Combobox(options_frame, textvariable=format_var, values=["wav", "mp3"], width=10).pack(side="left", padx=5)

tk.Label(options_frame, text="輸出資料夾：").pack(side="left", padx=(20, 0))
output_dir_var = tk.StringVar()
tk.Entry(options_frame, textvariable=output_dir_var, width=30).pack(side="left", padx=5)
tk.Button(options_frame, text="選擇", command=select_output_dir).pack(side="left")

progress_bar = ttk.Progressbar(app, orient="horizontal", length=500, mode="determinate")
progress_bar.pack(pady=10)

log_area = tk.Text(app, height=10, bg="#222", fg="#0f0")
log_area.pack(fill="both", padx=10, pady=5, expand=True)

tk.Button(app, text="開始轉換", command=start_conversion, bg="#008080", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

app.mainloop()
