"""
Simple test for Dijkstra algorithm implementation.
"""

from environment.grid import Grid
from algorithms.dijkstra import DijkstraPathfinder

def test_dijkstra():
    """Test the Dijkstra implementation."""
    print("Testing Dijkstra Algorithm...")
    
    # Create small test grid
    grid = Grid(5, 5) 
    grid.add_obstacle(0, 4)
    grid.add_obstacle(4, 0)# Add one obstacle
    grid.add_obstacle(2, 4)
    grid.add_obstacle(3, 4)
    grid.add_obstacle(3, 3)
    
    print("Grid:")
    print(grid)
    print()
    
    # Test pathfinding
    pathfinder = DijkstraPathfinder(grid)
    result = pathfinder.find_path((0, 0), (4, 4))
    
    print(f"Path found: {result['found']}")
    print(f"Nodes expanded: {result['nodes_expanded']}")
    print(f"Computation time: {result['computation_time']:.4f}s")
    print(f"Path: {result['path']}")
    print(f"Path length: {len(result['path']) if result['found'] else 0} steps")

if __name__ == "__main__":
    test_dijkstra() 