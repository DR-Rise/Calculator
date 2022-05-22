import random

rows = 13
cols = 13
k = 8

#initializing the matrix with 0 values
myCellMatrix =[[0 for i in range(rows)] for j in range(cols)]

# filling first and last row by 1 to form the wall
for i in range (rows):
    for j in range(cols):
        if i == 0 or i == (cols-1):
            myCellMatrix[i][j]=1

# filling first and last colmn  by 1 to form the wall
for i in range (rows):
    for j in range(cols):
        if j == 0 or j == (cols-1):
            myCellMatrix[i][j]=1

# print the final matrix
for rows in myCellMatrix:
    print(rows)
print()

# replace k number of elements with number 5 randomly
while k>0:
    randRow=random.randint(1,10)
    randCol=random.randint(1,10)
    if myCellMatrix[randRow][randCol] == 0:
       myCellMatrix[randRow][randCol] = 8
       k-=1
# print the final matrix
for rows in myCellMatrix:
    print(rows)
print()