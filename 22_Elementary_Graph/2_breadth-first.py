from pygraphviz import *

def BFS(graph, node):
    for nd in graph.iternodes():
        nd.attr['color'] = 'white'
        nd.attr['d'] = 999
        nd.attr['pi'] = None
    node.attr['color'] = 'gray'
    node.attr['d'] = 0
    node.attr['pi'] = None
    Q = [ node ]
    while Q:
        u = Q[0]
        Q = Q[1:]
        for v in graph.neighbors_iter(u):
            if v.attr['color'] == 'white':
                v.attr['color'] = 'black'
                v.attr['d'] = int(u.attr['d']) + 1
                v.attr['pi'] = u
                Q.append(v)
        u.attr['color'] = 'black'

    for nd in graph.iternodes():
        nd.attr['label'] = 'd = ' + nd.attr['d']
        nd.attr['shape'] = 'polygon'

def main():
    G = AGraph("graph22_3.dot")
    print G
    BFS(G, G.get_node(3)) 
    

    G.layout(prog='circo')
    G.draw("graph22_3.png")

if __name__ == '__main__':
    main()
