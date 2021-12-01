with open('input.txt') as f:
    numbers = [int(num) for num in f]
    print(numbers)

count = 0;

for num,current in enumerate(numbers):
    if num == 0: pass
    if current > numbers[num-1]: count += 1

print(count)
