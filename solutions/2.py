

def is_repetitive(x: str):
    """
    For a given integer string, detect depetitive digit patterns.
    
    We can do that by splitting
    """
    assert len(x) % 2 == 0, "Only even length strings can be repetitive"
    x1 = x[:len(x)//2]
    x2 = x[len(x)//2:]
    
    return x1 == x2
    


sum_repetitions = 0
with open('2.txt') as f:
    line = f.read()
    
    ranges = line.split(',')
    
    for _range in ranges:
        start, end = _range.split('-')
        
        # Odd length strings cannot have full repetitions
        if len(start) == len(end) and len(start) % 2 != 0:
            continue
        
        possible_repetitions = [i for i in range(int(start), int(end)+1) if len(str(i)) % 2 == 0]
        repetitions = [i for i in possible_repetitions if is_repetitive(str(i))]
        
        sum_repetitions += sum(repetitions)
        
        
print(f'Part 1: {sum_repetitions}')



def has_repetitive_pattern(x: str):
    """
    For a given integer string, detect depetitive digit patterns of any length.
    
    We can do that by checking all possible splits of the string.
    """
    for i in range (1, len(x)):
        if len(x) % i != 0:
            continue
        
        segments = [x[j:j+i] for j in range(0, len(x), i)]
        if len(set(segments)) == 1:
            return True
    
    return False


sum_repetitions = 0
with open('2.txt') as f:
    line = f.read()
    
    ranges = line.split(',')
    
    for _range in ranges:
        start, end = _range.split('-')
        
        repetitions = [i for i in range(int(start), int(end)+1) if has_repetitive_pattern(str(i))]
        
        sum_repetitions += sum(repetitions)
        
        
print(f'Part 2: {sum_repetitions}')

