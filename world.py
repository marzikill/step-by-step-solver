from utils import select_from, encapsulate, count_args, build_object_name

class World:
    def __init__(self):
        self.objects = {}
        self.functions = {}
        self.active_data = []

    def __repr__(self):
        return "".join([f"{name} : {object}\n"
                        for name, object in self.objects.items()])
            
    def affiche(self):
        print(f"\nObjets courants :\n{self}")

    # def select_object_name(self):
    #     return select_from(self.objects,
    #                        display= lambda n: f"{n} = {self.objects[n]}")

    def add_object(self, object):
        # print(f"Ajout de {object} de type {type(object)}")
        self.objects[object.name] = object

    def del_object(self, object_name):
        return self.objects.pop[object_name]

    def sel_objects(self, n):
        assert len(self.active_data) == n, f"{self.active_data}, {n}"
        return [self.objects[k] for k in self.active_data]
        # return [self.objects[self.select_object_name()]
        #             for _ in range(n)]

    # def sel_function(self):
    #     return select_from(self.functions,
    #                           prompt = "Action à effectuer : ")

    def add_function(self, fun_info):
        fun, fun_name = fun_info
        num_args = count_args(fun)
        def fun_with_selection():
            data = self.sel_objects(num_args)
            return self.apply_add(fun, data, fun_name = fun_name)
        self.functions[fun_name] = fun_with_selection

    def add_solfunction(self, fun_info, rec_mode, difficulté):
        fun, fun_name = fun_info
        num_args = count_args(fun)
        def fun_seuillée(*args):
            if rec_mode(*args) < difficulté:
                return fun(*args)
            else:
                print("Le problème est trop dur !")
                return None
        def fun_with_selection():
            data = self.sel_objects(num_args)
            return self.apply_add(fun_seuillée, data, fun_name = fun_name)
        self.functions[fun_name] = fun_with_selection

    def add_method(self, fun_name):
        def method_with_selection():
            # object_name = self.select_object_name()
            object_name = self.active_data.pop(0)
            fun = self.objects.pop(object_name).interface[fun_name]
            num_args = count_args(fun)
            data = self.sel_objects(num_args)
            return self.apply_add(fun, data)
        self.functions[fun_name] = method_with_selection

    def apply_add(self, fun, data, fun_name = ""):
        fun = encapsulate(fun)
        res = fun(*data)
        for i, ob in enumerate(res):
            if fun_name:
                args_names = [o.name for o in data]
                ob.name = build_object_name(fun_name,
                                        args_names,
                                        len(res),
                                        i)
            self.add_object(ob)
        return res
