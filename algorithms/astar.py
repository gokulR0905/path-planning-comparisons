import heapq
import time
import psutil
import os
from typing import Tuple, Dict, Set
from .base import BasePathfinder, PathResult


class AStarPathfinder(BasePathfinder):
    def __init__(self, grid, heuristic_type: str = "euclidean"):
        super().__init__(grid)
        self.algorithm_name = "A*"
        self.heuristic_type = heuristic_type
    
    def heuristic(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
        #We use a heuristic to guide search quicker
        x1, y1 = pos1
        x2, y2 = pos2
        
        if self.heuristic_type == "manhattan":
            return abs(x1 - x2) + abs(y1 - y2)
        elif self.heuristic_type == "euclidean":
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        elif self.heuristic_type == "diagonal":
            dx, dy = abs(x1 - x2), abs(y1 - y2)
            return 1.414 * min(dx, dy) + abs(dx - dy)
        else:
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    
    def find_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> PathResult:
        start_time = time.time()
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB
        
        self.reset_metrics()
        
        #Our priority queue holds (f_cost, g_cost, position), here f_cost = g_cost + h_cost
        start_g = 0.0
        start_h = self.heuristic(start, goal)
        start_f = start_g + start_h
        
        min_heap = [(start_f, start_g, start)]
        visited: Set[Tuple[int, int]] = set()
        g_costs: Dict[Tuple[int, int], float] = {start: 0.0}
        parent_map: Dict[Tuple[int, int], Tuple[int, int]] = {start: None}
        
        #Similar to bfs but with a priority queue and a heuristic
        while min_heap:
            current_f, current_g, current_pos = heapq.heappop(min_heap)
            
            if current_pos in visited:
                continue
            
            visited.add(current_pos)
            self.nodes_expanded += 1

            if current_pos == goal:
                path = self.reconstruct_path(goal, parent_map)
                path_length = self.calculate_path_length(path)
                computation_time = time.time() - start_time
                
                current_memory = process.memory_info().rss / 1024 / 1024
                memory_usage = current_memory - initial_memory
                
                return PathResult(
                    path=path,
                    path_length=path_length,
                    nodes_expanded=self.nodes_expanded,
                    computation_time=computation_time,
                    memory_usage=memory_usage,
                    algorithm_name=self.algorithm_name,
                    found=True
                )
            
            for neighbor_pos, move_cost in self.get_neighbors(current_pos):
                if neighbor_pos not in visited:
                    tentative_g = current_g + move_cost

                    if (neighbor_pos not in g_costs or 
                        tentative_g < g_costs[neighbor_pos]):
                        g_costs[neighbor_pos] = tentative_g
                        parent_map[neighbor_pos] = current_pos
                        
                        h_cost = self.heuristic(neighbor_pos, goal)
                        f_cost = tentative_g + h_cost
                        
                        heapq.heappush(min_heap, (f_cost, tentative_g, neighbor_pos))
        
        computation_time = time.time() - start_time
        current_memory = process.memory_info().rss / 1024 / 1024
        memory_usage = current_memory - initial_memory
        
        return PathResult(
            path=[],
            path_length=0.0,
            nodes_expanded=self.nodes_expanded,
            computation_time=computation_time,
            memory_usage=memory_usage,
            algorithm_name=self.algorithm_name,
            found=False
        ) 