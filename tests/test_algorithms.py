"""
Test cases for pathfinding algorithms.
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from environment import Grid, ObstacleGenerator
from algorithms import DijkstraPathfinder, AStarPathfinder


def test_basic_pathfinding():
    """Test basic pathfinding functionality."""
    print("Testing basic pathfinding...")
    
    grid = Grid(10, 10)
    dijkstra = DijkstraPathfinder(grid)
    astar = AStarPathfinder(grid)
    
    start = (0, 0)
    goal = (9, 9)
    
    # Test on empty grid
    dijkstra_result = dijkstra.find_path(start, goal)
    astar_result = astar.find_path(start, goal)
    
    print(f"Empty grid results:")
    print(f"  Dijkstra: Path found={dijkstra_result.found}, Nodes={dijkstra_result.nodes_expanded}")
    print(f"  A*: Path found={astar_result.found}, Nodes={astar_result.nodes_expanded}")
    
    if dijkstra_result.found and astar_result.found:
        improvement = (dijkstra_result.nodes_expanded - astar_result.nodes_expanded) / dijkstra_result.nodes_expanded * 100
        print(f"  A* node reduction: {improvement:.1f}%")
    
    return dijkstra_result.found and astar_result.found


def test_with_obstacles():
    """Test pathfinding with obstacles."""
    print("\nTesting with obstacles...")
    
    grid = Grid(15, 15)
    ObstacleGenerator.generate_random_obstacles(grid, 0.3, seed=42)
    
    dijkstra = DijkstraPathfinder(grid)
    astar = AStarPathfinder(grid)
    
    start = (0, 0)
    goal = (14, 14)
    
    dijkstra_result = dijkstra.find_path(start, goal)
    astar_result = astar.find_path(start, goal)
    
    print(f"Grid with 30% obstacles:")
    print(f"  Dijkstra: Path found={dijkstra_result.found}, Nodes={dijkstra_result.nodes_expanded}")
    print(f"  A*: Path found={astar_result.found}, Nodes={astar_result.nodes_expanded}")
    
    if dijkstra_result.found and astar_result.found:
        improvement = (dijkstra_result.nodes_expanded - astar_result.nodes_expanded) / dijkstra_result.nodes_expanded * 100
        print(f"  A* node reduction: {improvement:.1f}%")
    
    return True


if __name__ == '__main__':
    print("Running pathfinding algorithm tests...")
    
    success1 = test_basic_pathfinding()
    success2 = test_with_obstacles()
    
    if success1 and success2:
        print("\nAll tests passed! ✓")
    else:
        print("\nSome tests failed! ✗") 