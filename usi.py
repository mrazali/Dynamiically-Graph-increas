import pydot
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'

path="project"

def print_option():
    print(" ")
    print("0) finish node")
    print("1) Insert node")
    print("2) Delete node")
    print("3) Move In")
    print("4) Move out ")
    print("5) make Graph")
    print(" ")

def insert_link(dirName):
    if not os.path.exists(path+"/"+dirName):
        os.mkdir(path+"/"+dirName)
        print("Directory ", path , "Created !")
    else:
        print ("Directory ", path , "Already Exits !")

def delete_link(dirName):
    if os.path.exists(path+"/"+dirName):
        os.rmdir(path+"/"+dirName)
        print("Directory ", path , "Deleted !")
    else:
        print ("Directory ", path , "Not Exits !")

def move_in(dirName):
    if os.path.exists(path+"/"+dirName):
        return path+"/"+dirName
    else:
        print ("That name is not exists ")
        return path

def move_out(p):
        return "project"


def built_graph():
    rootDir = "project/ceo"

    a=["skyblue","yellow"]
    x=0
    G = pydot.Dot(graph_type="digraph")

    node = pydot.Node(rootDir.split('/')[-1], style="filled", fillcolor="green")
    G.add_node(node)

    for root , dirs ,files in os.walk(rootDir):
        
        root=root.split('\\''')[-1]
        for subdir in dirs:
            node = pydot.Node(subdir, style="filled", fillcolor=a[x])
            G.add_node(node)
            edge = pydot.Edge(root.split('/')[-1], subdir)
            G.add_edge(edge)
        x=x+1
        if(x>1):
            x=0
        
    G.write_png('example1_graph.png')



n=1
while(n):
    print_option()
    dirName = input("Enter selection : ")
    if (dirName=="1"):
        dirName = input("ADD Name : ")
        insert_link(dirName)
    elif (dirName=="2"):
        dirName = input("Delete Name: ")
        delete_link(dirName)
    elif (dirName=="3"):
        dirName = input("MOve-in Name: ")
        path=move_in(dirName)
    elif (dirName=="4"):
        path=move_out(path)
        print(path)
    elif (dirName=="5"):
        built_graph()
    elif (dirName=="0"):
        n=0
    else:
        print("you Enter out of seletion , Try Again")
