# Simulation Logic

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Sandpile class with a 2D grid and grain adding method
class Sandpile:
    def __init__(self, size=20):
        self.size = size
        self.grid = np.zeros((size,size)) # create square grid of given size initialized to zero

    def add_grain(self, x, y):
        self.grid[x, y] += 1

    def display(self):
        print(self.grid)

    def topple(self):
        unstable = True # check if we still have unstable cells
        while unstable:
            unstable = False #assume stability unless we find a problem

            for x in range(self.size):
                for y in range(self.size):
                    if self.grid[x,y] >= 4:
                        # topple
                        self.grid[x,y] -= 4

                        #distribute one grain to each neighbour
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x+dx, y+dy

                            if 0 <= nx < self.size and 0 <= ny < self.size:
                                self.grid[nx, ny] += 1

                        # set for next iteration
                        unstable = True

    def visualize(self):
        plt.imshow(self.grid, cmap="plasma", interpolation="nearest")
        plt.colorbar(label="Number of grains")
        plt.title("Sandpile Configuration")
        plt.show()

    def animate(self, num_frames=200, drop_location=None):
        """
        Animation of sanpile
        """
        fig, ax = plt.subplots()
        im = ax.imshow(self.grid, cmap='viridis', vmin=0, vmax=4)
        plt.colorbar(im, ax=ax, label='Number of grains')

        def update(frame):
            # Drop grain at fixed or random location
            if drop_location:
                x, y = drop_location
            else:
                x = np.random.randint(0, self.size)
                y = np.random.randint(0, self.size)
            self.add_grain(x,y)
            self.topple()
            im.set_array(self.grid)
            return [im]
        
        ani = animation.FuncAnimation(
            fig, update, frames=num_frames, interval=50, blit=True
        )

        plt.title("Sandpile Animation")
        plt.show()