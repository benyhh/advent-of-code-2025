

def move(pos, direction, distance):
    alreadyCountedZero = (pos == 0) and (direction == 'L')
    if direction == 'L':
        pos -= distance
    else:
        pos += distance

    nCrossings = abs(pos // 100) - int(alreadyCountedZero)
    
    # When negative direction and landing exactly at -100*n, we need to count one extra crossing
    extraCount = pos < 0 and pos % 100 == 0

    # When landing at zero without crossing, we need to count.
    exactlyZero = pos == 0

    pos %= 100

    isZero = pos == 0

    assert nCrossings >= 0
    
    return pos, isZero, nCrossings + extraCount or exactlyZero


pos = 50
zeroCount = 0
crossedZeroCount = 0
with open('1.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    
    direction = line[0]
    distance = int(line[1:])

    pos, isZero, nCrossings = move(pos, direction, distance)

    zeroCount += isZero
    crossedZeroCount += nCrossings

print("Part 1: ", zeroCount)
print("Part 2: ", crossedZeroCount)

