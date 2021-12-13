from backend.tree.tree import Tree


def get_content(path: str) -> str:
    """
    Function for reading from file
    """
    with open(path, "r") as f:
        content = f.read()

    return content


def get_tree(inpt: str) -> Tree:
    
    #-----------parse input----------------#
    lines = inpt.split("\n")
    relations = {}

    if lines[-1] == "":
        lines.pop()

    for line in lines:
        
        line = line.replace(" ", "")
        parent, children_str = line.split("->")
        children = children_str.split(",")
        relations[parent] = children
    #---------------------------------------#

    #----Get all members---------#
    members = set(relations)
    nodes = {}

    for children in relations.values():
        members = members | set(children)

    #----------------------------#

    #-------Creating relations---------------#
    for parent, children in relations.items():

        if parent not in nodes:

            nodes[parent] = Tree(parent)

        p = nodes[parent]

        for child in children:

            if child not in nodes:
                nodes[child] = Tree(child)

            c = nodes[child]

            p.children.append(c)
            c.parent = p

            members.remove(child)
    #------------------------------------------#

    # Not definite root (More members without parent)
    if len(members) > 1:
        return 1

    return nodes[members.pop()]
