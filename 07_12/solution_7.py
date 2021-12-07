with open('input.txt') as f:
    values = [int(num) for num in f.readline().split(",")]
    min = min(values)
    max = max(values)
    
minimum = 20000000000

def calculateFuel(fuel):
    required = 0
    for v in values:
        required += additionHelper(abs(v - fuel))
    return required

def additionHelper(f):
    res  = 0;
    for x in range(f+1):
        res += x
    return res


for i in range(max+1):
    print("Round ", i, " of ", max)
    fuel_needed = calculateFuel(i)
    print(fuel_needed,minimum)
    if fuel_needed < minimum: 
        minimum = fuel_needed
        fuel_amount = i

print(minimum)