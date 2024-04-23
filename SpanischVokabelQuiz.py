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

class RoundedButton(tk.Button):
    def __init__(self, master=None, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.config(relief=tk.FLAT)
        self.config(borderwidth=0)
        self.config(bg="#4CAF50")  
        self.config(fg="#ffffff")  
        self.config(font=("Arial", 12, "bold"))  
        self.config(cursor="hand2") 
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.config(bg="#449d44") 

    def on_leave(self, event):
        self.config(bg="#4CAF50") 

def check_answer(event=None):
    user_translation = entry.get().lower()
    if user_translation == correct_translation:
        messagebox.showinfo("Ergebnis", "Richtig! Gut gemacht.", icon="info")
        ask_question()
    else:
        messagebox.showerror("Ergebnis", f"Falsch. Die richtige Übersetzung von '{german_word}' ist '{correct_translation}'.", icon="error")

def ask_question():
    global german_word, correct_translation
    german_word, correct_translation = random.choice(list(spanish_vocabulary.items()))
    label.config(text=f"Was ist die Übersetzung von '{german_word}' ins Spanische?")
    entry.delete(0, tk.END)

background_color = "#f9f7f7"
text_color = "#333333"

root = tk.Tk()
root.title("Spanisch-Vokabel-Quiz")
root.configure(bg=background_color)

label = tk.Label(root, text="", bg=background_color, fg=text_color, font=("Arial", 14, "bold"))
label.place(relx=0.5, rely=0.4, anchor="center")

entry = tk.Entry(root)
entry.place(relx=0.5, rely=0.5, anchor="center")
entry.bind("<Return>", check_answer)

check_button = RoundedButton(root, text="Überprüfen", command=check_answer)
check_button.place(relx=0.5, rely=0.6, anchor="center")

next_button = RoundedButton(root, text="Nächste Frage", command=ask_question)
next_button.place(relx=0.5, rely=0.7, anchor="center")

ask_question()
root.mainloop()
