from PIL import Image, ImageTk  # Correct import
import customtkinter as ctk  # Correct import
import tkinter as tk  # Standard Tkinter
import pandas as pd
import sys

# Username Variables
UserName = ""
Password = ""

# Test Variables
success = False  # test #


def PokeInput():
    global PokeInputVar
    PokeInputVar = Entry.get()
    Entry.delete(0, tk.END)


def LoginInput():
    global UserInput, Password
    UserInput = UserName.get()
    UserInput = UserInput.lower()
    Password = PassName.get()
    UserName.delete(0, tk.END)
    PassName.delete(0, tk.END)
    login.destroy()


login = ctk.CTk()

login.columnconfigure(0, weight=1)
login.columnconfigure(1, weight=1)
login.columnconfigure(2, weight=1)
login.columnconfigure(3, weight=1)
login.rowconfigure(4, weight=1)
login.rowconfigure(5, weight=1)
login.columnconfigure(6, weight=1)

login.geometry("300x300")
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("green")

# Modules
UserLabel = ctk.CTkLabel(login, text="Username:")
PassLabel = ctk.CTkLabel(login, text="Password:")
UserName = ctk.CTkEntry(login, height=50)
PassName = ctk.CTkEntry(login, height=50)
LoginButton = ctk.CTkButton(login, text="Login", command=LoginInput, height=30)

# Grid the modules
UserLabel.grid(row=0, column=0)
PassLabel.grid(row=1, column=0, pady=50)

UserName.grid(row=0, column=1)
PassName.grid(row=1, column=1, pady=0)

LoginButton.grid(row=2, column=0, columnspan=2, pady=50, sticky='ew')

login.mainloop()

try:
    with open('Main/passwords.csv', 'r') as file:
        data = pd.read_csv(file, index_col=False)
        pd.DataFrame(data)
        data = (data.loc[data['Username'] == UserInput])
        print(data)
        if data.empty is True:
            print("Invalid Username or Password")
            sys.exit()
        else:
            pokemon1 = data.loc[:, 'poke1'].to_string(index=False)
            pokemon2 = data.loc[:, 'poke2'].to_string(index=False)
            pokemon3 = data.loc[:, 'poke3'].to_string(index=False)
            pokemon4 = data.loc[:, 'poke4'].to_string(index=False)
            pokemon5 = data.loc[:, 'poke5'].to_string(index=False)
            pokemon6 = data.loc[:, 'poke6'].to_string(index=False)
            success = True
except NameError:
    print("Invalid Username or Password")

if success is True:
    # PokeVariables
    PokeInputVar = ""

    # Set up the window
    root = ctk.CTk()
    root.geometry("750x750")

    # Configure grid columns (0, 1, and 2)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)
    root.title("Custom Tkinter Application")

    # Modules

    PokeSubmit = ctk.CTkButton(root,
                               text="Submit",
                               command=PokeInput,
                               height=50)
    label1 = ctk.CTkLabel(root, text="Input Pokemon")
    Entry = ctk.CTkEntry(root, height=50)
    
    Poke1 = ctk.CTkLabel(root, text=pokemon1, text_color='black', bg_color='grey')
    Poke1Label = ctk.CTkLabel(root, text="Pokemon 1:")
    Poke2 = ctk.CTkLabel(root, text=pokemon2, text_color='black', bg_color='grey')
    Poke2Label = ctk.CTkLabel(root, text="Pokemon 2:")

    # Grid the modules
    Entry.grid(row=1, column=1, columnspan=3, sticky='ew', pady=20)
    label1.grid(row=0, column=2, pady=20)
    PokeSubmit.grid(row=1, column=4, padx=10)
    
    Poke1Label.grid(row=3, column=1)
    Poke1.grid(row=3, column=2, pady=10)
    Poke2Label.grid(row=4, column=1)
    Poke2.grid(row=4, column=2, pady=10)



    root.mainloop()
