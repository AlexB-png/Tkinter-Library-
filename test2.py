from PIL import Image, ImageTk  # Correct import
import customtkinter as ctk  # Correct import
import tkinter as tk  # Standard Tkinter

# Username Variables
UserName = ""
Password = ""

def PokeInput():
    global PokeInputVar
    PokeInputVar = Entry.get()
    Entry.delete(0, tk.END)


def LoginInput():
    global UserName, Password
    UserName = UserName.get()
    Password = PassName.get()
    UserName.delete(0, tk.END)
    PassName.delete(0, tk.END)

login = ctk.CTk()

login.columnconfigure(0, weight=1)
login.columnconfigure(1, weight=1)
login.columnconfigure(2, weight=1)
login.columnconfigure(3, weight=1)
login.rowconfigure(4, weight=1)
login.rowconfigure(5, weight=1)
login.columnconfigure(6, weight=1)

login.geometry("750x750")
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("green")

# Modules
UserLabel = ctk.CTkLabel(login, text="Username:")
PassLabel = ctk.CTkLabel(login, text="Password:")
UserName = ctk.CTkEntry(login, height=50)
PassName = ctk.CTkEntry(login, height=50)
LoginButton = ctk.CTkButton(login, text="Login", command=LoginInput)

# Grid the modules
UserLabel.grid(row=0, column=0)
PassLabel.grid(row=1, column=0)



login.mainloop()



















# PokeVariables
PokeInputVar = ""

# Set up the window
root = ctk.CTk()
root.geometry("750x750")

# Set appearance mode and color theme







# Configure grid columns (0, 1, and 2)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.columnconfigure(6, weight=1)
root.title("Custom Tkinter Application")
# Modules

PokeSubmit = ctk.CTkButton(root, text="Submit", command=PokeInput, height=50)
label1 = ctk.CTkLabel(root, text="Input Pokemon")
Entry = ctk.CTkEntry(root, height=50)
Entry.grid(row=1, column=1, columnspan=3, sticky='ew')
label1.grid(row=0, column=2)
PokeSubmit.grid(row=1, column=4, padx=10)

root.mainloop()
