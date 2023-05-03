s = 'adbbdsef'
queries = [['1','4','x'],['2','3','7','1']]
n = 8 # length of string
q = 2 # num of queries

def q1(index, char):
    global s
    s = s[:index] + char + s[index+1:]
    
def q2(start, finish, n):
    global s
    return sorted([*s[start:finish+1]])[::-1][n-1]

x = 0
while True:
    if queries[x][0] == '1':
        q1(int(queries[x][1]),queries[x][2])
    else:
        q2(int(queries[x][1]),int(queries[x][2]),int(queries[x][3]))
    x+=1
    
    if x == q:
        break
    


print(q2(0,7,2))