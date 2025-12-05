import numpy as np
import networkx as nx


ranges = []

def part1():
    fresh_count = 0
    with open("5.txt", "r") as f:
        lines = f.readlines()    

        construct_ranges = True
        for line in lines:
            if line == "\n":
                construct_ranges=False
                continue
            
            
            if construct_ranges:
                lower, upper = line.split("-")
                lower, upper = int(lower), int(upper)
                
                if len(ranges) == 0:
                    ranges.append((lower, upper))
                    continue

                merged_range = False
                for i, (r_lower,r_upper) in enumerate(ranges):
                    
                    if (r_lower <= lower <= r_upper) or (r_lower <= upper <= r_upper):
                        ranges[i] = (min(lower,r_lower), max(upper,r_upper))
                        merged_range=True
                        break
                    
                if not merged_range:
                    ranges.append((lower,upper))
                    
                    
            else:
                id_ingredient = int(line.strip())
                
                is_fresh = False
                for r_lower,r_upper in ranges:
                    if r_lower <= id_ingredient <= r_upper:
                        is_fresh = True
                        break
                    
                                    
                fresh_count += is_fresh
            

    print("Part 1:", fresh_count)
        
        


def part2():

    with open("5.txt", "r") as f:
        lines = f.readlines()    

        lower_bounds = []
        upper_bounds = []
        for line in lines:
            if line == "\n":
                break
    
            lower, upper = line.split("-")
            lower_bounds.append(int(lower))
            upper_bounds.append(int(upper))
            

    lower_bounds = np.array(lower_bounds)
    upper_bounds = np.array(upper_bounds)
    
    
    can_merge = np.logical_and(lower_bounds <= lower_bounds[:,np.newaxis],  lower_bounds[:, np.newaxis] <= upper_bounds)
    
    i_merge_lower, i_merge_upper = np.where(can_merge)
    
    G = nx.Graph()
    G.add_edges_from(zip(i_merge_lower, i_merge_upper))
    

    merged_lower_bounds = []
    merged_upper_bounds = []
    
    for comp in nx.connected_components(G):
        comp = list(comp)
        F = lower_bounds[comp].min()
        L = upper_bounds[comp].max()
        merged_lower_bounds.append(F)
        merged_upper_bounds.append(L)

    merged_lower_bounds = np.array(merged_lower_bounds)
    merged_upper_bounds = np.array(merged_upper_bounds)
    
    n_fresh_ids = np.sum(merged_upper_bounds-merged_lower_bounds+1)

    print("Part 2:", n_fresh_ids)
    
    
part1()
part2()

