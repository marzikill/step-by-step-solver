from tkinter import *
from tkinter import ttk
from problem_solver import ProblemIndex, ProblemInstance, InputException, OutputException

window = Tk()
window.title("Bac à sable algorithmique")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

mainframe = LabelFrame(window, bd = 10)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=0, minsize=200)
mainframe.columnconfigure(1, weight=1)

def get_selection(lst):
    """ Listbox | OrderedTreeview -> str
    Renvoie le problème sélectionné par l'utilisateur. """
    if isinstance(lst, OrderedTreeview):
        return lst.selected_items

    idx = lst.curselection()
    if len(idx) == 1:
        idx = int(idx[0])
        return lst.get(idx)
    return ""

class PanneauChoix:
    def __init__(self, parent, controller):
        self.controller = controller 
        # Menu de choix
        panel = LabelFrame(parent, text="Choix du problème",
                                bd=10,
                                width=100,
                                height=200,
                                background="yellow")
        panel.grid(column=0, row=0, sticky=(N, W, E, S))
        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(0, weight=1)

        choices = StringVar(value=[pb_name for pb_name in ProblemIndex])
        self.liste_problèmes = Listbox(panel,
                                       listvariable=choices,
                                       exportselection=0)
        self.liste_problèmes.grid(column=0, row=0, sticky=(N, W, E, S))

        self.load_button = ttk.Button(panel,
                                      text='Charger',
                                      command=lambda: self.send_problem())
        self.load_button.grid(column=0, row=1, sticky=(N, W, E, S))

    def send_problem(self):
        self.controller.load_problem(get_selection(self.liste_problèmes))

class OrderedTreeview(ttk.Treeview):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.selected_items = []
        self.bind("<<TreeviewSelect>>", self.on_select)

    def on_select(self, event):
        """
        Custom method to keep track of the selected items in order.
        """
        # Clear the list and add selected items in the order of selection
        news = [self.item(item, "values")[0] for item in self.selection()]
        last = set(news).symmetric_difference(set(self.selected_items)).pop()
        if last not in self.selected_items:
            self.selected_items.append(last)
        else:
            self.selected_items.pop(self.selected_items.index(last))

    def get_selection(self):
        return self.selected_items

class PanneauRésolution:
    def __init__(self, parent, controller):
        self.controller = controller

        # Menu de résolution
        panel = LabelFrame(mainframe, text="Résolution du problème",
                                bd=10,
                                width = 200,
                                height = 200,
                                background="blue")
        panel.grid(column=1, row=0, sticky=(N, W, E, S))

        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(0, weight=1)
        panel.rowconfigure(1, weight=1)
        panel.rowconfigure(2, weight=1)

        panel_1 = LabelFrame(panel, text="Données du problème",
                                bd=10,
                                width = 200,
                                height = 200,
                                background="green")
        panel_1.grid(column=0, row=0, sticky=(N, W, E, S))
        panel_1.columnconfigure(0, weight=1)
        panel_1.rowconfigure(0, weight=1)

        self.donnees = OrderedTreeview(panel_1,
                                       columns=("var", "data"), show="headings")
        self.donnees.heading('var', text='Variable')
        self.donnees.heading('data', text='Contenu')
        self.donnees.grid(column=0, row=0, sticky=(N, W, E, S))
        
        panel_2 = LabelFrame(panel, text="Solutions du problème",
                                bd=10,
                                width = 200,
                                height = 200,
                                background="red")
        panel_2.grid(column=0, row=1, sticky=(N, S, W, E))
        panel_2.columnconfigure(0, weight=1)
        panel_2.rowconfigure(0, weight=1)
        self.solution = Listbox(panel_2, exportselection=0)
        self.solution.grid(column=0, row=0, sticky=(N, W, E, S))

        panel_3 = LabelFrame(panel, text="Interface du problème",
                                bd=10,
                                width = 200,
                                height = 200,
                                background="white")
        panel_3.grid(column=0, row=2, sticky=(N, S, W, E))
        panel_3.columnconfigure(0, weight=1)
        panel_3.columnconfigure(1, weight=1)
        panel_3.rowconfigure(0, weight=1)
        panel_3.rowconfigure(1, weight=1)
        self.interface = Listbox(panel_3, exportselection=0)
        self.interface.grid(column=0, columnspan=2, row=0, sticky=(N, W, E, S))
        validate_button = Button(panel_3, text = "Valider",
                                 command=lambda : self.send_sel())
        validate_button.grid(column=0, row=1, sticky=(N, W, E, S))
        help_button = Button(panel_3, text = "Documentation",
                                 command=lambda : print("help"))
        help_button.grid(column=1, row=1, sticky=(N, W, E, S))


    def load_problem(self, pb):
        pb_name = pb.problem.name
        print("Chargement des données du problème", pb_name)
        for ob in pb.objects():
            print(ob)
            self.donnees.insert("", "end", values = ob)

        print("Chargement de la solution du problème", pb_name)
        for ob in pb.sol:
            self.solution.insert('end', ob)

        print("Chargement de l'interface du problème", pb_name)
        for fun, doc in pb.functions():
            self.interface.insert('end', fun)

    def reset_problem(self):
        for item in self.donnees.get_children():
            self.donnees.delete(item)
        self.solution.delete(0, 'end')
        self.interface.delete(0, 'end')

    def update(self, pb):
        self.reset_problem()
        self.load_problem(pb)

    def send_sel(self):
        """ Renvoie un tuple :
        ((objet_name1, objet_name2, ...), fonction_nom)"""
        info = get_selection(self.donnees), get_selection(self.interface)
        self.controller.send_data(info)

class ProblemSolverController:
    def __init__(self):
        self.choose_pb_pane = PanneauChoix(mainframe, self)
        self.pb_pane = PanneauRésolution(mainframe, self)
        self.pb = None
        self.selected_pb = None

    def load_problem(self, choice):
        """ (re)Charge le problème sélectionné """
        self.selected_pb = choice
        self.pb = ProblemInstance(5, ProblemIndex[choice])
        self.pb_pane.update(self.pb)

    def send_data(self, info):
        """ Applique la sélection de l'utilisateur et réinitialise 
        la sélection des données. La fonction sélectionnée est 
        réinitialisée dans le cas où l'appel est effectué avec succès. """
        data_names, fun_name = info
        print(info)
        try:
            self.pb.select_apply_operation(fun_name, data_names)
        except (ValueError, TypeError, RecursionError, AttributeError, OutputException) as e:
            # self.view.popup(e.__str__())
            print(e)
        except InputException as e:
            # Todo : inplémentener un popup demandant une entrée utilisateur
            a = (42, "ma variable")
            self.pb.make_input(e, a)
        self.pb_pane.update(self.pb)

P = ProblemSolverController()

window.mainloop()
