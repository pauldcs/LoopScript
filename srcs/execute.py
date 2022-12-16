def traverse(node, indent=0):
    print("    " * indent + "└── " + str(node))
    for child in node.children:
        traverse(child, indent=indent+1)