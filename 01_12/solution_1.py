with open('input.txt') as f:
    numbers = [int(num) for num in f]
    print(numbers)

count = 0;

# Part 1
for num,current in enumerate(numbers):
    if num == 0: pass
    if current > numbers[num-1]: count += 1

print(count)

count_3 = 0;
# Part 2
for num,current in enumerate(numbers):
    if num == (len(numbers) -  3): break
    one = current + numbers[num+1] + numbers[num+2]
    two = numbers[num+1] + numbers[num+2] + numbers[num+3]
    if two > one: count_3 += 1

print(count_3)
