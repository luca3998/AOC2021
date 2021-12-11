board = [[0 for x in range(1000)] for y in range(1000)]
lines = []

class Line():
    def __init__(self, x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

with open('input.txt') as f:
    coordinates = [x.split('->') for x in f]

start = [c[0].split(',') for c in coordinates]    
end =  [c[1].split(',') for c in coordinates] 

for i in range(len(start)):
    lines.append(Line(int(start[i][0].strip()),int(start[i][1].strip()),int(end[i][0].strip()),int(end[i][1].strip())))
    
for line in lines:
    if(line.x1 == line.x2):
        if(line.y1<=line.y2):
            for i in range(line.y1,line.y2 + 1):
                board[i][line.x2] += 1
        else:
            for i in range(line.y1,line.y2 - 1,-1):
                board[i][line.x2] += 1
    elif(line.y1 == line.y2):
        if(line.x1<=line.x2):
            for i in range(line.x1,line.x2 + 1):
                board[line.y2][i] += 1
        else:
            for i in range(line.x1,line.x2 - 1,-1):
                board[line.y2][i] += 1
    else: 
        diff = abs(line.x1-line.x2)
        diff2 = abs(line.y1-line.y2)        # Diagonale stap hier 
        if(line.x1 < line.x2): 
            if(line.y1<line.y2): # naar rechtsonder
                for i in range(0, diff + 1 ):
                    board[line.y1 + i][line.x1 + i] += 1
            else: # naar rechtsboven
                for i in range(0, diff + 1):
                    board[line.y1 - i][line.x1 + i] += 1
        else:
            if(line.y1<line.y2):
                for i in range(0, diff + 1): # naar linksonder
                    board[line.y1+i][line.x1-i] += 1
            else:
                for i in range(0, diff + 1): # naar linksboven
                    board[line.y1 - i][line.x1 - i] += 1

answer = 0
for x in range(1000):
    for y in range(1000):
        if board[y][x] >= 2: answer += 1

print(answer)
    