import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the coordinates of the vertices of the triangular prism
vertices = np.array([[0, 0, 0],
                      [1, 0, 0],
                      [0.5, 1, 0],
                      [0, 0, 1],
                      [1, 0, 1],
                      [0.5, 1, 1]])

# Define the triangular faces of the prism
faces = [[vertices[0], vertices[1], vertices[2]],
         [vertices[3], vertices[4], vertices[5]],
         [vertices[0], vertices[1], vertices[4], vertices[3]],
         [vertices[2], vertices[5], vertices[4], vertices[1]],
         [vertices[0], vertices[3], vertices[5], vertices[2]]]

# Create a 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the triangular prism
ax.add_collection3d(Poly3DCollection(faces, facecolors='red', linewidths=1, edgecolors='black'))

# Set plot limits
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()