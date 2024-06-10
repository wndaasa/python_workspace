import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Define vertices of a 5D hypercube
vertices = np.array([[int(x) for x in format(i, '05b')] for i in range(2**5)]) * 2 - 1

# Define edges of a 5D hypercube
edges = []
for i in range(2**5):
    for j in range(5):
        neighbor = i ^ (1 << j)
        if neighbor > i:
            edges.append((i, neighbor))

# Function to project 5D vertices to 3D
def project_5d_to_3d(vertices, angles):
    projection_matrix = np.eye(5)
    for i in range(5):
        for j in range(i+1, 5):
            rotation_matrix = np.eye(5)
            rotation_matrix[i, i] = np.cos(angles[i, j])
            rotation_matrix[i, j] = -np.sin(angles[i, j])
            rotation_matrix[j, i] = np.sin(angles[i, j])
            rotation_matrix[j, j] = np.cos(angles[i, j])
            projection_matrix = projection_matrix @ rotation_matrix
    
    rotated_vertices = vertices @ projection_matrix.T
    return rotated_vertices[:, :3]

# Function to plot the 3D projected vertices and edges
def plot_hypercube(ax, vertices):
    ax.cla()
    ax.set_box_aspect([1,1,1])
    for edge in edges:
        points = vertices[list(edge), :]
        ax.plot3D(*zip(*points), color='cyan')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')  
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_title('5D Hypercube projection in 3D space')
    ax.grid(False)
    ax.axis('off')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')

# Initialize the anglesj 
angles = np.zeros((5, 5))

def update(frame):
    global angles
    for i in range(5):
        for j in range(i+1, 5):
            angles[i, j] += np.pi / 150
            angles[j, i] -= np.pi / 150
    projected_vertices = project_5d_to_3d(vertices, angles)
    plot_hypercube(ax, projected_vertices)

ani = FuncAnimation(fig, update, frames=3600, interval=1)

plt.show()
