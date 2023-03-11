def select_from(iterable, prompt = "Sélection : "):
    assoc = { i:name for i, name in enumerate(iterable)}
    for i in assoc:
        print(f"[{i}] : {assoc[i]}")
    selected = int(input(prompt))
    return assoc[selected]

def listargs2str(list_args):
    return ", ".join([str(e) for e in list_args])
