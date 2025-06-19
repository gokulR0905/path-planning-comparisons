from typing import Set, Tuple, List
import random


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.obstacles: Set[Tuple[int, int]] = set()
    
    def add_obstacle(self, x: int, y: int):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.obstacles.add((x, y))
    
    def remove_obstacle(self, x: int, y: int):
        self.obstacles.discard((x, y))
    
    def is_obstacle(self, x: int, y: int) -> bool:
        return (x, y) in self.obstacles
    
    def is_valid_position(self, x: int, y: int) -> bool:
        return (0 <= x < self.width and 
                0 <= y < self.height and 
                not self.is_obstacle(x, y))
    
    def clear_obstacles(self):
        self.obstacles.clear()
    
    def get_free_positions(self) -> List[Tuple[int, int]]:
        free_positions = []
        for x in range(self.width):
            for y in range(self.height):
                if not self.is_obstacle(x, y):
                    free_positions.append((x, y))
        return free_positions
    
    def get_random_free_position(self) -> Tuple[int, int]:
        free_positions = self.get_free_positions()
        if not free_positions:
            raise ValueError("No free positions available")
        return random.choice(free_positions)
    
    def get_obstacle_density(self) -> float:
        total_cells = self.width * self.height
        return len(self.obstacles) / total_cells if total_cells > 0 else 0.0
    
    def __str__(self) -> str:
        result = []
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if self.is_obstacle(x, y):
                    row += "█"  
                else:
                    row += "·" 
            result.append(row)
        return "\n".join(result) 