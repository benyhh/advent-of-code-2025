
import numpy as np


rows = [] # For printing christmas tree
total_splits = 0
n_timelines: int = 1

with open("7.txt", "r") as f:
    lines = f.readlines()
    
    first_line = np.array(list(lines.pop(0).strip()))
    rows.append(first_line) # For printing christmas tree
    n_beams = np.where(first_line == "S", 1, 0)
    
    for line in lines:
        arr = np.array(list(line.strip()))
        
        i_splitters = arr == "^"
        if not np.any(i_splitters):
            rows.append(np.where(n_beams != 0, "|", ".")) # For printing christmas tree
            continue

        current_beams = np.where(i_splitters, 0, n_beams)
        i_beams_split = np.logical_and(n_beams != 0, i_splitters)
        n_beams_split = np.where(i_beams_split, n_beams, 0)
        
        total_splits += np.sum(i_beams_split)
        if not np.any(i_beams_split):
            continue


        n_timelines += np.sum(np.where(i_beams_split,n_beams, 0))
        
        left_shift = np.concat([n_beams_split[1:], [0]])
        right_shift = np.concat([[0], n_beams_split[:-1]])

        n_split_beams = left_shift + right_shift
        n_beams = n_split_beams + current_beams


        # For printing christmas tree
        new_row = np.where(n_beams != 0, "|", ".")
        new_row = np.where(i_splitters, "^", new_row)
        rows.append(new_row)
        
        
print("Part 1:", total_splits)
print("Part 2:", n_timelines)

# Uncomment to print christmas tree
# for row in rows:
#     print("".join(row))