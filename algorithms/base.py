"""
Base pathfinding class with common functionality.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Tuple, Optional
import time


@dataclass
class PathResult:
    path: List[Tuple[int, int]]
    path_length: float
    nodes_expanded: int
    computation_time: float
    memory_usage: float
    algorithm_name: str
    found: bool = True


class BasePathfinder(ABC):
    
    def __init__(self, grid):
        self.grid = grid
        self.nodes_expanded = 0
        self.algorithm_name = "Base"
    
    def reset_metrics(self):
        self.nodes_expanded = 0
    
    def get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[Tuple[int, int], float]]:
        #finding neighbours on the basis of manhattan distance
        x, y = position
        neighbors = []
       
        #Manhattan distance
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if self.grid.is_valid_position(new_x, new_y):
                neighbors.append(((new_x, new_y), 1.0))
        
        return neighbors
    
    def reconstruct_path(self, goal: Tuple[int, int], parent_map: dict) -> List[Tuple[int, int]]:
        #Backtracking to get the path from goal to start
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = parent_map.get(current)
        return path[::-1]  
    
    def calculate_path_length(self, path: List[Tuple[int, int]]) -> float:
        if len(path) < 2:
            return 0.0
        
        length = 0.0
        for i in range(1, len(path)):
            x1, y1 = path[i-1]
            x2, y2 = path[i]
            # Euclidean distance
            length += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        
        return length
    
    @abstractmethod
    def find_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> PathResult:
        pass 