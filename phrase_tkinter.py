import tkinter as tk

def phrase():
    prenom = champ_nom.get()
    texte = "Bonjour " + prenom
    label_phrase.config(text=texte)

fenetre = tk.Tk()

champ_nom = tk.Entry(fenetre)
champ_nom.pack()

bouton = tk.Button(fenetre, text="Faire la phrase.", command=phrase)
bouton.pack()

label_phrase = tk.Label(fenetre, text="")
label_phrase.pack()

fenetre.mainloop()