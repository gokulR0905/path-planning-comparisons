# Path Planning Algorithm Comparison: Dijkstra vs A*

## Project Overview
This project implements and compares Dijkstra's and A* path planning algorithms on graph-based maps to determine the most efficient routes. The analysis focuses on performance trade-offs between uninformed and informed search strategies.

## Key Features
- **Complete implementations** of Dijkstra and A* algorithms
- **Performance analysis** including node expansions, computation time, and memory usage
- **Multiple test scenarios** with varying obstacle configurations
- **Comprehensive visualization** of paths and performance metrics
- **Statistical comparison** of algorithm efficiency

## Algorithms Implemented

### Dijkstra's Algorithm (Uninformed Search)
- Guarantees shortest path
- Explores nodes uniformly in all directions
- Uses actual distance from start (g-cost only)

### A* Algorithm (Informed Search)
- Uses heuristic function for guidance
- More efficient node exploration
- Maintains optimality with admissible heuristics

## Performance Metrics Analyzed
- **Node Expansions**: Number of nodes explored during search
- **Computation Time**: Time taken to find the optimal path
- **Memory Usage**: Peak memory consumption during execution
- **Path Length**: Total distance of discovered path



## Expected Results
Based on algorithm characteristics:
- **A* reduces node exploration by 40-70%** compared to Dijkstra
- **A* provides 50-80% faster computation** in most scenarios
- **Both algorithms maintain path optimality**
- **A* advantage increases with grid size and complexity**


## Key Findings
The analysis demonstrates clear performance advantages of informed search (A*) over uninformed search (Dijkstra) while maintaining solution optimality. A* takes lesser time and finds the optimal path through the usage of the heuristic 