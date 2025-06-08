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

## Project Structure
```
path_planning_project/
├── algorithms/
│   ├── __init__.py
│   ├── dijkstra.py          # Dijkstra implementation
│   ├── astar.py             # A* implementation
│   └── base.py              # Base pathfinding class
├── environment/
│   ├── __init__.py
│   ├── grid.py              # Grid map representation
│   └── obstacles.py         # Obstacle generation
├── visualization/
│   ├── __init__.py
│   ├── plotter.py           # Static visualizations
│   └── animator.py          # Real-time animations
├── analysis/
│   ├── __init__.py
│   ├── metrics.py           # Performance metrics
│   └── performance.py       # Analysis and reporting
├── tests/
│   ├── test_algorithms.py   # Algorithm unit tests
│   └── test_environment.py  # Environment tests
├── results/
│   ├── plots/               # Generated visualizations
│   └── reports/             # Performance reports
├── main.py                  # Main simulation runner
├── requirements.txt         # Dependencies
└── README.md               # This file
```

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
  - Memory usage tracking
  - Path optimality verification
  - Statistical comparisons

- **Rich Visualizations**
  - Grid visualization with obstacles, paths, and visited nodes
  - Side-by-side algorithm comparisons
  - Performance metric charts
  - Real-time pathfinding animations
  - Multi-scenario analysis plots

## Metrics Analyzed
| Metric | Description | Purpose |
|--------|-------------|---------|
| **Nodes Expanded** | Number of nodes explored during search | Algorithm efficiency |
| **Computation Time** | Time taken to find path | Speed comparison |
| **Path Length** | Total distance of found path | Solution quality |
| **Memory Usage** | Peak memory consumption | Resource efficiency |
| **Success Rate** | Percentage of successful pathfinds | Robustness |

## Expected Results
- **A*** should expand fewer nodes due to heuristic guidance
- **Dijkstra** guarantees optimal paths but explores more nodes
- **A*** typically faster for most scenarios
- Both find optimal paths when A* uses admissible heuristics
- Performance varies with obstacle density and configuration

## Installation
```bash
# Clone the repository
git clone <repository-url>
cd path_planning_project

# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
# Run complete comparison demo
python main.py

# Run specific algorithm comparison
python -c "from main import PathPlanningSimulation; sim = PathPlanningSimulation(); sim.run_demo()"

# Generate performance analysis
python analysis/performance.py
```

## Quick Start Example
```python
from environment import Grid, ObstacleGenerator
from algorithms import DijkstraPathfinder, AStarPathfinder

# Create environment
grid = Grid(20, 20)
ObstacleGenerator.generate_random_obstacles(grid, density=0.3)

# Initialize algorithms
dijkstra = DijkstraPathfinder(grid)
astar = AStarPathfinder(grid, heuristic_type="euclidean")

# Compare performance
start, goal = (0, 0), (19, 19)
dijkstra_result = dijkstra.find_path(start, goal)
astar_result = astar.find_path(start, goal)

print(f"Dijkstra nodes expanded: {dijkstra_result.nodes_expanded}")
print(f"A* nodes expanded: {astar_result.nodes_expanded}")
```

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
- [ ] 3D pathfinding extension

## Performance Insights
Based on typical results:
- A* reduces node exploration by 40-70% compared to Dijkstra
- Computation time improvement of 50-80% with A*
- Both algorithms maintain path optimality
- A* advantage increases with larger grids and complex environments

## Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-analysis`)
3. Implement changes with tests
4. Submit pull request with performance comparison

## License
MIT License - see LICENSE file for details

## References
- Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). A formal basis for the heuristic determination of minimum cost paths.
- Dijkstra, E. W. (1959). A note on two problems in connexion with graphs.
- Russell, S., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach. 