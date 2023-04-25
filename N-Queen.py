boardQueen = [[' ' for _ in range(5)] for _ in range(5)]
boardAttacked = [[' ' for _ in range(5)] for _ in range(5)]

def attackRange(a,b,side):
    for x in range(side):
        for y in range(side):
            if x==a or y==b or y==x-a+b or y==a-x+b:
                boardAttacked[y][x] = 'x'

attackRange(2,2,5)
print(boardAttacked)