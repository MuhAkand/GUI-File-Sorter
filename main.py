import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organizeFiles():
    path = entryPath.get()
    if not path:
        return  # No path provided

    list_ = os.listdir(path)
    for file_ in list_:
        name, ext = os.path.splitext(file_)
        extension = ext[1:]
        if ext == '':
            continue

        if os.path.exists(os.path.join(path, extension)):
            shutil.move(os.path.join(path, file_), os.path.join(path, extension, file_))
        else:
            os.makedirs(os.path.join(path, extension))
            shutil.move(os.path.join(path, file_), os.path.join(path, extension, file_))

def browsePath():
    path = filedialog.askdirectory()
    if path:
        entryPath.delete(0, tk.END)
        entryPath.insert(0, path)

# Create a GUI window
root = tk.Tk()
root.title("File Organizer")

# Create widgets
labelPath = tk.Label(root, text="Enter Path:")
entryPath = tk.Entry(root, width=50)
buttonBrowse = tk.Button(root, text="Browse", command=browsePath)
buttonOrganize = tk.Button(root, text="Organize Files", command=organizeFiles)

# Arrange widgets using grid layout
labelPath.grid(row=0, column=0, padx=5, pady=5)
entryPath.grid(row=0, column=1, padx=5, pady=5)
buttonBrowse.grid(row=0, column=2, padx=5, pady=5)
buttonOrganize.grid(row=1, columnspan=3, padx=5, pady=5)

# Run the GUI
root.mainloop()
