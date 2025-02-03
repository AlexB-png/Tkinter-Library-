from PIL import Image, ImageTk  # Correct import
import customtkinter as ctk  # Correct import
import tkinter as tk  # Standard Tkinter

# Set up the window
root = ctk.CTk()
root.geometry("500x500")

# Set appearance mode and color theme
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("green")

# Configure grid columns (0, 1, and 2)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.title("Custom Tkinter Application")
# Modules

label1 = ctk.CTkLabel(root, text="Input Pokemon")
Entry = ctk.CTkEntry(root, height=50) 
Entry.grid(row=0, column=1, columnspan=2, sticky='ew')
label1.grid(row=0, column=0)

root.mainloop()
