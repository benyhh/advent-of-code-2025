


with open('3.txt', 'r') as f:
    lines = f.readlines()

total_joltage: int = 0
for line in lines:
    line = line.strip()
    numbers = line.split()[0]
    numbers_sorted = sorted(numbers)

    sorted_numbers_except_last = sorted(numbers[:-1])
    n_largest = sorted_numbers_except_last[-1]
    i_largest = numbers.index(sorted_numbers_except_last[-1])
    
    # Largest number after this index
    sorted_numbers_after_largest = sorted(numbers[i_largest+1:])
    i_next_largest = numbers.index(sorted_numbers_after_largest[-1], i_largest+1)
    n_next_largest = sorted_numbers_after_largest[-1]
        
    total_joltage += int(n_largest + n_next_largest)


print("Part 1:", total_joltage)



def find_next_largest(numbers: str, start_indexes: list[int], offsets: list[int], index_sequence: list[list[int]], iteration: int) -> int:
    """
    Recursively looks for the next largest numbers for all the start indexes. 
    The next largest number can be at any offset from the previous index as long as 
    it is in the range numbers[start_index + offset: len(numbers) - (12 - iteration)]. Offset starting at 1
    Calls itself until start_indexes only has one element or the offset is >= 12
    and then it returns start index remaining.
    
    Keeps track of the most promising index sequences and start indexes.
    Recursively calls itself until only one start index remains or 12 iterations have been made.
    """
    
    next_numbers = []
    new_offsets = []
    for i,(start_index, offset) in enumerate(zip(start_indexes, offsets)):
        possible_numbers = numbers[start_index + offset: len(numbers) - (12 - iteration) + 1]
        largest_possible_number = sorted(possible_numbers)[-1]
        next_index = numbers.index(largest_possible_number, start_index + offset)
        next_numbers.append(largest_possible_number)
        index_sequence[i].append(next_index)
        new_offsets.append(next_index - start_index + 1)

    max_next_number = max(next_numbers)
    start_indexes = [i for i,val in zip(start_indexes, next_numbers) if val == max_next_number]
    new_offsets = [offset for offset, val in zip(new_offsets, next_numbers) if val == max_next_number]
    index_sequence = [seq for seq, val in zip(index_sequence, next_numbers) if val == max_next_number]
    if iteration >= 11:
        return index_sequence[0]
        
    return find_next_largest(numbers, start_indexes, new_offsets, index_sequence, iteration+1)
    

with open('3.txt', 'r') as f:
    lines = f.readlines()

total_joltage: int = 0
for line in lines:

    line = line.strip()
    numbers = line.split()[0]
    numbers_sorted = sorted(numbers[:-12])
    n_largest = numbers_sorted[-1]
    start_indexes = [i for i, val in enumerate(numbers[:-12]) if val == n_largest]

    max_index_sequence = find_next_largest(numbers, start_indexes, offsets=[1]*len(start_indexes), index_sequence=[[start_index] for start_index in start_indexes], iteration=1)
    max_joltage = int("".join(str(numbers[i]) for i in max_index_sequence))
    
    total_joltage += max_joltage
    
print("Part 2:", total_joltage)
