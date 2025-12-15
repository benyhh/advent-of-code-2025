import numpy as np
import pandas as pd


df = pd.read_csv("9.csv", header=None, names = ["x","y"])
arr = df.to_numpy()

rows, cols = np.triu_indices(len(arr), k=1)
d = np.prod(np.abs(arr[cols] - arr[rows])+1,axis=1)

argmax = np.argmax(d)

print("Part 1:", d[argmax])

grid = np.full((df.max()+1), False, dtype=bool)

arr_pad = np.append(arr,arr[0,np.newaxis],axis=0)

pos = arr[0]

for dx,dy in np.diff(arr_pad,axis=0):
    
    if dx == 0:
        y1,y2 = sorted([pos[1], pos[1]+dy])
        grid[pos[0],y1:y2+1] = True
    else:    
        x1,x2 = sorted([pos[0], pos[0]+dx])
        grid[x1:x2,pos[1]]=True
    
    pos += np.array([dx,dy])


i_largest_desc = np.argsort(d)[::-1]
for i in i_largest_desc:
    x1,y1 = df.iloc[rows[i]]
    x2,y2 = df.iloc[cols[i]]

    x1,x2 = sorted([x1,x2])
    y1,y2 = sorted([y1,y2])
    
    _df = df.loc[df["x"].between(x1,x2, inclusive="neither") & df["y"].between(y1,y2, inclusive="neither")]
    if not _df.empty:
        continue
    
    if not np.any(grid[x1+1:x2,y1+1:y2]):
        break


print("Part 2:", d[i])