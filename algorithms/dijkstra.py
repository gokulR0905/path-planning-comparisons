import heapq
import time
import psutil
import os
from typing import Tuple, Dict, Set
from .base import BasePathfinder, PathResult


class DijkstraPathfinder(BasePathfinder):
    
    def __init__(self, grid):
        super().__init__(grid)
        self.algorithm_name = "Dijkstra"
    
    def find_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> PathResult:
        #We use Dijkstra's algorithm to find the shortest path between two points in a grid
        #This is done using a heap -> priority queue to keep track of shortest path
        start_time = time.time()
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB
        
        self.reset_metrics()
        
        #Initialize data structures with min_heap holding (cost, pos)
        min_heap = [(0.0, start)]  
        visited: Set[Tuple[int, int]] = set()
        distances: Dict[Tuple[int, int], float] = {start: 0.0}
        parent_map: Dict[Tuple[int, int], Tuple[int, int]] = {start: None}
        
        while min_heap:
            current_dist, current_pos = heapq.heappop(min_heap)
            
       
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
            
            #Neighbour processing -> we follow a similar approach to bfs but with a priority queue
            for neighbor_pos, move_cost in self.get_neighbors(current_pos):
                if neighbor_pos not in visited:
                    tentative_distance = current_dist + move_cost
                    
                 
                    if (neighbor_pos not in distances or 
                        tentative_distance < distances[neighbor_pos]):
                        distances[neighbor_pos] = tentative_distance
                        parent_map[neighbor_pos] = current_pos
                        heapq.heappush(min_heap, (tentative_distance, neighbor_pos))
        
        computation_time = time.time() - start_time
        current_memory = process.memory_info().rss / 1024 / 1024
        memory_usage = current_memory - initial_memory
        
        #Our results
        return PathResult(
            path=[],
            path_length=0.0,
            nodes_expanded=self.nodes_expanded,
            computation_time=computation_time,
            memory_usage=memory_usage,
            algorithm_name=self.algorithm_name,
            found=False
        ) 