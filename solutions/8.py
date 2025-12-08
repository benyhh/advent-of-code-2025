import pandas as pd
import numpy as np
import networkx as nx


df = pd.read_csv("8.csv", header=None, names = ["x","y","z"])
arr = df.to_numpy()

rows, cols = np.triu_indices(len(arr), k=1)

d = np.linalg.norm(arr[rows] - arr[cols], axis=1)
G = nx.Graph()

for i in range(20):
    G.add_node(i)

for i in range(1000):

    argmin = np.argmin(d)
    d[argmin] = np.inf
    
    node1 = int(rows[argmin])
    node2 = int(cols[argmin])

    G.add_edge(node1,node2)


print("Part 1:", np.prod(sorted([len(comp) for comp in nx.connected_components(G)])[-3:]))


while nx.number_connected_components(G) != 1:
    argmin = np.argmin(d)
    d[argmin] = np.inf
    
    node1 = int(rows[argmin])
    node2 = int(cols[argmin])
    G.add_edge(node1,node2)
    

print("Part 2:", arr[node1,0] * arr[node2,0])