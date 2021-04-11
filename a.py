import pydot
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'



graph = pydot.Dot(graph_type='digraph')
nodes = "project/ceo"
for layerCfg in nodes.layerCfgs:
    node = pydot.Node(layerCfg.name)
    graph.add_node(node)
    nodes[layerCfg.name] = node
    for inp in layerCfg._inputs:
        if isinstance(inp,int):
            node = pydot.Node("input[{}]".format(inp))
            graph.add_node(node)
            nodes[str(inp)] = node
                    

    for layerCfg in nodes.layerCfgs:            
        for inp in layerCfg._inputs:
            if isinstance(inp,int):
                inp = str(inp)
            edge = pydot.Edge(nodes[inp],nodes[layerCfg.name])
            graph.add_edge(edge)

graph.write_png('examp.png')
