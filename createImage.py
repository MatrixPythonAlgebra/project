import numpy as np
from PIL import Image, ImageDraw

width = 200
height = 200
image = Image.new('RGB', (width, height), color = 'white')
draw = ImageDraw.Draw(image)

starPoints = [
    (100, 10),
    (130, 80),
    (200, 80),
    (150, 120),
    (170, 190),
    (100, 150),
    (30, 190),
    (50, 120),
    (0, 80),
    (70, 80)
]

draw.polygon(starPoints, fill=None, outline='red')
image.save("star.png")
image.show()