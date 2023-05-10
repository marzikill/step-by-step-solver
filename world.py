class World:
    def __init__(self):
        self.objects = {}
        self.functions = {}
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

    def get_selection(self):
        data = [self.objects[k] for k in self.active_data]
        self.active_data = []
        return data

    def add_function(self, fun):
        def fun_with_selection():
            data = self.get_selection()
            res = fun(*data)
            for o in res:
                self.add_object(o)
            return res
        self.register_fun(fun_with_selection, fun.name, fun.signature_str + fun.doc)

    def register_fun(self, fun, fun_name, fun_doc):
        if not fun_doc:
            fun_doc = 'Documentation manquante'
        self.functions[fun_name] = fun
        self.docs[fun_name] = f"{fun_name} :\n{fun_doc}"
