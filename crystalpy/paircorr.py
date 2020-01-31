# Import the champions
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

'''
GENERATE DATA SETS
'''

# Animation parameters
spatial_resolution = 0.1
tot_frames = 360
fps = 30

# Generate expanding circle
circle_angles = np.linspace(0, 2*np.pi, num=100, endpoint=True)
x_pos = np.cos(circle_angles)
y_pos = np.sin(circle_angles)
circle_data = np.hstack((x_pos[:,None], y_pos[:,None])) * spatial_resolution
data_1 = [frame * circle_data for frame in range(tot_frames)]

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
#ax2.set_ylim([])
ax2.set_title('Pair Correlation Function', fontsize=font)

'''
ANIMATE THE DIAGRAM
'''

ani = FuncAnimation(fig, update, tot_frames, interval=1000/fps, blit=False)
#ani.save('data/animation.gif', writer='imagemagick', fps=fps)
plt.show()
