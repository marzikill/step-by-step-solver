from utils import select_from

class World:
    def __init__(self):
        self.objects = {}
        self.functions = {}

    def __repr__(self):
        return "".join([f"{name} : {object}\n"
                        for name, object in self.objects.items()])
            
    def affiche(self):
        print(f"\nObjets courants :\n{self}")

    def select_object_name(self):
        return select_from(self.objects)
            
    def add_object(self, object):
        self.objects[object.name] = object

    def del_object(self, object_name):
        return self.objects.pop[object_name]

    def add_function(self, fun_info):
        fun, fun_name, num_args = fun_info
        def fun_with_selection():
            data = [self.objects[self.select_object_name()]
                      for _ in range(num_args)]
            return self.apply_add(fun, data)
        self.functions[fun_name] = fun_with_selection

    def add_method(self, method_info):
        method_name, num_args = method_info
        def method_with_selection():
            object_name = self.select_object_name()
            data = [self.objects[self.select_object_name()]
                    for _ in range(num_args)]
            fun = self.objects.pop(object_name).interface[method_name]
            return self.apply_add(fun, data)
        self.functions[method_name] = method_with_selection

    def apply_add(self, fun, data):
        res = fun(*data)
        for ob in res:
            self.add_object(ob)
        return res
            
