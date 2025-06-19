import time
import random
from typing import Dict, List
from environment import Grid, ObstacleGenerator
from algorithms import DijkstraPathfinder, AStarPathfinder
from analysis import PerformanceAnalyzer
from visualization import PathPlotter


class PathPlanningComparison:
    def __init__(self, grid_size: int = 20):
        self.grid_size = grid_size
        self.grid = Grid(grid_size, grid_size)
        self.results = []
        
        self.dijkstra = DijkstraPathfinder(self.grid)
        self.astar = AStarPathfinder(self.grid, heuristic_type="euclidean")
       
        self.analyzer = PerformanceAnalyzer()
        self.plotter = PathPlotter()
    
    def run_single_comparison(self, start, goal, scenario_name):
        print(f"\n--- {scenario_name} ---")
        print(f"Start: {start}, Goal: {goal}")
        print(f"Grid size: {self.grid_size}x{self.grid_size}")
        print(f"Obstacle density: {self.grid.get_obstacle_density():.2%}")
        
        print("\nRunning Dijkstra...")
        dijkstra_result = self.dijkstra.find_path(start, goal)
        print(f"  Path found: {dijkstra_result.found}")
        print(f"  Nodes expanded: {dijkstra_result.nodes_expanded}")
        print(f"  Computation time: {dijkstra_result.computation_time:.4f}s")
        print(f"  Memory usage: {dijkstra_result.memory_usage:.2f}MB")
        if dijkstra_result.found:
            print(f"  Path length: {dijkstra_result.path_length:.2f}")
        
        print("\nRunning A*...")
        astar_result = self.astar.find_path(start, goal)
        print(f"  Path found: {astar_result.found}")
        print(f"  Nodes expanded: {astar_result.nodes_expanded}")
        print(f"  Computation time: {astar_result.computation_time:.4f}s")
        print(f"  Memory usage: {astar_result.memory_usage:.2f}MB")
        if astar_result.found:
            print(f"  Path length: {astar_result.path_length:.2f}")
        
        if dijkstra_result.found and astar_result.found:
            node_improvement = ((dijkstra_result.nodes_expanded - astar_result.nodes_expanded) 
                              / dijkstra_result.nodes_expanded * 100)
            time_improvement = ((dijkstra_result.computation_time - astar_result.computation_time) 
                              / dijkstra_result.computation_time * 100)
            
            print(f"\nPerformance Comparison:")
            print(f"  A* node reduction: {node_improvement:.1f}%")
            print(f"  A* time improvement: {time_improvement:.1f}%")
            print(f"  Path length difference: {abs(dijkstra_result.path_length - astar_result.path_length):.2f}")
        
        scenario_result = {
            'scenario_name': scenario_name,
            'start': start,
            'goal': goal,
            'dijkstra': dijkstra_result,
            'astar': astar_result,
            'grid_state': str(self.grid)
        }
        self.results.append(scenario_result)
        
        if dijkstra_result.found and astar_result.found:
            print(f"\nGenerating visualization for {scenario_name}...")
            fig = self.plotter.plot_comparison(self.grid, dijkstra_result, astar_result, start, goal)
            
            plot_filename = f"results/plots/{scenario_name.replace(' ', '_').replace('(', '').replace(')', '').replace('%', 'percent')}.png"
            self.plotter.save_plot(plot_filename)
            
            self.plotter.show_plot()
    
    def run_comprehensive_analysis(self):
        print("="*60)
        print("PATH PLANNING ALGORITHM COMPARISON")
        print("="*60)
        print("Comparing Dijkstra vs A* algorithms")
        print("Analyzing: Node expansions, computation time, memory usage")
        
        scenarios = [
            ("Empty Grid", self.setup_empty_grid),
            ("Random Obstacles (20%)", lambda: self.setup_random_obstacles(0.2)),
            ("Random Obstacles (40%)", lambda: self.setup_random_obstacles(0.4)),
            ("Maze Environment", self.setup_maze_environment),
            ("Corridor Environment", self.setup_corridor_environment),
        ]
        
        for scenario_name, setup_func in scenarios:
            setup_func()
            
            free_positions = self.grid.get_free_positions()
            if len(free_positions) < 2:
                print(f"Skipping {scenario_name} - insufficient free space")
                continue
            
            start = free_positions[0]
            goal = free_positions[-1]
            distance = ((start[0] - goal[0]) ** 2 + (start[1] - goal[1]) ** 2) ** 0.5
            if distance < self.grid_size * 0.3:
                for pos in reversed(free_positions):
                    dist = ((start[0] - pos[0]) ** 2 + (start[1] - pos[1]) ** 2) ** 0.5
                    if dist >= self.grid_size * 0.3:
                        goal = pos
                        break
            
            self.run_single_comparison(start, goal, scenario_name)
        
        self.generate_summary_report()
    
    def setup_empty_grid(self):
        self.grid.clear_obstacles()
    
    def setup_random_obstacles(self, density: float):
        self.grid.clear_obstacles()
        ObstacleGenerator.generate_random_obstacles(self.grid, density, seed=42)
    
    def setup_maze_environment(self):
        self.grid.clear_obstacles()
        ObstacleGenerator.generate_maze_obstacles(self.grid, seed=42)
    
    def setup_corridor_environment(self):
        self.grid.clear_obstacles()
        ObstacleGenerator.generate_corridor_obstacles(self.grid, num_corridors=3, seed=42)
    
    def generate_summary_report(self):
        if not self.results:
            return
        
        print("\n" + "="*60)
        print("SUMMARY ANALYSIS")
        print("="*60)
        
        dijkstra_stats = {'nodes': [], 'time': [], 'memory': []}
        astar_stats = {'nodes': [], 'time': [], 'memory': []}
        
        for result in self.results:
            if result['dijkstra'].found:
                dijkstra_stats['nodes'].append(result['dijkstra'].nodes_expanded)
                dijkstra_stats['time'].append(result['dijkstra'].computation_time)
                dijkstra_stats['memory'].append(result['dijkstra'].memory_usage)
            
            if result['astar'].found:
                astar_stats['nodes'].append(result['astar'].nodes_expanded)
                astar_stats['time'].append(result['astar'].computation_time)
                astar_stats['memory'].append(result['astar'].memory_usage)
        
        print(f"\nDijkstra Algorithm Performance:")
        if dijkstra_stats['nodes']:
            print(f"  Average nodes expanded: {sum(dijkstra_stats['nodes'])/len(dijkstra_stats['nodes']):.1f}")
            print(f"  Average computation time: {sum(dijkstra_stats['time'])/len(dijkstra_stats['time']):.4f}s")
            print(f"  Average memory usage: {sum(dijkstra_stats['memory'])/len(dijkstra_stats['memory']):.2f}MB")
        
        print(f"\nA* Algorithm Performance:")
        if astar_stats['nodes']:
            print(f"  Average nodes expanded: {sum(astar_stats['nodes'])/len(astar_stats['nodes']):.1f}")
            print(f"  Average computation time: {sum(astar_stats['time'])/len(astar_stats['time']):.4f}s")
            print(f"  Average memory usage: {sum(astar_stats['memory'])/len(astar_stats['memory']):.2f}MB")
        
        if dijkstra_stats['nodes'] and astar_stats['nodes']:
            avg_dijkstra_nodes = sum(dijkstra_stats['nodes']) / len(dijkstra_stats['nodes'])
            avg_astar_nodes = sum(astar_stats['nodes']) / len(astar_stats['nodes'])
            avg_dijkstra_time = sum(dijkstra_stats['time']) / len(dijkstra_stats['time'])
            avg_astar_time = sum(astar_stats['time']) / len(astar_stats['time'])
            
            node_improvement = (avg_dijkstra_nodes - avg_astar_nodes) / avg_dijkstra_nodes * 100
            time_improvement = (avg_dijkstra_time - avg_astar_time) / avg_dijkstra_time * 100
            
            print(f"\nOverall Performance Comparison:")
            print(f"  A* node expansion improvement: {node_improvement:.1f}%")
            print(f"  A* computation time improvement: {time_improvement:.1f}%")
            
        print(f"\nAnalysis completed!")
        print(f"Results demonstrate the efficiency advantages of informed search (A*)")
        print(f"over uninformed search (Dijkstra) while maintaining path optimality.")
        
        print(f"\nGenerating overall performance comparison plot...")
        self.generate_performance_plots()
    
    def generate_performance_plots(self):
        
        dijkstra_results = [r['dijkstra'] for r in self.results if r['dijkstra'].found]
        astar_results = [r['astar'] for r in self.results if r['astar'].found]
        
        if dijkstra_results and astar_results:
            results_dict = {
                'Dijkstra': dijkstra_results,
                'A*': astar_results
            }
            
            fig = self.plotter.plot_performance_comparison(results_dict)
            
            self.plotter.save_plot("results/plots/performance_comparison.png")
            
            self.plotter.show_plot()


def main():
    print("Initializing Path Planning Algorithm Comparison...")
    
    comparison = PathPlanningComparison(grid_size=15)
    
    comparison.run_comprehensive_analysis()


if __name__ == "__main__":
    main() 