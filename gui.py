from tkinter import *
from tkinter import ttk

window =Tk()
window.title("Bac à sable algorithmique")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

mainframe = LabelFrame(window, bd = 10)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=0, minsize=200)
mainframe.columnconfigure(1, weight=1)


class PanneauChoix:
    def __init__(self, parent):
        # Menu de choix
        left_panel = LabelFrame(parent, text="Choix du problème",
                                bd=10,
                                width=100,
                                height=200,
                                background="yellow")
        left_panel.grid(column=0, row=0, sticky=(N, W, E, S))
    

class PanneauRésolution:
    def __init__(self, parent):
        # Menu de résolution
        right_panel = LabelFrame(mainframe, text="Résolution du problème",
                                bd=10,
                                width = 200,
                                height = 200,
                                background="blue")
        right_panel.grid(column=1, row=0, sticky=(N, W, E, S))

        right_panel.columnconfigure(0, weight=1)
        right_panel.rowconfigure(0, weight=1)
        right_panel.rowconfigure(1, weight=1)
        right_panel.rowconfigure(2, weight=1)

        right_panel_1 = LabelFrame(right_panel, text="Données du problème",
                                bd=10,
                                width = 200,
                                height = 200,
                                background="green")
        right_panel_1.grid(column=0, row=0, sticky=(N, W, E, S))
        right_panel_2 = LabelFrame(right_panel, text="Solutions du problème",
                                bd=10,
                                width = 200,
                                height = 200,
                                background="red")
        right_panel_2.grid(column=0, row=1, sticky=(N, S, W, E))

        right_panel_3 = LabelFrame(right_panel, text="Interface du problème",
                                bd=10,
                                width = 200,
                                height = 200,
                                background="white")
        right_panel_3.grid(column=0, row=2, sticky=(N, S, W, E))

        
left = PanneauChoix(mainframe)
right = PanneauRésolution(mainframe)
# # Liste des problèmes
# liste_lang =Listbox(left_panel)
# for l in ["Python", "php", "java"]:
#     liste_lang.insert(0, l)
# liste_lang.grid(row=0, column = 0, sticky="ew")

# # Boutons de la liste
# frm_buttons =Frame(left_panel)
# btn_info =Button(frm_buttons, text="Infos", width = 10, command=fun_btn_info)
# btn_load =Button(frm_buttons, text="Charger", width = 10, command=fun_btn_load)
# btn_info.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# btn_load.grid(row=0, column=1, sticky="ew", padx=5)

# frm_buttons.grid(row=1, column=0, sticky="ns")
# left_panel.grid(row=0, column=0, sticky="nsew")

# # Manipulations
class RightPane:
    def __init__(self, parent, control):
        self.initial_args = (parent, control)
        root = LabelFrame(parent, bd = 10, background="green")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Affichage des objets de la liste controlobjets
        # controlobjets = [("liste1", (1, 5, 3)), ("entier1", 1)]
        # self.liste_objets = ttk.Treeview(root, columns = ('Nom', 'Objet'), show='headings')
        # self.liste_objets.heading('Nom', text='Nom')
        # self.liste_objets.heading('Objet', text='Objet')
        # for e in controlobjets:
        #     self.liste_objets.insert('',END, values=e)
        # self.liste_objets.grid(row=0,column=0, sticky=(N, W, E, S))

        # Affichage de la solution

        # Affichage et gestion de l'interface
        self.liste_interface = Listbox(root, bd = 5)
        self.liste_interface.grid(row=0, column=0, sticky=(N, W, E, S))
        # for l in ["divise", "propose", "info"]:
        #     self.liste_interface.insert(0, l)
        # self.btn_select = Button(root, text = "Appliquer", command=self.select_fun)
        # self.btn_select.grid(row=2, column=0, sticky="nsew")

        root.grid(row=0, column=0, sticky=(N, W, E, S))

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
        

# p2 = RightPane(right_panel, None)

window.mainloop()
