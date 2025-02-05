from PIL import Image, ImageTk  # Correct import
import customtkinter as ctk  # Correct import
import tkinter as tk  # Standard Tkinter
import pandas as pd
import sys
import webbrowser
import requests
import json
import os
from tkinter import *
from PIL import Image, ImageTk


def OpenURL():
    global BrowserURL
    webbrowser.open(BrowserURL)


def ExtraOperations():
    global SuccessWindow
    root.iconify()

    # Window Setup
    SuccessWindow = ctk.CTk()  
    SuccessWindow.geometry('500x500')
    SuccessWindow.title('Success')

    # Modules
    BrowserButton = ctk.CTkButton(SuccessWindow, text="Open JSON", command=OpenURL)
    PrintJSONFile = ctk.CTkButton(SuccessWindow, text="Print JSON", command=PrintJSON)

    # Grid Setup
    BrowserButton.grid(row=0, column=0, pady=20)
    PrintJSONFile.grid(row=1, column=0)

    SuccessWindow.mainloop()


def PrintJSON():
    global PokemonJSON
    global BrowserURL
    url_response = requests.get(BrowserURL)
    data = url_response.json()
    PokemonJSON = (json.dumps(data, indent=4))
    os.system('cls')
    print(PokemonJSON)


def CheckIfOnline(url):
    global fail
    global PokemonJSON
    global BrowserURL
    BrowserURL = url
    url_response = requests.get(url)
    if url_response.status_code != 200:
        os.system('cls')
        print("Server does not exist")
        fail = True
    else:
        data = url_response.json()
        PokemonJSON = (json.dumps(data, indent=4))
        fail = False
        print(PokemonJSON)


def Replace1Fun():
    global URL
    Replace1.configure(fg_color='lime')
    selected = Entry.get()
    Entry.delete(0, tk.END)
    Entry.insert(0, 'https://pokeapi.co/api/v2/pokemon/')
    URL = selected
    CheckIfOnline(URL)
    if fail is False:
        
        global PokemonJSON
        PokemonJSON = json.loads(PokemonJSON)
        x = PokemonJSON["name"]
        with open('Main/passwords.csv', 'r') as file:
            data = pd.read_csv(file, index_col=False)
            data.loc[data['Username'] == UserInput, 'poke1'] = x
        with open('Main/passwords.csv', 'w') as file:
            data.to_csv(file, index=False)
        os.system('cls')
        print("The Pokemon has been replaced")
        Poke1.configure(text=x)


def PokeInput():
    Entry.delete(0, tk.END)


def LoginInput():
    global UserInput, Password
    UserInput = UserName.get()
    UserInput = UserInput.lower()
    Password = PassName.get()
    UserName.delete(0, tk.END)
    PassName.delete(0, tk.END)
    try:
        with open('Main/passwords.csv', 'r') as file:
            data = pd.read_csv(file, index_col=False)
            pd.DataFrame(data)
            data = (data.loc[data['Username'] == UserInput])
            data = (data.loc[data['password'] == Password])
            if data.empty is True:
                LoginfailLabel.configure(text="Invalid Username or Password", text_color='red')
            else:
                global pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6, success
                pokemon1 = data.loc[:, 'poke1'].to_string(index=False)
                pokemon2 = data.loc[:, 'poke2'].to_string(index=False)
                pokemon3 = data.loc[:, 'poke3'].to_string(index=False)
                pokemon4 = data.loc[:, 'poke4'].to_string(index=False)
                pokemon5 = data.loc[:, 'poke5'].to_string(index=False)
                pokemon6 = data.loc[:, 'poke6'].to_string(index=False)
                success = True
                login.destroy()
    except NameError:
        LoginfailLabel.configure(text="Invalid Username or Password", text_color='red')


def replace():
    slot = Replacement.get()
    Replacement.delete(0, tk.END)
    PokeSelector = Entry.get()
    print(slot)
    PokeInputVar = f"https://pokeapi.co/api/v2/pokemon/{PokeSelector}"
    print(PokeInputVar)
    CheckIfOnline(PokeInputVar)

def my_command():
    print("RERERERERERRE")


# Username Variables
UserName = ""
Password = ""

# Test Variables
success = False  # test #
Fail = False

# JSON Variables
PokemonJSON = ""

# LOGIN PAGE #

login = ctk.CTk()

login.columnconfigure(0, weight=1)
login.columnconfigure(1, weight=1)
login.columnconfigure(2, weight=1)
login.columnconfigure(3, weight=1)
login.rowconfigure(4, weight=1)
login.rowconfigure(5, weight=1)
login.columnconfigure(6, weight=1)

login.geometry("250x300")
ctk.set_appearance_mode('dark')

# Modules
UserLabel = ctk.CTkLabel(login, text="Username:")
PassLabel = ctk.CTkLabel(login, text="Password:")
UserName = ctk.CTkEntry(login, height=50)
PassName = ctk.CTkEntry(login, height=50)
LoginButton = ctk.CTkButton(login, text="Login", command=LoginInput, height=30)
LoginfailLabel = ctk.CTkLabel(login, text="Input Username and Password")

# Grid the modules
UserLabel.grid(row=0, column=0)
PassLabel.grid(row=1, column=0, pady=50)

UserName.grid(row=0, column=1, sticky='ew')
PassName.grid(row=1, column=1, pady=0, sticky='ew')

LoginButton.grid(row=2, column=0, columnspan=2, pady=10, sticky='ew')

LoginfailLabel.grid(row=3, column=0, columnspan=2, pady=10)

login.mainloop()

# END LOGIN #
# POKEMON PAGE #

if success is True:
    # PokeVariables
    PokeInputVar = ""

    # Set up the window
    root = ctk.CTk()
    root.geometry("750x550")

    # Configure grid columns (0, 1, and 2)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)
    root.rowconfigure(10, weight=1)
    root.title("Custom Tkinter Application")

    original_image = Image.open('Main/poke.png')
    resized_image = original_image.resize((100, 100))
    click_btn = ImageTk.PhotoImage(resized_image)
    button = tk.Button(root, image=click_btn, command=my_command)
    button.grid(row=0, column=3)

    PokeSubmit = ctk.CTkButton(root,
                            text="Clear",
                            command=PokeInput,
                            height=50)
    label1 = ctk.CTkLabel(root, text="Input Pokemon")
    Entry = ctk.CTkEntry(root, height=50)

    Replacement = ctk.CTkEntry(root)
    ReplacementButton = ctk.CTkButton(root, text="Replace pokemon slot:", height=25, command=replace)
    
    Poke1 = ctk.CTkLabel(root, text=pokemon1, text_color='black', bg_color='grey', font=('arial', 25))
    Poke1Label = ctk.CTkLabel(root, text="Pokemon 1:", font=('arial', 25))

    Poke2 = ctk.CTkLabel(root, text=pokemon2, text_color='black', bg_color='grey', font=('arial', 25))
    Poke2Label = ctk.CTkLabel(root, text="Pokemon 2:", font=('arial', 25))

    Poke3 = ctk.CTkLabel(root, text=pokemon3, text_color='black', bg_color='grey', font=('arial', 25))
    Poke3Label = ctk.CTkLabel(root, text="Pokemon 3:", font=('arial', 25))

    Poke4 = ctk.CTkLabel(root, text=pokemon4, text_color='black', bg_color='grey', font=('arial', 25))
    Poke4Label = ctk.CTkLabel(root, text="Pokemon 4:", font=('arial', 25))

    Poke5 = ctk.CTkLabel(root, text=pokemon5, text_color='black', bg_color='grey', font=('arial', 25))
    Poke5Label = ctk.CTkLabel(root, text="Pokemon 5:", font=('arial', 25))

    Poke6 = ctk.CTkLabel(root, text=pokemon6, text_color='black', bg_color='grey', font=('arial', 25))
    Poke6Label = ctk.CTkLabel(root, text="Pokemon 6:", font=('arial', 25))

    # Grid the modules
    Entry.grid(row=1, column=1, columnspan=3, sticky='ew', pady=20)
    label1.grid(row=0, column=2, pady=20)
    PokeSubmit.grid(row=1, column=4, padx=10)

    Poke1Label.grid(row=3, column=1)
    Poke1.grid(row=3, column=2, pady=10)

    Poke2Label.grid(row=4, column=1)
    Poke2.grid(row=4, column=2, pady=10)

    Poke3Label.grid(row=5, column=1)
    Poke3.grid(row=5, column=2, pady=10)

    Poke4Label.grid(row=6, column=1)
    Poke4.grid(row=6, column=2, pady=10)

    Poke5Label.grid(row=7, column=1)
    Poke5.grid(row=7, column=2, pady=10)

    Poke6Label.grid(row=8, column=1)
    Poke6.grid(row=8, column=2, pady=10)

    Replacement.grid(row=9, column=2)
    ReplacementButton.grid(row=9, column=1)

    button.grid(row=9, column=5)

    root.mainloop()

    # END POKEMON PAGE #

# Thank you page :) #

tysm = ctk.CTk()
tysm.geometry("900x200")
tysm.title("Thank You!")
LabelTy = ctk.CTkLabel(tysm, text="Thank you for using our application!", font=('arial', 45))

tysm.columnconfigure(1, weight=1)
tysm.columnconfigure(2, weight=1)
tysm.rowconfigure(1, weight=1)
tysm.rowconfigure(2, weight=1)

LabelTy.grid(row=0, column=0, columnspan=2, sticky='ew')

tysm.mainloop()