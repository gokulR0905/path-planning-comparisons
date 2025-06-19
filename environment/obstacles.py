import random
from typing import List, Tuple
from .grid import Grid


class ObstacleGenerator:
    @staticmethod
    def generate_random_obstacles(grid: Grid, density: float, seed: int = None):
        if seed is not None:
            random.seed(seed)
        
        total_cells = grid.width * grid.height
        num_obstacles = int(total_cells * density)
        
        positions = [(x, y) for x in range(grid.width) for y in range(grid.height)]
        obstacle_positions = random.sample(positions, min(num_obstacles, len(positions)))
        
        for x, y in obstacle_positions:
            grid.add_obstacle(x, y)
    
    @staticmethod
    def generate_maze_obstacles(grid: Grid, seed: int = None):
        if seed is not None:
            random.seed(seed)
        
        #Create corridors with random walls
        for x in range(0, grid.width, 3):
            for y in range(grid.height):
                if random.random() < 0.7:
                    grid.add_obstacle(x, y)
        
        for y in range(0, grid.height, 3):
            for x in range(grid.width):
                if random.random() < 0.7:
                    grid.add_obstacle(x, y)
        
        #Add some random obstacles in corridors
        for _ in range(grid.width * grid.height // 20):
            x = random.randint(0, grid.width - 1)
            y = random.randint(0, grid.height - 1)
            if random.random() < 0.3:
                grid.add_obstacle(x, y)
    
    @staticmethod
    def generate_corridor_obstacles(grid: Grid, num_corridors: int = 3, seed: int = None):
        if seed is not None:
            random.seed(seed)
        for x in range(grid.width):
            for y in range(grid.height):
                grid.add_obstacle(x, y)
        
        corridor_spacing = grid.height // (num_corridors + 1)
        for i in range(num_corridors):
            y = corridor_spacing * (i + 1)
            for x in range(grid.width):
                grid.remove_obstacle(x, y)
                if y > 0 and random.random() < 0.2:
                    grid.remove_obstacle(x, y - 1)
                if y < grid.height - 1 and random.random() < 0.2:
                    grid.remove_obstacle(x, y + 1)

        for _ in range(num_corridors - 1):
            x = random.randint(1, grid.width - 2)
            for y in range(grid.height):
                if random.random() < 0.6:
                    grid.remove_obstacle(x, y)
    
    @staticmethod
    def generate_clustered_obstacles(grid: Grid, num_clusters: int = 5, seed: int = None):
        #Clustered obstacles
        if seed is not None:
            random.seed(seed)
        
        for _ in range(num_clusters):
            center_x = random.randint(2, grid.width - 3)
            center_y = random.randint(2, grid.height - 3)
            cluster_size = random.randint(3, 6)
           
            for _ in range(cluster_size ** 2):
                offset_x = random.randint(-cluster_size//2, cluster_size//2)
                offset_y = random.randint(-cluster_size//2, cluster_size//2)
                
                x = center_x + offset_x
                y = center_y + offset_y
                
                if (0 <= x < grid.width and 0 <= y < grid.height and 
                    random.random() < 0.7):
                    grid.add_obstacle(x, y)
    
    @staticmethod
    def generate_diagonal_obstacles(grid: Grid, num_diagonals: int = 3, seed: int = None):
        if seed is not None:
            random.seed(seed)
        
        for i in range(num_diagonals):
            #Alternate between main diagonals
            if i % 2 == 0:
                #Main diagonal (top-left to bottom-right)
                offset = random.randint(-grid.width//4, grid.width//4)
                for d in range(max(grid.width, grid.height)):
                    x = d + offset
                    y = d
                    if 0 <= x < grid.width and 0 <= y < grid.height:
                        if random.random() < 0.8:
                            grid.add_obstacle(x, y)
            else:
                #Anti-diagonal (top-right to bottom-left)
                offset = random.randint(-grid.width//4, grid.width//4)
                for d in range(max(grid.width, grid.height)):
                    x = grid.width - 1 - d + offset
                    y = d
                    if 0 <= x < grid.width and 0 <= y < grid.height:
                        if random.random() < 0.8:
                            grid.add_obstacle(x, y) 