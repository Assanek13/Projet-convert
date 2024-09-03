import tkinter as tk
from tkinter import messagebox

def convertir():
    try:
        binaire = entree_binaire.get()
        # Vérifie si la chaîne contient des chiffres binaires
        if not all(char in '01' for char in binaire):
            raise ValueError("La chaîne binaire est invalide.")

        # Conversion du binaire en décimal
        decimal = int(binaire, 2)
        hexadecimal = hex(decimal).upper().replace("0X", "")

        # Affichage des résultats
        label_decimal.config(text=f"Décimal: {decimal}")
        label_hexadecimal.config(text=f"Hexadécimal: {hexadecimal}")
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Convertisseur binaire")

# Création des widgets
label_instruction = tk.Label(fenetre, text="Entrez un nombre binaire:")
label_instruction.pack(pady=5)

entree_binaire = tk.Entry(fenetre)
entree_binaire.pack(pady=5)

bouton_convertir = tk.Button(fenetre, text="Convertir", command=convertir)
bouton_convertir.pack(pady=5)

label_decimal = tk.Label(fenetre, text="Décimal: ")
label_decimal.pack(pady=5)

label_hexadecimal = tk.Label(fenetre, text="Hexadécimal: ")
label_hexadecimal.pack(pady=5)

# Démarrage de la boucle principale
fenetre.mainloop()
