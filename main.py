import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


def organize_folder(folder):
    """
    Organizes all files in the selected folder into subfolders by file extension.
    """
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            _, extension = os.path.splitext(file)
            extension = extension[1:].upper()  # Remove dot and convert to uppercase

            if extension == '':
                extension = 'NO_EXTENSION'

            destination_folder = os.path.join(folder, extension)
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)

            shutil.move(file_path, os.path.join(destination_folder, file))


def choose_folder():
    """
    Opens a dialog for the user to select a folder to organize.
    """
    folder = filedialog.askdirectory()
    if folder:
        organize_folder(folder)
        messagebox.showinfo("Done", f"Files organized in: {folder}")


# Create the main window
window = tk.Tk()
window.title("File Organizer by Extension")
window.geometry("300x100")

label = tk.Label(window, text="Click the button to choose a folder to organize:")
label.pack(padx=10, pady=10)

choose_button = tk.Button(window, text="Choose Folder", command=choose_folder)
choose_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 300
window_height = 150

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.mainloop()
