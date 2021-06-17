import numpy as np
from scipy.stats import geom

def truncated_geom_rvs(p, n):
    k = geom.rvs(p)
    if k <= n:
        return k
    else:
        return n

def get_path_grid_path(grid, start):


    path = []
    path_component = [start]
    
    while np.count_nonzero(grid)



class Peruser:
    
    def __init__(self, grid):
        self.grid = grid
        self.num_sizes = len(grid)
        self.num_colors = len(grid[0])
        self.path = []









