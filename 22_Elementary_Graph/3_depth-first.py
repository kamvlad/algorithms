from pygraphviz import *

time = 0

def DFS(graph):
    global time
    for nd in graph.iternodes():
        nd.attr['color'] = 'white'
        nd.attr['pi'] = None
    time = 0
    for nd in graph.iternodes():
        if nd.attr['color'] == 'white':
            DFS_VISIT(graph, nd)

def DFS_VISIT(graph, u):
    global time
    time = time + 1
    u.attr['d'] = time
    u.attr['color'] = 'gray'
    for v in graph.out_neighbors(u):
        if v.attr['color'] == 'white':
            v.attr['pi'] = u
            DFS_VISIT(graph, v)
    u.attr['color'] = 'black'
    time = time + 1
    u.attr['f'] = time

def main():
    G = AGraph("graph22_4.dot")
    DFS(G) 

    for v in G:
        v.attr['label'] = v.attr['d'] + '/' + v.attr['f']

    G.layout(prog='circo')
    G.draw("graph22_4.png")

if __name__ == '__main__':
    main()
