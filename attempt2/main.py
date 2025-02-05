import customtkinter as ctk
import tkinter as tk
import hashlib
import pandas as pd

# Login Window #


def CheckDataframeEmpty():
    if data.empty is True:
        return False  # DataFrame is empty #
    else:
        return True  # DataFrame is NOT empty #


def UserPassword():
    global data, success, Username
    Username = UserEntry.get()
    Password = PassEntry.get()
    Password = hashlib.sha256(Password.encode('utf-8')).hexdigest()  # Encryption :) #
    print(Password)
    UserEntry.delete(0, tk.END)
    PassEntry.delete(0, tk.END)
    with open('attempt2/passwords.csv', 'r') as file:
        data = pd.read_csv(file)
        data = data.loc[data['Username'] == Username]  # Username as input #
        data = data.loc[data['password'] == Password]  # Password as input #

        result = CheckDataframeEmpty()
        if result == False:
            FailLabel.configure(text="Invalid Username or Password", text_color='red')  # LOUD INCORRECT BUZZER #
        else:
            FailLabel.configure(text="Success", text_color='lime')  # LOUD CORRECT BUZZER #
            success = True
            login.destroy()


# Variables
success = False

login = ctk.CTk()
login.geometry('250x200')
login.title("Login Page")

# Config #
login.rowconfigure(3, weight=0)
login.rowconfigure(4, weight=1)

# Modules #
UserEntry = ctk.CTkEntry(login)
PassEntry = ctk.CTkEntry(login)
UserLabel = ctk.CTkLabel(login, text="Username:")
PassLabel = ctk.CTkLabel(login, text="Password:")
FailLabel = ctk.CTkLabel(login, text="Input Username and password")

LoginButton = ctk.CTkButton(login, text="Input", command=UserPassword)

# Grid the Modules #

UserLabel.grid(row=0, column=0, padx=10)
UserEntry.grid(row=0, column=1)
PassLabel.grid(row=1, column=0, pady=20, padx=10)
PassEntry.grid(row=1, column=1)

LoginButton.grid(row=2, column=0, columnspan=2, sticky='ew')

FailLabel.grid(row=3, column=0, columnspan=2, sticky='ew', pady=20)

login.mainloop()

# END LOGIN #

# POKEDEX #


def FindPokemon():
    with open('attempt2/passwords.csv', 'r') as file:
        global pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6
        data = pd.read_csv(file)
        data = data.loc[data['Username'] == Username]
        pokemon1 = data.iloc[0]['poke1']
        pokemon2 = data.iloc[0]['poke2']
        pokemon3 = data.iloc[0]['poke3']
        pokemon4 = data.iloc[0]['poke4']
        pokemon5 = data.iloc[0]['poke5']
        pokemon6 = data.iloc[0]['poke6']
        print(pokemon1)


if success is True:
    pokedex = ctk.CTk()
    pokedex.geometry('800x800')
    pokedex.title("Pokedex")

    # Config #
    pokedex.columnconfigure(2, weight=1)
    pokedex.columnconfigure(3, weight=1)

    # Modules #
    # Input Boxes#
    PokeInput = ctk.CTkEntry(pokedex) # Input Pokemon here #
    SlotInput = ctk.CTkEntry(pokedex) # Input Slot Number here #

    # Buttons #
    PokeButton = ctk.CTkButton(pokedex, text="Input Pokemon Here")
    SlotButton = ctk.CTkButton(pokedex, text="Input Slot Number Here")

    # Labels #
    PokeLabel = ctk.CTkLabel(pokedex, text='Input Pokemon ID or name here')
    SlotLabel = ctk.CTkLabel(pokedex, text='Input the slot you want to replace')
    FindPokemon()
    
    LabelList = []
    for i in range(6):  # Create 6 labels for the 6 Pokemon
        LabelList.append(ctk.CTkLabel(pokedex, text=f"Pokemon {i + 1}:"))

    # Create labels for each Pokemon
    PokeList = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6]
    PokeLabelList = []
    for i in range(6):  # Create 6 labels for the 6 Pokemon
        PokeLabelList.append(ctk.CTkLabel(pokedex, text=f"{PokeList[i]}"))

    for i, label in enumerate(LabelList):
        label.grid(row=i+2, column=0, pady=5, padx=10)

    for i, label2 in enumerate(PokeLabelList):
        label2.grid(row=i+2, column=1, pady=5, padx=10)

    # Grid the module #
    PokeLabel.grid(row=0, column=0, pady=20, padx=10)
    PokeInput.grid(row=0, column=1, padx=10)
    PokeButton.grid(row=0, column=2, columnspan=2, sticky='ew', padx=10)

    SlotLabel.grid(row=1, column=0, padx=10)
    SlotInput.grid(row=1, column=1, padx=10)
    SlotButton.grid(row=1, column=2, padx=10, columnspan=2, sticky='ew')

    pokedex.mainloop()