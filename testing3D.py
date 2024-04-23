import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the size of the raster matrix
size = 10

# Create an empty raster matrix
raster = np.zeros((size, size, size), dtype=np.uint8)

# Define the coordinates of the vertices of the triangular prism
vertices = np.array([[0, 0, 0],
                      [1, 0, 0],
                      [0.5, 1, 0],
                      [0, 0, 1],
                      [1, 0, 1],
                      [0.5, 1, 1]])

# Define the edges of the prism
edges = [(0, 1), (1, 2), (2, 0),
         (3, 4), (4, 5), (5, 3),
         (0, 3), (1, 4), (2, 5)]

# Set voxel values for the prism's vertices and edges
for edge in edges:
    start = vertices[edge[0]] * size
    end = vertices[edge[1]] * size
    num_points = int(np.linalg.norm(end - start)) + 1
    x_values = np.linspace(start[0], end[0], num_points)
    y_values = np.linspace(start[1], end[1], num_points)
    z_values = np.linspace(start[2], end[2], num_points)
    for x, y, z in zip(x_values, y_values, z_values):
        raster[int(x), int(y), int(z)] = 1

# Print the raster matrix
print(raster)