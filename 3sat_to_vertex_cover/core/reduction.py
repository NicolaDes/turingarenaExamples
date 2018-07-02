import matplotlib.pyplot as plt
import networkx as nx

def verify(cnf, vc):
    
   print("verify")

def getKey(dictionary, search):
    for key, val in dictionary.items():
        if val ==search:
            return key
    return 0

def reduce(formula, max):

    G = nx.Graph()
    
    mapping = dict()
    nodes = 1

    variables_original = set()
    for c in formula:
        for x in c:
            mapping[nodes]=x
            G.add_node(nodes,weigth=x)
            nodes=nodes+1
            mapping[nodes]=-x
            G.add_node(nodes,weigth=-x)
            G.add_edge(nodes,nodes-1)
            nodes=nodes+1
        # for x in c:
        #     mapping[nodes]=x
        #     G.add_node(nodes,weigth=x)
        #     nodes=nodes+1
        #     G.add_node(getKey(mapping,x),weigth=x)
    
    print(G.edges())
    print(G.nodes().data())
    
    nx.draw_networkx(G)
    plt.savefig("simple_path.png") # save as png
    plt.show() # display

    print(getKey(mapping,3))
            
    #     gadget_c.append(c)

    # print(gadget_v,gadget_c)
    # for p in gadget_v:
    #     for n in p: 
    #         mapping[n]=nodes
    #         G.add_node(mapping[n],weigth=n)
    #         nodes=nodes+1
    # for c in gadget_c:
    #     for l in c:
    #         mapping[l]=nodes
    #         G.add_node(mapping[n],weigth=l)
    #         nodes=nodes+1
    
    

    # print(G.nodes().data())
    # print(mapping)

    return [1]