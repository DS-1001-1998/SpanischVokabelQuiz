import random
import tkinter as tk
from tkinter import messagebox


spanish_vocabulary = {
    "Haus": "casa",
    "Auto": "coche",
    "Buch": "libro",
    "Apfel": "manzana",
    "Hallo": "hola",
    "Tisch": "mesa",
    "Neu": "nuevo",
    "Schule": "escuela",
    "Weg": "camino",
    "Arbeit": "trabajo",
    "Stadt": "ciudad",
    "Schlüssel": "llave",
    "Hund": "perro",
    "Katze": "gato",
    "Rot": "rojo",
    "Blau": "azul",
    "Grün": "verde",
    "Gelb": "amarillo",
    "Orange": "naranja",
    "Schwarz": "negro",
    "Weiß": "blanco",
    "Garten": "jardín",
    "Mann": "hombre",
    "Frau": "mujer",
    "Kind": "niño",
    "Mädchen": "niña",
    "Schule": "escuela",
    "Bank": "banco",
    "Fenster": "ventana",
    "Stuhl": "silla",
    "Himmel": "cielo",
}

def check_answer(event=None):
    user_translation = entry.get().lower()
    if user_translation == correct_translation:
        messagebox.showinfo("Ergebnis", "Richtig! Gut gemacht.")
        ask_question()
    else:
        messagebox.showerror("Ergebnis", f"Falsch. Die richtige Übersetzung von '{german_word}' ist '{correct_translation}'.")

def ask_question():
    global german_word, correct_translation
    german_word, correct_translation = random.choice(list(spanish_vocabulary.items()))
    label.config(text=f"Was ist die Übersetzung von '{german_word}' ins Spanische?")
    entry.delete(0, tk.END)

# Custom colors for a modern design
background_color = "#f9f7f7"
text_color = "#333333"
button_color = "#4CAF50"

# GUI setup with custom design
root = tk.Tk()
root.title("Spanisch-Vokabel-Quiz")
root.configure(bg=background_color)

label = tk.Label(root, text="", bg=background_color, fg=text_color, font=("Arial", 14, "bold"))
label.place(relx=0.5, rely=0.4, anchor="center")

entry = tk.Entry(root)
entry.place(relx=0.5, rely=0.5, anchor="center")
entry.bind("<Return>", check_answer)

check_button = tk.Button(root, text="Überprüfen", command=check_answer, bg=button_color, fg=text_color)
check_button.place(relx=0.5, rely=0.6, anchor="center")

next_button = tk.Button(root, text="Nächste Frage", command=ask_question, bg=button_color, fg=text_color)
next_button.place(relx=0.5, rely=0.7, anchor="center")

ask_question()
root.mainloop()