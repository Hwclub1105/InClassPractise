ranges = [[1,4], [6,10], [18,21]]
milestone = {}
queries = [3,5,11,28]
preSpace = 0
ans = []

for i in range(len(ranges)-1):
    space = ranges[i+1][0] - ranges[i][1]
    if space-1 > 0:
        milestone[ranges[i][1]] = space-1 + preSpace
        preSpace = space-1

for i in [*milestone.keys()][::-1]:
    ans.append()
        