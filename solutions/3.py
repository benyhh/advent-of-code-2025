


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



def find_next_largest(numbers: str, start_index: list[int], next_index: int, index_sequence: list[int], iteration: int) -> int:
    """
    Recursively looks for the largest number in the sequence after the index of the previous largest number in the sequence.
    After 12 interations, return the sequence of indices.
    """
    
    possible_numbers = numbers[next_index: len(numbers) - (12 - iteration) + 1]
    largest_possible_number = sorted(possible_numbers)[-1]
    next_index = numbers.index(largest_possible_number, next_index)
    index_sequence.append(next_index)


    if iteration >= 11:
        return index_sequence
        
    return find_next_largest(numbers, start_index, next_index+1, index_sequence, iteration+1)
    

with open('3.txt', 'r') as f:
    lines = f.readlines()

total_joltage: int = 0
for line in lines:
    line = line.strip()
    
    numbers = line.split()[0]
    numbers_sorted = sorted(numbers[:-12])
    n_largest = numbers_sorted[-1]
    start_index = numbers.index(n_largest)
    
    max_index_sequence = find_next_largest(numbers, start_index, next_index=start_index+1, index_sequence=[start_index], iteration=1)
    max_joltage = int("".join(str(numbers[i]) for i in max_index_sequence))
    
    total_joltage += max_joltage
    
print("Part 2:", total_joltage)
