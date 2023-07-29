import pickle

def getlogo(fname: str) -> str:
    with open(f"./{fname}.pkl", mode="rb") as f:
        content = f.read()
    logo = pickle.loads(content)
    return logo
