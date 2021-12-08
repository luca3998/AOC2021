with open('input.txt') as f:
    numbers = [int(num) for num in f.readline().split(",")]
    boards = [int(word) for line in f for word in line.split()]

called_numbers = {numbers[0]}

class Board():
    def __init__(self, board, marked):
        self.board = board
        self.marked = marked


def checkRows(board,set):
    count_called = 0
    for i in range(25):
        if i % 5 == 0: count_called = 0
        if board[i] in set: count_called += 1
        if count_called == 5: return True

    return False

def checkColumns(board,set):
    count_called = 0
    for i in range(5):
        for j in range(0,25,5):
            if board[i+j] in set: count_called += 1
            if count_called == 5: 
                return True
        count_called = 0
    return False

def main(nums, set):
    for num in nums:
        set.add(num)
        for x in range(0,len(boards),25):
            currentboard = [boards[z] for z in range(x,x+25)]
           
            if(checkRows(currentboard,set) or checkColumns(currentboard,set)):
                unmarked_sum = sum([c for c in currentboard if c not in set])
                result = num * unmarked_sum
                return result
            
print(main(numbers, called_numbers))

def finalBoard():
    
    for board in listofboards:
        if board.marked == False:
            finalboard = Board(board.board,False)
            print(finalboard.board)
    for num in numbers:
        called_numbers_2.add(num)
        if(checkColumns(finalboard.board, called_numbers_2) or checkRows(finalboard.board, called_numbers_2)):
            unmarked_sum = sum([int(c) for c in finalboard.board if c not in called_numbers_2])
            result = num * unmarked_sum
            return result

listofboards = []

# Initialize the list of boards
for x in range(0,len(boards),25):
    currentboard = [boards[z] for z in range(x,x+25)]
    listofboards.append(Board(currentboard,False))

def countMarked():
    counter = 0
    for x in listofboards:
        if x.marked == True: counter += 1
    return counter

def main2(nums, set):
    for num in nums:
        set.add(num)
        for b in listofboards:
            if((b.marked == False) and (checkRows(b.board ,set) or checkColumns(b.board,set) )):
                b.marked = True
            if countMarked() == 99: 
                result = finalBoard()
                return result

called_numbers_2 = {numbers[0]}
print(main2(numbers,called_numbers_2))

# 11382 is het niet 

# if checkrows is okay, remove board from list. 
# misschien als while loop en dan totdat de lengte 1 is, en dan daarop verder tot alles gemarkt is .
