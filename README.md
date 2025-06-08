# Path Planning Algorithm Comparison: A* vs Dijkstra

## Project Overview
This project implements and compares two fundamental pathfinding algorithms to analyze their performance characteristics and efficiency trade-offs:

- **Dijkstra's Algorithm** - Uninformed search that guarantees shortest path
- **A* Algorithm** - Informed search using heuristics for efficiency

## Objectives
- Implement both algorithms on grid-based maps with obstacles
- Compare performance metrics: node expansions, computation time, path optimality
- Analyze trade-offs between uninformed vs informed search strategies
- Visualize algorithm execution and results
- Generate comprehensive performance reports

## Key Research Questions
1. How does A* heuristic guidance affect node exploration efficiency?
2. What is the performance difference in various obstacle configurations?
3. How do algorithms scale with grid size and obstacle density?
4. When does each algorithm perform better?


## Features
- **Multiple Algorithm Implementations**
  - Dijkstra's algorithm with priority queue optimization
  - A* with configurable heuristics (Manhattan, Euclidean, Diagonal)
  
- **Diverse Test Environments**
  - Random obstacle placement
  - Maze-like structures
  - Corridor environments
  - Room-based layouts
  - Clustered obstacles

- **Comprehensive Performance Analysis**
  - Node expansion counting
  - Computation time measurement

- **Rich Visualizations**
  - Grid visualization with obstacles, paths, and visited nodes
  - Side-by-side algorithm comparisons
  - Performance metric charts
  - Multi-scenario analysis plots

## Metrics Analyzed
| Metric | Description | Purpose |
|--------|-------------|---------|
| **Nodes Expanded** | Number of nodes explored during search | Algorithm efficiency |
| **Computation Time** | Time taken to find path | Speed comparison |
| **Path Length** | Total distance of found path | Solution quality |
| **Success Rate** | Percentage of successful pathfinds | Robustness |

## Expected Results
- **A*** should expand fewer nodes due to heuristic guidance
- **Dijkstra** guarantees optimal paths but explores more nodes
- **A*** typically faster for most scenarios
- Both find optimal paths when A* uses admissible heuristics
- Performance varies with obstacle density and configuration


## Dependencies
- Python 3.7+
- NumPy - Numerical computations and grid operations
- Matplotlib - Visualization and plotting
- Collections - Data structures (built-in)
- Heapq - Priority queue implementation (built-in)
- Time - Performance timing (built-in)

## Development Roadmap
- [ ] Basic algorithm implementations
- [ ] Grid environment with obstacles
- [ ] Performance metrics collection
- [ ] Visualization system
- [ ] Comprehensive testing suite
- [ ] Statistical analysis tools
- [ ] Documentation and examples
- [ ] Advanced heuristics exploration

## Performance Insights
Based on typical results:
- A* reduces node exploration by 40-70% compared to Dijkstra
- Computation time improvement of 50-80% with A*
- Both algorithms maintain path optimality
- A* advantage increases with larger grids and complex environments
