import math

with open("12.txt", 'r') as f:
    
    lines = f.readlines()
    
    shapes = {}
    shape_sizes = {}
    
    grids = []
    current_shape = 0
    parse_shapes = True
    for line in lines:

        if 'x' in line:
            parse_shapes = False

        line = line.strip()
        if line == '':
            continue
        
        if parse_shapes:
            if line[1] == ':':
                current_shape = int(line[0])
                shapes[current_shape] = []
                shape_sizes[current_shape] = 0
                
            else:
                shapes[current_shape].append(list(line))
                shape_sizes[current_shape] += len(line.replace('.',''))

        else:
            split = line.split(': ')
            dim = tuple(int(d) for d in split[0].split('x'))
            counts = eval((split[1].replace(' ', ',')))
            
            grids.append((dim,counts))

        
def total_shape_area_optimistic(counts: tuple[int], shape_sizes: dict[int,int]):
    return sum((c * shape_sizes[i] for i,c in enumerate(counts)))
    
def total_shape_area_pessimistic(counts: tuple[int]):
    return sum(counts) * 9


guarenteed_fail = 0
guarenteed_success = 0

for grid in grids:
    
    dim, counts = grid

    grid_area = math.prod(dim)
    shape_area_optimistic = total_shape_area_optimistic(counts, shape_sizes)
    if grid_area < shape_area_optimistic:
        guarenteed_fail += 1
        
    shape_area_pessimistic = total_shape_area_pessimistic(counts)
    grid_area_floored = (dim[0] - dim[0]%3) * (dim[1] - dim[1]%3)
    if grid_area_floored >= shape_area_pessimistic:
        guarenteed_success += 1
    


# Luckily, assuming pessimistic and optimistic placement covered every case in the puzzle input. 
print('Part 1:', guarenteed_success)