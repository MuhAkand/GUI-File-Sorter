import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import threading


def organizeFiles():
    path = entryPath.get()
    if not path:
        messagebox.showerror("Error", "Please provide a valid directory path.")
        return

    try:
        for root, _, files in os.walk(path):
            for file_ in files:
                src_file = os.path.join(root, file_)
                if src_file != __file__:  # Exclude this script file
                    name, ext = os.path.splitext(file_)
                    extension = ext[1:]
                    dest_dir = os.path.join(path, extension)
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    dest_file = os.path.join(dest_dir, file_)
                    if not os.path.exists(dest_file):
                        shutil.move(src_file, dest_file)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return

    messagebox.showinfo("Success", "Files organized successfully.")


def browsePath():
    path = filedialog.askdirectory()
    if path:
        entryPath.delete(0, tk.END)
        entryPath.insert(0, path)


def confirmAndOrganize():
    if messagebox.askyesno("Confirmation", "Are you sure you want to organize files in the selected directory?"):
        threading.Thread(target=organizeFiles).start()


# Create a GUI window
root = tk.Tk()
root.title("File Organizer")

# Create widgets
labelPath = tk.Label(root, text="Enter Path:")
entryPath = tk.Entry(root, width=50)
buttonBrowse = tk.Button(root, text="Browse", command=browsePath)
buttonOrganize = tk.Button(root, text="Organize Files", command=confirmAndOrganize)

# Arrange widgets using grid layout
labelPath.grid(row=0, column=0, padx=5, pady=5)
entryPath.grid(row=0, column=1, padx=5, pady=5)
buttonBrowse.grid(row=0, column=2, padx=5, pady=5)
buttonOrganize.grid(row=1, columnspan=3, padx=5, pady=5)

# Run the GUI
root.mainloop()
