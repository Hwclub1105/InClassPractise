'''
l1 = []
l2 = []
'''

def preAndSuff(s1,s2):
    counter = 0
    for i in s2:
        for j in s1:
          try:
            if (i == j[0:len(i)]) or (i == j[len(j)-len(i):len(j)]):
                counter += 1
          except IndexError:
            print('no')
            pass
    return counter


list1 = []
list2 = []

len1 = int(input('Enter the number of words in s1: '))
for i in range(len1):
    list1.append(input('Enter element',i+1))

len2 = int(input('Enter the number of words in s2: '))
for i in range(len2):
    list2.append(input('Enter element',i+1))

print(preAndSuff(list1,list2))
