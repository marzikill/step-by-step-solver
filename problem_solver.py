# TODD
# - [ ] ajouter d'autres problèmes
# - [ ] ajouter une fonctionnalité d'annulation
# - [ ] ajouter un nombre maximum d'objets dans World

# - [~] ajouter les docstring des fonctions
# - [~] ajouter une fonctionnalité de destruction d'objet
# - +afficher les docstring dans Problème_minimum.apply_operation+
#   -> ajouter une méthode info
# - [X] une fois le problème de difficulté n résolu, enchaîner avec n + 1
# - [X] rendre la classe Problème plus générale
# - [X] rendre la classe Monde plus générale et supporter d'autres structures de données 
# - [X] ajout de fonctions arbitraires à l'interface de manipulation
# - [X] self.supported_opérations : pas très beau. À déplacer dans World
# - [X] rendre indépendant le processus de sélection et d'action ?
# - [X] se cantoner aux fonction qui ne renvoient q'un élément
# -> plus besoin de mettre des , partout
# -> plus facile de construire le nom des nouveaux éléments
# -> supprimer la composante fun_name : fun.__name__ suffit ?
# - [X] reprendre l'interface du type liste pour virer les q, = sortie(l)
# - [X] reprendre la méthode résoudre de la classe solveur :
# à réécrire

from world import World
from utils import encapsulate, listargs2str

class Problème_Solver:
    def __init__(self, n, problem_description):
        self.problem_desc = problem_description
        self.difficulté = n
        self.solved = False
        self.monde = World()

        # Ajout des fonctions et méthodes du problème
        for fun_info in problem_description["problem_funs"]:
            self.monde.add_function(fun_info)
        for meth_info in problem_description["problem_mets"]:
            self.monde.add_method(meth_info)

        # Ajout des fonctions et méthodes du solveur
        self.monde.add_function(self.resoudre_funinfo())
        solver_funs = [(self.propose_solution, "propose"),
                       (self.info, "info")]
        for fun_info in solver_funs:
            self.monde.add_function(fun_info)


    def __str__(self):
        monde = f"\nObjets courants\n{self.monde}" 
        sol = f"Solution du problème\n{listargs2str(self.sol)}\n"
        return monde + sol


    def generate_problem_data(self):
        in_fun = encapsulate(self.problem_desc["entrée_fun"])
        self.entrée = in_fun(self.difficulté)
        self.monde.objects = {}
        for o in self.entrée:
            self.monde.add_object(o)

        out_fun = encapsulate(self.problem_desc["solution_fun"][0])
        self.sol = out_fun(*self.entrée)


    def info(self):
        print(f""" PROBLÈME {self.problem_desc['name']} (difficulté {self.difficulté}) :
        {self.problem_desc['type']}
        {self.problem_desc['doc']}""")
        return ""


    def vérifie_solution(self, sel):
        print(f"Vérifie : {self.sol} == {sel}")
        return all(sel[i] == self.sol[i] for i in range(len(sel)))
        

    def resoudre_funinfo(self):
        """ Résout le problème pour une difficulté strictement
        inférieure à la difficulté actuelle. """
        fun, fun_name = self.problem_desc["solution_fun"]

        def fun_cas_plus_simples(*args):
            if len(args[0]) < self.difficulté:
                return fun(*args)
            else:
                print("Le problème est trop dur !")
                return None

        return fun_cas_plus_simples, fun_name

    def propose_solution(self):
        """ Sélectionne un objet et vérifie qu'il s'agit d'une
        solution du problème. """
        sel = self.monde.sel_objects(len(self.sol))
        sel_str = ", ".join([o.name for o in sel])

        print(f"Réponse proposée : {sel}\nRéponse attendue : {self.sol}")
        if self.vérifie_solution(sel):
            print("Bravo vous avez résolu le problème !")
            print(f"Propose : {sel_str}")
            self.solved = True
        else:
            print("Ça n'est pas la bonne réponse, il faut continuer...")
        return None

    def select_apply_operation(self):
        print(self)
        op_name = self.monde.sel_function()
        op = self.monde.functions[op_name]
        op()

    def joue(self):
        self.generate_problem_data()
        self.solved = False
        while not self.solved:
            self.select_apply_operation()
        return self.solved
