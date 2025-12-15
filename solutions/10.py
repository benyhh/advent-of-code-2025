import numpy as np
import networkx as nx
import sys
from scipy.optimize import milp, LinearConstraint
sys.setrecursionlimit(5000)


def explore_wiring(current_node: tuple[bool], G, buttons, light_diagram):
    
    while G.degree[current_node] != len(buttons):
        
        
        used_buttons = [data.get('button') for _,_,data in G.edges(current_node, data=True)]
        remaining_buttons = [_b for _b in buttons if not any([all(_b==ub) for ub in used_buttons])]
        button = remaining_buttons[0]

        
        new_node = tuple(np.logical_xor(np.array(current_node),button))
        G.add_edge(current_node, new_node, button=button)
        if new_node == tuple(light_diagram):
            return
        
        explore_wiring(new_node, G, buttons, light_diagram)
        
    return



def part1():
    shortes_paths = []
    with open("10.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            
            light_diagram, line = line.strip().split("]")
            wiring_schematics, joltage_requirement = line.split('{')
            
            joltage_requirement = eval('(' + joltage_requirement.replace('}', ')'))
            light_diagram = np.where(np.array(list(light_diagram.replace("[",""))) == '#', True,False)
            wiring_schematics = [eval(ws) for ws in wiring_schematics.strip().replace('(','[').replace(')',']').split(' ')]
            
            buttons = []
            for ws in wiring_schematics:
                button = np.array([False]*len(light_diagram))
                button[ws] = True
                buttons.append(button)
            
            G = nx.Graph()
            start_node = (False,)*len(light_diagram)
            G.add_node(start_node)
            explore_wiring(start_node, G, buttons, light_diagram)
            
            shortest_path_nodes = nx.shortest_path(G, source=start_node, target=tuple(light_diagram))
            shortes_paths.append(len(shortest_path_nodes) - 1)

        
    print('Part 1:',sum(shortes_paths))


def minimize_presses_with_milp(A,y):
    m,n = A.shape
    
    constraint = LinearConstraint(A, y, y)
    
    integrality = np.ones(n)
    
    c = np.ones(n)
    
    res = milp(c=c, constraints=constraint, integrality=integrality)
    return sum(res.x)
    
        
def part2():

    total_presses = []
    with open("10.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            
            light_diagram, line = line.strip().split("]")
            wiring_schematics, joltage_requirement = line.split('{')
            
            joltage_requirement = np.array(eval('(' + joltage_requirement.replace('}', ')')))
            
            light_diagram = np.where(np.array(list(light_diagram.replace("[",""))) == '#', 1,0)
            wiring_schematics = [eval(ws) for ws in wiring_schematics.strip().replace('(','[').replace(')',']').split(' ')]
        
            
            buttons = []
            for ws in wiring_schematics:
                button = np.full_like(light_diagram,0)
                button[ws] = 1
                buttons.append(button)
        
        
            buttons = np.array(buttons).T
            
            presses = minimize_presses_with_milp(buttons, joltage_requirement)
            total_presses.append(presses)
            
                
    print('Part 2:', int(sum(total_presses)))

part1()
part2()
