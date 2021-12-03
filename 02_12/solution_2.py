with open('input.txt') as f:
    numbers = [word for line in f for word in line.split()]

# Part 1
def part_one():
    horizontal = 0
    depth = 0   
    aim = 0

    for i in range(len(numbers)):
        if i % 2 == 1: continue
        
        if numbers[i] == 'forward':
            horizontal += int(numbers[i+1])
        elif numbers[i] == 'up':
            depth -= int(numbers[i+1])
        elif numbers[i] == 'down':
            depth += int(numbers[i+1])

    print(horizontal, depth, horizontal * depth)

# part 2
def part_two():
    horizontal = 0
    depth = 0   
    aim = 0
    for i in range(len(numbers)):
        if i % 2 == 1: continue
        
        if numbers[i] == 'forward':
            horizontal += int(numbers[i+1])
            depth += int(numbers[i+1]) * aim
        elif numbers[i] == 'up':
            aim -= int(numbers[i+1])
        elif numbers[i] == 'down':
            aim += int(numbers[i+1])

    print(horizontal, depth, horizontal * depth)

part_two()