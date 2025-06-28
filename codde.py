import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
num_cameras = 12        # Number of cameras around the head
radius = 0.25           # Radius (in meters) of the camera rig
elevation_angle = 0     # Elevation angle for all cameras (0° = horizontal plane)

# Compute camera positions
azimuths = np.linspace(0, 2 * np.pi, num_cameras, endpoint=False)
elev = np.deg2rad(elevation_angle)

x = radius * np.cos(azimuths) * np.cos(elev)
y = radius * np.sin(azimuths) * np.cos(elev)
z = radius * np.sin(elev) * np.ones_like(azimuths)

# Plot
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, s=50)

# Draw head sphere
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 50)
xs = 0.1 * np.outer(np.cos(u), np.sin(v))  # head radius 0.1m
ys = 0.1 * np.outer(np.sin(u), np.sin(v))
zs = 0.1 * np.outer(np.ones_like(u), np.cos(v))
ax.plot_surface(xs, ys, zs, alpha=0.3)

# Labels & Presentation
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('Camera Placement Around Head')
ax.set_box_aspect([1,1,1])
plt.show()
