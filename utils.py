from inspect import signature

def select_from(iterable, prompt = "Sélection : ", display = None, autosel = True):
    assoc = { i:e for i, e in enumerate(iterable)}
    if len(assoc) == 1 and autosel:
        return assoc[0]
    if not display:
        display = lambda e: assoc[i]
    for i in assoc:
        print(f"[{i}] : {display(assoc[i])}")
    selected = int(input(prompt))
    return assoc[selected]

def listargs2str(list_args):
    return ", ".join([str(e) for e in list_args])

def sig(fun_doc, out = 0):
    if not fun_doc or fun_doc.find('->') < 0:
        return []
    sig = fun_doc.split('->')[out]
    return [T.strip() for T in sig.split(',')]

def find_method_doc(objects, fun_name):
    for o in objects:
        if type(o).__dict__.get(fun_name):
            return type(o).__dict__.get(fun_name).__doc__
    return ""
    

def new_object_name(fun_name, args_names, n, i):
    if n == 1:
        return f"{fun_name}({listargs2str(args_names)})"
    return f"{fun_name}({listargs2str(args_names)})[{i}]"


def encapsulate(f):
    # S'assure que la fonction f renvoie un tuple
    def wrapper(*args):
        rep = f(*args)
        if rep is None:
            return ()
        if not isinstance(rep, tuple):
            return rep,
        return rep
    return wrapper

def count_args(f):
    sig = signature(f)
    return len(sig.parameters)

