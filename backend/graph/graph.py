from typing import List, Dict


def get_graph(txt_input: str) -> Dict[str, List[str]]:

    graph = {}
    txt_input = txt_input.replace(" ", "")
    lines = txt_input.split("\n")

    if lines[-1] == "":
        lines = lines[:-1]

    for line in lines:

        from_, to = line.split("->")
        graph[from_] = to.split(",")

    return graph
