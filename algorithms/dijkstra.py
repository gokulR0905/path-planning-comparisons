import heapq
import time
from typing import List, Tuple, Dict, Optional

class DijkstraPathfinder:
   
    #We prioritize g-cost in dijstra, we use a priority queue storing nodes according to lowest g-cost.
    def __init__(self, grid):
        #intitializing the grid and the nodes expanded
        self.grid = grid
        self.nodes_expanded = 0  
    
    def find_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> Dict:
        #Main function for dijkstra which finds the shortest path
        #By using a min heap which prioritizes nodes with lowest g-cost we are able to find the shortest path
        start_time = time.time()
        self.nodes_expanded = 0
        
        min_heap = []
        visited_nodes = set()
        start_dist = 0
        dist_from_start = {}
        parent_nodes = {}

        #we push to our heap based on smallest g-cost
        #initialising
        heapq.heappush(min_heap, (start_dist, start))
        dist_from_start[start] = start_dist
        parent_nodes[start] = None

        while min_heap:
            current_dist, current_node = heapq.heappop(min_heap)
            
            #if already visited, skip
            if current_node in visited_nodes:
                continue
                
            #else we add to visited nodes and increment counter
            visited_nodes.add(current_node)
            self.nodes_expanded += 1

            #we check if goal was achieved
            if current_node == goal:
                path = self.reconstruct_path(goal, parent_nodes)
                computation_time = time.time() - start_time
                return {
                    'path': path,
                    'nodes_expanded': self.nodes_expanded,
                    'computation_time': computation_time,
                    'found': True
                }
            
            #checking neighbours
            for neighbour, cost in self.get_neighbours(current_node):
                if neighbour not in visited_nodes:
                    dist = dist_from_start[current_node] + cost

                    if neighbour not in dist_from_start or dist < dist_from_start[neighbour]:
                        dist_from_start[neighbour] = dist
                        parent_nodes[neighbour] = current_node
                        heapq.heappush(min_heap, (dist, neighbour))

        
        computation_time = time.time() - start_time
        return {
            'path': [],
            'nodes_expanded': self.nodes_expanded,
            'computation_time': computation_time,
            'found': False
        }
    
    def get_neighbours(self, position: Tuple[int, int]) -> List[Tuple[Tuple[int, int], float]]:
        #We get neighbours and their costs
        x, y = position
        neighbors = []
        
        #we are working with manhattan distance - 4 directional movement
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            #checking if our neighbours are valid (within bounds and not obstacles)
            if self.grid.is_valid_position(new_x, new_y):
                neighbors.append(((new_x, new_y), 1.0))

        return neighbors

        
    
    def reconstruct_path(self, goal: Tuple[int, int], parent_map: Dict) -> List[Tuple[int, int]]:
        
        #We reconstruct from visited nodes to start node by backtracking
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = parent_map[current]
        return path[::-1]
    
    def calculate_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:

        x1, y1 = pos1
        x2, y2 = pos2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# # Quick test function
# def test_dijkstra():
#     from environment.grid import Grid
    
#     # Create small test grid
#     grid = Grid(5, 5)
    
#     grid.add_obstacle(2, 4)
    
#     # Test pathfinding
#     pathfinder = DijkstraPathfinder(grid)
#     result = pathfinder.find_path((0, 0), (4, 4))
    
#     print(f"Path found: {result['found']}")
#     print(f"Nodes expanded: {result['nodes_expanded']}")
#     print(f"Path: {result['path']}")

# if __name__ == "__main__":
#     test_dijkstra() 