import pydot
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'

rootDir = "project/ceo"

a=["skyblue","yellow"]
x=0
G = pydot.Dot(graph_type="digraph")

node = pydot.Node(rootDir.split('/')[-1], style="filled", fillcolor="green")
G.add_node(node)

for root , dirs ,files in os.walk(rootDir):
    print(dirs)
    
    root=root.split('\\''')[-1]
    for subdir in dirs:
        node = pydot.Node(subdir, style="filled", fillcolor=a[x])
        G.add_node(node)
        edge = pydot.Edge(root.split('/')[-1], subdir)
        G.add_edge(edge)
    print (a[x])
    x=x+1
    if(x>1):
        x=0
    print (root)
    
G.write_png('example1_graph.png')





