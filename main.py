import numpy as np

# 3x3 matrix with random values
random3 = np.random.random((3,3))
print(random3)

# 3x3 identity matrix
eye3 = np.eye(3)
print(eye3)

# matrix [1, 2 ,3,
#         4, 5, 6,
#         7, 8, 9 ]

matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8 ,9]])
print(matrix)
print(matrix[0,0])
print(matrix[2, 2])

for row in matrix:
 for item in row:
  print(item)

dp = np.dot(matrix,eye3)
print(dp)

result = np.zeros((3,3))

for i in range(3):
 for j in range(3):
  for k in range(3):
   result[i][j] += matrix[i][k] * eye3[k, j]

print(result)

def dotProduct(A, B):
 if A.shape[1] != B.shape[0]:
    return "mismatched indecies"
 
 A_dim = A.shape
 B_dim = B.shape

 res_dim = (A_dim[0], B_dim[1])
 res = np.zeros(res_dim)

 for i in range(3):
   for j in range(3):
    for k in range(3):
      res[i][j] += A[i][k] * B[k, j]

 return res

check = dotProduct(matrix, eye3)

print(check)
