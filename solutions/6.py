import numpy as np
import pandas as pd


def part1():
    df = pd.read_csv("6.txt", sep="\s+", header=None)

    operation = df.iloc[-1]
    df = df.iloc[:-1].astype(int)

    prod = df.loc[: , operation == "*"].prod(axis=0)
    cumsum = df.loc[:, operation == "+"].sum(axis=0)

    total = prod.sum() + cumsum.sum()
    print("Part 1:", total)



def part2():
    start_indexes = []
    with open("6.txt", "r") as f:
        lines = f.readlines()

        operations = lines.pop()
        
        for i, op in enumerate(operations):
            if op != " ":
                start_indexes.append(i)
                
        
        rows = []
        for i, line in enumerate(lines):
            
            line_split = [line[i:j-1] for i,j in zip(start_indexes[:-1], start_indexes[1:])] + [line[start_indexes[-1]:].strip()]
            
            rows.append(line_split)
            
        arr = np.array(rows)
                
        
        total = 0
        operations = list(operations.replace(" ",""))
        for j,op in zip(range(arr.shape[1]), operations):
            
            df = pd.Series(arr[:,j])
            df = df.str.split("",expand=True)
            df = df.iloc[:,1:-1]
            vals = df.sum(axis=0).astype(int)
            if op == "*":
                total += vals.prod()
                
            else:
                total += vals.sum()
                

        print("Part 2:", total)
            
        

part1()
part2()