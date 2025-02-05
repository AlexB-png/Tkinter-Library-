from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter as tk
import pandas as pd
import webbrowser
import requests
import json
import os
from tkinter import *
from PIL import Image, ImageTk
import hashlib

# Variables
UserInputField = ''
Password = ''
fail = False
success = False
PokemonJSON = {}
InvalidSlot = False

def LoginInput():
    global UserInput, Password
    UserInput = UserName.get()
    UserInput = UserInput.lower()
    Password = PassName.get()

    # Hash the password consistently using SHA-256
    Password = hashlib.sha256(Password.encode('utf-8')).hexdigest()

    UserName.delete(0, tk.END)
    PassName.delete(0, tk.END)
    try:
        with open('Pokedex/passwords.csv', 'r') as file:
            data = pd.read_csv(file, index_col=False)
            pd.DataFrame(data)
            data = (data.loc[data['Username'] == UserInput])
            data = (data.loc[data['password'] == Password])
            if data.empty is True:
                LoginfailLabel.configure(text="Invalid Username or Password", text_color='red')
            else:
                global pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6
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


def CheckIfOnline(url):
    global fail, PokemonJSON
    url_response = requests.get(url)
    if url_response.status_code != 200:
        os.system('cls')
        print("Server does not exist")
        fail = True
    else:
        data = url_response.json()
        PokemonJSON = data
        fail = False


def replace():
    global PokemonJSON, InvalidSlot
    slot = Replacement.get()
    try:
        slot = int(slot)
        if slot < 1 or slot > 6:
            print("Invalid slot number")
            InvalidSlot = True
        else:
            InvalidSlot = False
            print("Slot number is correct")
    except ValueError:
        print("Invalid slot number")
        return
    Replacement.delete(0, tk.END)
    PokeSelector = Entry.get()
    Entry.delete(0, tk.END)
    PokeInputVar = f"https://pokeapi.co/api/v2/pokemon/{PokeSelector}"
    CheckIfOnline(PokeInputVar)
    if fail is False:
        global PokemonName, PokemonSprite
        PokemonName = PokemonJSON["name"]
        PokemonSprite = PokemonJSON["sprites"]["front_default"]

        if InvalidSlot is False:
            print(f'slot{slot} has been replaced')
            with open('Main/passwords.csv', 'r') as file:
                data = pd.read_csv(file, index_col=False)
                data.loc[data['Username'] == UserInput, f'poke{slot}'] = PokemonName
            with open('Main/passwords.csv', 'w') as file:
                data.to_csv(file, index=False)
            poke_label_name = f"pokemon{slot}"
            globals()[poke_label_name].configure(text=PokemonName)

# LOGIN WINDOW #
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
LoginfailLabel = ctk.CTkLabel(login, text="Input Username and Password")

UserName = ctk.CTkEntry(login, height=50)
PassName = ctk.CTkEntry(login, height=50)

LoginButton = ctk.CTkButton(login, text="Login", command=LoginInput, height=30)

# Grid the modules
UserLabel.grid(row=0, column=0)
PassLabel.grid(row=1, column=0, pady=50)

UserName.grid(row=0, column=1, sticky='ew')
PassName.grid(row=1, column=1, pady=0, sticky='ew')

LoginButton.grid(row=2, column=0, columnspan=2, pady=10, sticky='ew')

LoginfailLabel.grid(row=3, column=0, columnspan=2, pady=10)

login.mainloop()

# POKEMON PAGE #
if success == True:
    root = ctk.CTk()
    root.geometry("750x550")

    # Initialize label references for Pokemon
    labels = []

    pokemon_list = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6]
    for i, pokemon in enumerate(pokemon_list, start=1):
        poke_label = ctk.CTkLabel(root, text=pokemon, text_color='black', bg_color='grey', font=('arial', 25))
        poke_label.grid(row=i+1, column=1, padx=10, pady=5)
        poke_label_name = ctk.CTkLabel(root, text=f"Pokemon {i}:", font=('arial', 25))
        poke_label_name.grid(row=i+1, column=0, padx=10, pady=5)

        # Store the created label reference
        labels.append(poke_label)

    # Custom Button Image #
    original_image = Image.open('Main/poke.png')
    resized_image = original_image.resize((100, 100))
    click_btn = ImageTk.PhotoImage(resized_image)
    CustomButton = tk.Button(root, image=click_btn)
    CustomButton.image = click_btn  # Save reference to prevent garbage collection
    CustomButton.grid(row=8, column=3)

    PokeSubmit = ctk.CTkButton(root, text="Clear", height=50)
    label1 = ctk.CTkLabel(root, text="Input Pokemon")
    Entry = ctk.CTkEntry(root, height=50)

    Replacement = ctk.CTkEntry(root)
    ReplacementButton = ctk.CTkButton(root, text="Replace pokemon slot:", height=25, command=replace)

    # Grid the modules
    Entry.grid(row=1, column=1, columnspan=3, sticky='ew', pady=20)
    label1.grid(row=0, column=2, pady=20)
    PokeSubmit.grid(row=1, column=4, padx=10)
    Replacement.grid(row=9, column=2)
    ReplacementButton.grid(row=9, column=1)

    root.mainloop()
