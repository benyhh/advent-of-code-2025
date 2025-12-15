import numpy as np


paper_roll = "@"

with open("4.txt") as f:
    lines = f.read().strip().split("\n")
    
data = np.array([list(line) for line in lines])

def part1():
    binary = np.where(data == paper_roll,1,0)
    binary_with_padding = np.pad(binary, ((1,1),(1,1)), 'constant', constant_values=0)

    sum_surrounding = binary_with_padding[:-2,:-2] + binary_with_padding[2:,2:] + binary_with_padding[2:,:-2] + binary_with_padding[:-2,2:] + binary_with_padding[1:-1,:-2] + binary_with_padding[1:-1,2:] + binary_with_padding[:-2,1:-1] + binary_with_padding[2:,1:-1]
    
    print("Part 1:", np.logical_and(binary, sum_surrounding < 4).sum())

part1()



def part2():

    binary = np.where(data == paper_roll,1,0)
    rolls_removed = 0
    while True:
        
        binary_with_padding = np.pad(binary, ((1,1),(1,1)), 'constant', constant_values=0)
        
        sum_surrounding = binary_with_padding[:-2,:-2] + binary_with_padding[2:,2:] + binary_with_padding[2:,:-2] + binary_with_padding[:-2,2:] + binary_with_padding[1:-1,:-2] + binary_with_padding[1:-1,2:] + binary_with_padding[:-2,1:-1] + binary_with_padding[2:,1:-1]
        
        to_remove = np.where(np.logical_and(binary, sum_surrounding < 4), 1, 0)
        if not to_remove.any():
            break
        
        rolls_removed += to_remove.sum()
        binary -= to_remove
        
        
    print("Part 2:", rolls_removed)
        
    
    
    
part2()