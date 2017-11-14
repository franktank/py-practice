Inputs:
    (string list) l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
Output:
    (string list) ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]


def answer(l):
    # your code here
    res = []
    for element in l:
        res.append(element.split("."))
    res = [[int(i) for i in e] for e in res]
    res.sort()
    res = [[str(i) for i in e] for e in res]
    return [".".join(i) for i in res]
