def select_from(iterable, prompt = "Sélection : ", display = None):
    assoc = { i:e for i, e in enumerate(iterable)}
    if not display:
        display = lambda e: assoc[i]
    for i in assoc:
        print(f"[{i}] : {display(assoc[i])}")
    selected = int(input(prompt))
    return assoc[selected]

def listargs2str(list_args):
    return ", ".join([str(e) for e in list_args])

def build_object_name(fun_name, args_names, n, i):
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

# @encapsulate
# def f(x):
#     return x + 1

# @encapsulate
# def g(x):
#     return x + 1, x + 2

# print(f(1))
# print(g(1))
