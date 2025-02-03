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
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=0)
root.title("Custom Tkinter Application")
# Modules

label1 = ctk.CTkLabel(root, text="Input First Name")
label2 = ctk.CTkLabel(root, text="Input Last Name")

entry1 = ctk.CTkEntry(root)
entry2 = ctk.CTkEntry(root)

InputButton = ctk.CTkButton(root, text='submit')

# Grid the modules

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

entry1.grid(row=0, column=1, pady=10, padx=30)
entry2.grid(row=1, column=1, pady=10, padx=30)

InputButton.grid(row=2, column=0, sticky='ew', columnspan=2)

root.mainloop()
