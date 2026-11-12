import matplotlib
matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from skimage.measure import marching_cubes

# Figure
fig = plt.figure(facecolor="black")
ax = fig.add_subplot(111, projection="3d")
ax.set_facecolor("black")
ax.set_axis_off()

# Coordinate grid
n = 100
x = np.linspace(-2, 2, n)
y = np.linspace(-2, 2, n)
z = np.linspace(-2, 2, n)

X, Y, Z = np.meshgrid(x, y, z, indexing="ij")

# Original implicit heart equation
F = (
    (X**2 + (9/4)*Y**2 + Z**2 - 1)**3
    - X**2 * Z**3
    - (9/80)*Y**2 * Z**3
)

print("Minimum:", F.min())
print("Maximum:", F.max())
print("Zero crossings:", np.any(F < 0) and np.any(F > 0))

# Extract surface
verts, faces, normals, values = marching_cubes(
    F,
    level=0,
    spacing=(x[1]-x[0], y[1]-y[0], z[1]-z[0])
)

# Shift vertices to correct coordinates
verts[:, 0] += x[0]
verts[:, 1] += y[0]
verts[:, 2] += z[0]

# Plot surface
ax.plot_trisurf(
    verts[:, 0],
    verts[:, 1],
    faces,
    verts[:, 2],
    color="red",
    edgecolor="darkred",
    linewidth=0.05,
    alpha=1
)

# Axis limits
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)

# Equal proportions
ax.set_box_aspect((1, 1, 1))

# Animation
def animate(i):
    ax.view_init(elev=15, azim=i)
    return ax,

anim = animation.FuncAnimation(
    fig,
    animate,
    frames=360,
    interval=20,
    blit=False
)

plt.show()