import re
from utils import encapsulate, count_args, new_object_name, sig, find_method_doc

class World:
    def __init__(self):
        self.objects = {}
        self.functions = {}
        self.functions_sig = {}
        self.docs = {}
        self.active_data = []

    def object_names(self):
        return [f"{name} : {object}" for name, object in self.objects.items()]

    def fun_names(self):
        return [fun_name for fun_name in self.functions]

    def add_object(self, object):
        self.objects[object.name] = object

    def del_object(self, object_name):
        return self.objects.pop[object_name]

    def get_check_sel_objects(self, fun_name, n, drop_self=False):
        """ Renvoie les objets actifs en vérifiant que ceux-ci sont compatibles
        en tant qu'arguments pour la fonction """
        if not len(self.active_data) == n:
            raise ValueError(f"{n} arguments attendus, {len(self.active_data)} actifs.")
        data = [self.objects[k] for k in self.active_data]
        if not all([o.__class__.__name__ == T
                    for o, T in zip(data, self.functions_sig[fun_name])]):
            raise TypeError(f"Les arguments sélectionnés n'ont pas le bon type")
                            # self.functions_sig[fun_name],
                            # [(o.__class__.__name__, T)
                            #  for o, T in zip(data, self.functions_sig[fun_name])])
        self.active_data = []
        return data

    def add_function(self, fun_info, num_args=None):
        fun, fun_name = fun_info
        num_args = count_args(fun) if not num_args else num_args
        def fun_with_selection():
            data = self.get_check_sel_objects(fun_name, num_args)
            return self.apply_add(fun, data, fun_name = fun_name)
        self.register_fun(fun_with_selection, fun_name, fun.__doc__)

    def add_solfunction(self, fun_info, rec_mode, difficulté):
        """ Lorsque rec_mode est défini, il est possible d'appeler 
        la fonction solution du problème lorsque celle-ci opère sur 
        des objets de taille inférieure à la difficulté du problème. """
        fun, fun_name = fun_info
        num_args = count_args(fun)
        def fun_seuillée(*args):
            if rec_mode(*args) < difficulté:
                return fun(*args)
            else:
                raise RecursionError("Le problème est trop dur")
        def fun_with_selection():
            data = self.get_check_sel_objects(fun_name, num_args)
            return self.apply_add(fun_seuillée, data, fun_name = fun_name)
        self.register_fun(fun_with_selection, fun_name, fun.__doc__)

    def add_method(self, meth_name):
        """ Les méthodes 'consomment' les objets auxquelles elles s'appliquent. """
        def method_with_selection():
            try:
                object_name = self.active_data.pop(0)
            except IndexError:
                raise ValueError("Aucun objet n'est sélectionné. ")
            try:
                fun = self.objects[object_name].interface[meth_name]
            except AttributeError:
                raise AttributeError(f"{meth_name} ne s'applique pas à {object_name}")
            num_args = count_args(fun)
            data = self.get_check_sel_objects(meth_name, num_args, drop_self=True)
            # On supprime l'objet une fois que tout est vérifié
            self.objects.pop(object_name)
            return self.apply_add(fun, data)
        doc = find_method_doc(self.objects.values(), meth_name)
        self.register_fun(method_with_selection, meth_name, doc, drop_self=True)

    def register_fun(self, fun, fun_name, fun_doc, drop_self=False):
        if not fun_doc:
            fun_doc = 'Documentation manquante'
        self.functions[fun_name] = fun
        self.functions_sig[fun_name] = sig(fun_doc) if not drop_self else sig(fun_doc)[1:]
        fun_doc = re.sub('\n\s+', '\n ', fun_doc)
        self.docs[fun_name] = f"{fun_name} :\n{fun_doc}"


    def apply_add(self, fun, data, fun_name = ""):
        fun = encapsulate(fun)
        res = fun(*data)
        for i, ob in enumerate(res):
            if fun_name:
                args_names = [o.name for o in data]
                ob.name = new_object_name(fun_name,
                                        args_names,
                                        len(res),
                                        i)
            self.add_object(ob)
        return res
