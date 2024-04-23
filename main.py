import numpy as np
from PIL import Image, ImageDraw
import part2,part4


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

ogImage = Image.open('star2.png')
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

print(f'{part2.XShear(point,2)}  {part2.YShear(point, 3)} {part2.XYShear(point, 2)}')
print(f'{part2.XMult(point,2)}  {part2.YMult(point, 3)} {part2.XYMult(point, 2)}')

imageMatrix = np.array(ogImage)
print(imageMatrix[10][100])

rotatedImageMatrix = np.rot90(imageMatrix, k=1)
rotatedImage = Image.fromarray(rotatedImageMatrix)
rotatedImage.show()
rotatedImage.save("cc90.png")

def reflect (image):
    # Define the reflection matrix
    reflection_matrix = np.array([[-1, 0],
                                   [0, -1]])
    
    # Apply the reflection matrix to each channel of the image
    reflected_image = np.zeros_like(image)
    for channel in range(image.shape[2]):
        reflected_image[:, :, channel] = np.flipud(np.fliplr(image[:, :, channel]))
    
    return reflected_image

reflectImageMatrix = reflect(imageMatrix)
reflectedImage = Image.fromarray(reflectImageMatrix)
reflectedImage.show()
reflectedImage.save("reflected.png")

# Zoom the original image by a factor of 2
zoom_factor = 2
zoomed_image_matrix = np.kron(imageMatrix, np.ones((zoom_factor, zoom_factor, 1), dtype=np.uint8))

# Display or save the zoomed image
zoomed_image = Image.fromarray(zoomed_image_matrix)
zoomed_image.show()
zoomed_image.save("zoomed.png")


new_image = np.zeros((200, 200, 3), dtype=np.uint8)
for i in range(200):
    for j in range(200):
        x, y = part2.ReflectYMX((i, j), 3)
        x, y = int(x), int(y)  # Ensure x and y are integers
        if y in range(200):
           new_image[x, y] = imageMatrix[i, j]
        #else:
          # new_image[x, j] = imageMatrix[i, j]


reflect3 = Image.fromarray(new_image)
reflect3.save("reflect3.png")
reflect3.show()

part4.make_gif(part4.make_img_arr())

