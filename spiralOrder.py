def spiralorder(matrix):
    ret=[]
    while matrix:

        ret+=(matrix.pop(0))
        if matrix:
            for row in matrix:
                ret.append(row.pop())

        if matrix:
            ret+=(matrix.pop()[::-1])
        
        if matrix:

            for row in matrix[::-1]:
                ret.append(row.pop(0))
    print(ret)
rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))
matrix=[]
for i in range(rows):
    row=list(map(int,input().split()))
    matrix.append(row)
    
print("spiral Order is:")
spiralorder(matrix)