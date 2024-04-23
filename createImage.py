import numpy as np
from PIL import Image, ImageDraw
import part2

width = 200
height = 200
image = Image.new('RGB', (width, height), color = 'white')
draw = ImageDraw.Draw(image)

starPoints = [
    (100, 10),
    (170, 190),
    (0, 80),
    (200, 80),
    (30, 190),
    (100, 10),
    (100, 117),
    (59, 117)
]

draw.polygon(starPoints, fill=None, outline='red')
image.save("star2.png")
image.show()

newStar = []
new_image = np.zeros((200, 200, 3), dtype=np.uint8)
for point in starPoints:
    newPoint = part2.XShear(point, 4)
    newStar.append(newPoint)

reflect3 = Image.new('RGB', (400, 400), color = 'white')
draw3 = ImageDraw.Draw(reflect3)

draw3.polygon(newStar, fill=None, outline='red')
reflect3.save("sheared.png")
reflect3.show()


