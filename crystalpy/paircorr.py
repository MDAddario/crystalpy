# Import the champions
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

'''
CREATE CIRCLE OBJECT
'''

# Generate circle position array
circle_res = 100
circle_angles = np.linspace(0, 2*np.pi, num=circle_res, endpoint=True)
x_pos = np.cos(circle_angles)
y_pos = np.sin(circle_angles)
unit_circle = np.hstack((x_pos[:,None], y_pos[:,None]))

'''
CUBIC LATTICE
'''

# User set parameters
a = 10
atom_size = 1
index_range = 3

# Direct lattice vectors
a1 = a * np.array([1, 0])
a2 = a * np.array([0, 1])

# Construct lattice
width = 2 * index_range + 1
lattice = np.empty((width**2, 2))

for n1 in range(-index_range, index_range+1):
	for n2 in range(-index_range, index_range+1):
	
		index = (n1 + index_range) * width + (n2 + index_range)
		lattice[index, :] = n1 * a1 + n2 * a2
		
atom_circle = unit_circle * atom_size
atoms = [atom_circle + offset for offset in lattice]

'''
GENERATE DATA SETS
'''

# Animation parameters
spatial_resolution = 0.1
tot_frames = 360
fps = 30

# Generate expanding circle
circle_quantum = unit_circle * spatial_resolution
data_1 = [frame * circle_quantum for frame in range(tot_frames)]

# Generate random curve g(r)
x_vals = (np.arange(tot_frames) * spatial_resolution)
y_vals = (np.sin(x_vals))
data_2 = np.hstack((x_vals[:,None], y_vals[:,None]))

'''
PLOT SYSTEM
'''

# Initiate axes for crystal diagram and pair correlation function
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# Paste the atoms
for atom in atoms:
	ax1.plot(atom[:,0], atom[:,1], '-', c='r')

# Initial positions
line1 = ax1.plot(data_1[0][:,0], \
				data_1[0][:,1], \
				'-')[0]
line2 = ax2.plot(data_2[:,0], \
				data_2[:,1], \
				'-')[0]

# Update axes
def update(frame):

	line1.set_data(data_1[frame][:,0:2].T)
	line2.set_data(data_2[0:frame+1,0:2].T)

'''
CONFIGURE PLOT SETTINGS
'''

# Set limits for the plots
font = 16
size = tot_frames * spatial_resolution
ax1.set_xlim([-size, size])
ax1.set_ylim([-size, size])
ax1.set_title('Crystal Lattice', fontsize=font)
ax2.set_xlim([0, size])
ax2.set_ylim([0, 5])
ax2.set_title('Pair Correlation Function', fontsize=font)

'''
ANIMATE THE DIAGRAM
'''

ani = FuncAnimation(fig, update, tot_frames, interval=1000/fps, blit=False)
#ani.save('data/animation.gif', writer='imagemagick', fps=fps)
plt.show()
