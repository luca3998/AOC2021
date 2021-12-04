with open('input.txt') as f:
    numbers = [list(line) for line in f]

# Part 1
maxLength = len(numbers[-1])
gamma = ""

for i in range(maxLength):  # Loop over elke kolom
    ones = 0
    zeroes = 0
    for j in range(len(numbers)):  # van elke rij
        if (numbers[j][i] == "1"):
            ones += 1
        else:
            zeroes += 1
    if ones > zeroes:
        gamma += str("1")
    else:
        gamma += str("0")

epsilon = ''.join('1' if x == '0' else '0' for x in gamma)

epsilon_int = int(epsilon, 2)
gamma_int = int(gamma, 2)

print("Answer for part 1 is ", epsilon_int * gamma_int)

# Part 2
oxygen = numbers
while(len(oxygen) > 1):
    for i in range(maxLength):  # Loop over elke kolom
        ones = 0
        zeroes = 0
        for j in oxygen:  # van elke rij
            if (j[i] == "1"):
                ones += 1
            else:
                zeroes += 1
        if(ones>=zeroes): mostCommon = "1" 
        else: mostCommon = "0"
        oxygen = [x for x in oxygen if x[i] == mostCommon]

scrubber = numbers       
while(len(scrubber) > 1):
    for i in range(maxLength):  # Loop over elke kolom
        ones = 0
        zeroes = 0
        for j in scrubber:  # van elke rij
            if (j[i] == "1"):
                ones += 1
            else:
                zeroes += 1
        if(zeroes<=ones): leastCommon = "0"
        else: leastCommon = "1"
        scrubber = [x for x in scrubber if x[i] == leastCommon]
        if(len(scrubber) == 1):
            break

oxygen_int = "".join(oxygen[0])   
scrubber_int = "".join(scrubber[0])    
print("Final answer: ", int(oxygen_int,2) * int(scrubber_int,2))