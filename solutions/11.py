import networkx as nx

with open('11.txt', 'r') as f:
    
    lines = f.readlines()
    
    G = nx.DiGraph()
    for line in lines:
        
        from_node, to_nodes = line.strip().split(': ')
        
        to_nodes = to_nodes.split(' ')
        
        G.add_edges_from([(from_node, to_node) for to_node in to_nodes])


def calc_sum_paths(source, target):
    print('Source:', source, ', target:', target)
    paths = nx.all_simple_paths(G, source, target)
    return sum(1 for path in paths)



print('Part 1:', calc_sum_paths('you', 'out'))


def count_paths(source, target):
    topo = list(nx.topological_sort(G))
    dp = {node: 0 for node in G.nodes()}
    dp[source] = 1
    for u in topo:
        for v in G.successors(u):
            dp[v] += dp[u]

    return dp[target]

svr_to_dac = count_paths('svr', 'dac')
svr_to_fft = count_paths('svr', 'fft')
dac_to_fft = count_paths('dac', 'fft')
fft_to_dac = count_paths('fft', 'dac')
dac_to_out = count_paths('dac', 'out')
fft_to_out = count_paths('fft', 'out')

total_paths = svr_to_dac * dac_to_fft * fft_to_out + svr_to_fft * fft_to_dac * dac_to_out

print('Part 2:', total_paths)

