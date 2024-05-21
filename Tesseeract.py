import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Define vertices of a 7D hypercube and scale them to increase size
vertices = np.array([[int(x) for x in format(i, '07b')] for i in range(2**7)]) * 4

# Define edges of a 7D hypercube
edges = []
for i in range(2**7):
    for j in range(7):
        neighbor = i ^ (1 << j)
        if neighbor > i:
            edges.append((i, neighbor))

# Function to project 7D vertices to 3D
def project_7d_to_3d(vertices, angles):
    projection_matrix = np.eye(7)
    for i in range(7):
        for j in range(i+1, 7):
            rotation_matrix = np.eye(7)
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
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])
    ax.set_title('7D Hypercube projection in 3D space')
    ax.grid(True)
    ax.axis('on')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')

# Initialize the angles
angles = np.zeros((7, 7))

def update(frame):
    global angles
    for i in range(7):
        for j in range(i+1, 7):
            angles[i, j] += np.pi / 180
            angles[j, i] -= np.pi / 180
    projected_vertices = project_7d_to_3d(vertices, angles)
    plot_hypercube(ax, projected_vertices)

ani = FuncAnimation(fig, update, frames=360, interval=50)

plt.show()
