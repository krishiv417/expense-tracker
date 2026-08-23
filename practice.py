
# rows=int(input("Enter row:"))
# cols=int(input("Enter column:"))
# matrix=[]

# print("Enter matrix elements:")

# for i in range(rows):
#     row=[]
#     for j in range(cols):
#         row.append(int(input()))
#     matrix.append(row)

# transpose=[]

# for j in range(cols):
#     row=[]
#     for i in range(rows):
#         row.append(matrix[i][j])
#     transpose.append(row)

# print("Original matrix:")
# for row in matrix:
#     print(row)

# print("Transpose matrix:")
# for row in transpose:
#     print(row)


# def sum_of_square(M):
#     even=0
#     odd=0
#     for i in M:
#         if i%2==0:
#             even+=i**2
#         else:
#             odd+=i**2
#     l=[even,odd]
#     return l
# l=[1,2,3,5,7]
# print(sum_of_square(l))


n=5

for i in range(1,n+1):
    for j in range(1,i):
        if (i+j)%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()