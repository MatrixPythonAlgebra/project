import numpy as np
from PIL import Image, ImageDraw

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