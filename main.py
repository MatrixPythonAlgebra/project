import numpy as np
from PIL import Image, ImageDraw
import part2

# 3x3 matrix with random values
random3 = np.random.random((3,3))

# 3x3 identity matrix
eye3 = np.eye(3)

# matrix [1, 2 ,3,
#         4, 5, 6,
#         7, 8, 9 ]

matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8 ,9]])

dp = np.dot(matrix,eye3)


# dot product function
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

# vector * matrix function
def vectorXmatrix (v, m):
  if len(v) != m.shape[0]:
    return "mismatch"
  
  result = np.zeros(m.shape[1])

  for i in range(m.shape[1]):
    for j in range(len(v)):
      result[i] += v[j] * m[j][i]

  return result

# check vector * matrix function
vector = np.array([1, 2, 3])
vectCheck = vectorXmatrix(vector, eye3)

# check dot product function
dotCheck = dotProduct(matrix, eye3)

ogImage = Image.open('star.png')
ogImage.show()
print(dotCheck)
#test part 2 rotations
point= [2,4]
print(part2.CounterClockRotate(point,np.pi/2))
print(part2.ClockRotate(point,np.pi/2))
#test part2 axis rotations
print(f'{part2.ReflectX(point)}  {part2.ReflectY(point)}')
print(f'{part2.ReflectYX(point)}  {part2.ReflectYMX(point, 3)}')
#test part 2 shearing and expansion/contraction
print(f'{part2.Xshear(point,2)}  {part2.YShear(point, 3)}  
      {part2.XYShear(point, 2)}')
print(f'{part2.XMult(point,2)}  {part2.YMult(point, 3)}  
      {part2.XYMult(point, 2)}')

imageMatrix = np.array(ogImage)

rotatedImageMatrix = np.rot90(imageMatrix, k=2)
rotatedImage = Image.fromarray(rotatedImageMatrix)
rotatedImage.show()