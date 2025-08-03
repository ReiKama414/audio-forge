import tkinter as tk

def log_message(log_widget, message):
    log_widget.insert(tk.END, message + "\n")
    log_widget.see(tk.END)

class DragDropArea(tk.Listbox):
    def __init__(self, master, files_list, **kwargs):
        super().__init__(master, **kwargs)
        self.files_list = files_list
        self.config(height=8, selectmode=tk.SINGLE)
        self.bind("<Double-Button-1>", self.remove_selected)

    def add_files(self, files):
        for f in files:
            if f not in self.files_list:
                self.files_list.append(f)
                self.insert(tk.END, f)

    def remove_selected(self, event):
        selection = self.curselection()
        if selection:
            index = selection[0]
            del self.files_list[index]
            self.delete(index)
