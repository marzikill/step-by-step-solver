# TODD
# - [ ] se cantoner aux fonction qui ne renvoient q'un élément
# -> plus besoin de mettre des , partout
# -> plus facile de construire le nom des nouveaux éléments
# -> supprimer la composante fun_name : fun.__name__ suffit ?
# - [ ] reprendre l'interface du type liste pour virer les q, = sortie(l)
# - [ ] reprendre la méthode résoudre de la classe solveur :
# à réécrire
# - [ ] ajouter d'autres problèmes
# - [ ] ajouter une fonctionnalité d'annulation
# - [ ] résoudre : pas très belle
# - ajouter un nombre maximum d'objets dans World

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

from world import World
from utils import select_from, listargs2str

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
        solver_funs = [(self.propose_solution, "propose", 0),
                       (self.info, "info", 0)]
        for fun_info in solver_funs:
            self.monde.add_function(fun_info)



    def __str__(self):
        monde = f"\nObjets courants\n{self.monde}" 
        sol = f"Solution du problème\n{self.sol}\n"
        return monde + sol


    def generate_problem_data(self):
        self.entrée = self.problem_desc["entrée_fun"](self.difficulté)
        self.sol, = self.problem_desc["solution_fun"][0](*self.entrée)

        self.monde.objects = {}
        for o in self.entrée:
            self.monde.add_object(o)


    def info(self):
        print(f""" PROBLÈME {self.problem_desc['name']} (difficulté {self.difficulté}) :
        {self.problem_desc['type']}
        {self.problem_desc['doc']}""")
        return ""
        # op_name = select_from(self.supported_opérations,
        #                       prompt = "Informations sur : ")
        # info = self.supported_opérations[op_name].__doc__
        # print(info)
        # return info


    def vérifie_solution(self, solution):
        return self.sol == solution
        

    def resoudre_funinfo(self):
        """ Résout le problème pour une difficulté strictement
        inférieure à la difficulté actuelle. """
        fun, fun_name, num_args = self.problem_desc["solution_fun"]
        def fun_cas_plus_simples():
            ob_name = self.monde.select_object_name()
            ob = self.monde.objects[ob_name]
            if len(ob) < self.difficulté:
                data_names = [self.monde.select_object_name()
                              for _ in range(num_args - 1)]
                data = [self.monde.objects[name] for name in data_names]
                args = [ob] + data
                args_names = [ob_name] + data_names
                sol_aux, = fun(*args)
                sol_aux.name = f"{fun_name}({listargs2str(args_names)})"
                self.monde.add_object(sol_aux)
                return [sol_aux]
            else:
                print("Le problème est trop dur !")
                return []
        return fun_cas_plus_simples, fun_name, 0


    def propose_solution(self):
        """ Sélectionne un objet et vérifie qu'il s'agit d'une
        solution du problème. """
        ob = self.monde.objects[self.monde.select_object_name()]
        print(f"Réponse proposée : {ob}\nRéponse attendue : {self.sol}")
        if self.vérifie_solution(ob):
            print("Bravo vous avez résolu le problème !")
            self.solved = True
        else:
            print("Ça n'est pas la bonne réponse, il faut continuer...")
        return []

    def select_apply_operation(self):
        print(self)
        op_name = select_from(self.monde.functions,
                              prompt = "Action à effectuer : ")
        op = self.monde.functions[op_name]
        op()

    def joue(self):
        self.generate_problem_data()
        self.solved = False
        while not self.solved:
            self.select_apply_operation()
        return self.solved


def lance_partie(probleme):
    """ int -> int
    Renvoie le nombre suivant """
    difficulté = 0
    P = Problème_Solver(0)
    while P.joue():
        difficulté += 1
        P = Problème_Solver(difficulté)
    return True

# P = Problème_Solver(5, problème_desc)
# P.joue()
