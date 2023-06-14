import tkinter as tk
from tkinter import ttk

def fun_btn_info():
    pass

def fun_btn_load():
    pass

def fun_btn_select(event):
    print("Hello")

window = tk.Tk()
window.title("Bac à sable algorithmique")

# Menu de choix
left_panel = tk.LabelFrame(window, text="Choix du problème", bd=5)

# Liste des problèmes
liste_lang = tk.Listbox(left_panel)
for l in ["Python", "php", "java"]:
    liste_lang.insert(0, l)
liste_lang.grid(row=0, column = 0, sticky="ew")

# Boutons de la liste
frm_buttons = tk.Frame(left_panel)
btn_info = tk.Button(frm_buttons, text="Infos", width = 10, command=fun_btn_info)
btn_load = tk.Button(frm_buttons, text="Charger", width = 10, command=fun_btn_load)
btn_info.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_load.grid(row=0, column=1, sticky="ew", padx=5)

frm_buttons.grid(row=1, column=0, sticky="ns")
left_panel.grid(row=0, column=0, sticky="ns")

# Manipulations
class RightPane:
    def __init__(self, window, control):
        self.initial_args = (window, control)
        self.root = tk.Frame(window)

        # Affichage des objets de la liste controlobjets
        controlobjets = [("liste1", (1, 5, 3)), ("entier1", 1)]
        self.liste_objets = ttk.Treeview(self.root, columns = ('Nom', 'Objet'), show='headings')
        self.liste_objets.heading('Nom', text='Nom')
        self.liste_objets.heading('Objet', text='Objet')
        for e in controlobjets:
            self.liste_objets.insert('', tk.END, values=e)
        self.liste_objets.grid(row=0,column=1)

        # Affichage de la solution

        # Affichage et gestion de l'interface
        self.liste_interface = tk.Listbox(self.root, bd = 5)
        for l in ["divise", "propose", "info"]:
            self.liste_interface.insert(0, l)
        self.liste_interface.grid(row=2, column=1, sticky="nsew")
        self.btn_select = tk.Button(self.root, text = "Appliquer", command=self.select_fun)

        self.btn_select.grid(row=3, column=1, sticky="nsew")
        self.root.grid(row=0, column=1, sticky="nsew")

    def select_fun(self):
        idx = self.liste_interface.curselection()
        self.reset()
        self.liste_interface.itemconfig(idx,
                                        foreground='#84A7A1',
                                        selectforeground='#84A7A1',
                                        background='#1F6E8C',
                                        selectbackground='#1F6E8C')
        return self.liste_interface.get(idx)

    def reset(self):
        self.__init__(*self.initial_args)
        

p2 = RightPane(window, None)

window.mainloop()
