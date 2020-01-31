# Import the champions
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

'''
GENERATE DATA SETS
'''



'''
PLOT SYSTEM
'''

# Initiate axes for crystal diagram and pair correlation function
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# Initial positions
line1 = ax1.plot(positions_list[0][:,0], \
				positions_list[0][:,0], \
				positions_list[0][:,0],
				'-o')[0]
line2 = ax2.plot(positions_list[0][:,0], \
				positions_list[0][:,0], \
				positions_list[0][:,0],
				'-o')[0]


# Update axes
def update(frame):

	line1.set_data(positions_list[frame][:,0:2].T)
	line2.set_data(positions_list[frame][:,0:2].T)

'''
CONFIGURE PLOT SETTINGS
'''

# Set limits for the plots
font = 16
ax1.set_xlim([])
ax1.set_ylim([])
ax1.set_title('Crystal Lattice', fontsize=font)
ax2.set_xlim([])
ax2.set_ylim([])
ax2.set_title('Pair Correlation Function', fontsize=font)

'''
ANIMATE THE DIAGRAM
'''

fps = 60
ani = FuncAnimation(fig, update, num_steps, interval=1000/fps, blit=False)
#ani.save('data/animation.gif', writer='imagemagick', fps=fps)
plt.show()
