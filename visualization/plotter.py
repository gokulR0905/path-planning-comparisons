import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from typing import List, Tuple
from algorithms.base import PathResult
from environment.grid import Grid


class PathPlotter:
    def __init__(self, figsize=(12, 8)):
        self.figsize = figsize
        plt.style.use('default') 
    
    def plot_grid_with_path(self, grid: Grid, path: List[Tuple[int, int]], 
                           start: Tuple[int, int], goal: Tuple[int, int],
                           title: str = "Path Planning Result"):
      
        fig, ax = plt.subplots(figsize=self.figsize)
    
        grid_array = np.zeros((grid.height, grid.width))
      
        for x, y in grid.obstacles:
            grid_array[y, x] = 1
       
        ax.imshow(grid_array, cmap='binary', origin='lower')
        
    
        if path:
            path_x = [pos[0] for pos in path]
            path_y = [pos[1] for pos in path]
            ax.plot(path_x, path_y, 'b-', linewidth=3, alpha=0.7, label='Path')
            ax.plot(path_x, path_y, 'bo', markersize=4, alpha=0.7)
        
        ax.plot(start[0], start[1], 'go', markersize=12, label='Start')
        ax.plot(goal[0], goal[1], 'ro', markersize=12, label='Goal')
  
        ax.set_xlim(-0.5, grid.width - 0.5)
        ax.set_ylim(-0.5, grid.height - 0.5)
        ax.set_xlabel('X Coordinate')
        ax.set_ylabel('Y Coordinate')
        ax.set_title(title)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
    
        ax.set_xticks(range(grid.width))
        ax.set_yticks(range(grid.height))
        
        plt.tight_layout()
        return fig, ax
    
    def plot_comparison(self, grid: Grid, dijkstra_result: PathResult, 
                       astar_result: PathResult, start: Tuple[int, int], 
                       goal: Tuple[int, int]):
    
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
       
        self._plot_single_result(ax1, grid, dijkstra_result, start, goal, "Dijkstra")
        
        self._plot_single_result(ax2, grid, astar_result, start, goal, "A*")
    
        if dijkstra_result.found and astar_result.found:
            node_improvement = ((dijkstra_result.nodes_expanded - astar_result.nodes_expanded) 
                              / dijkstra_result.nodes_expanded * 100)
            time_improvement = ((dijkstra_result.computation_time - astar_result.computation_time) 
                              / dijkstra_result.computation_time * 100)
            
            comparison_text = (f"A* Improvements:\n"
                             f"Nodes: {node_improvement:.1f}%\n"
                             f"Time: {time_improvement:.1f}%")
            
            fig.suptitle(f"Algorithm Comparison\n{comparison_text}", fontsize=14)
        
        plt.tight_layout()
        plt.subplots_adjust(top=0.85)
        return fig
    
    def _plot_single_result(self, ax, grid: Grid, result: PathResult, 
                           start: Tuple[int, int], goal: Tuple[int, int], 
                           algorithm_name: str):
        
        grid_array = np.zeros((grid.height, grid.width))
        
        for x, y in grid.obstacles:
            grid_array[y, x] = 1
        
        ax.imshow(grid_array, cmap='binary', origin='lower')
       
        if result.found and result.path:
            path_x = [pos[0] for pos in result.path]
            path_y = [pos[1] for pos in result.path]
            ax.plot(path_x, path_y, 'b-', linewidth=3, alpha=0.7, label='Path')
            ax.plot(path_x, path_y, 'bo', markersize=3, alpha=0.7)
        
        ax.plot(start[0], start[1], 'go', markersize=10, label='Start')
        ax.plot(goal[0], goal[1], 'ro', markersize=10, label='Goal')
        
        ax.set_xlim(-0.5, grid.width - 0.5)
        ax.set_ylim(-0.5, grid.height - 0.5)
        ax.set_xlabel('X Coordinate')
        ax.set_ylabel('Y Coordinate')
       
        if result.found:
            title = (f"{algorithm_name}\n"
                    f"Nodes: {result.nodes_expanded}, "
                    f"Time: {result.computation_time:.4f}s\n"
                    f"Path Length: {result.path_length:.2f}")
        else:
            title = f"{algorithm_name}\nNo path found"
        
        ax.set_title(title, fontsize=10)
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        
        # Set integer ticks
        ax.set_xticks(range(0, grid.width, max(1, grid.width//10)))
        ax.set_yticks(range(0, grid.height, max(1, grid.height//10)))
    
    def plot_performance_comparison(self, results_dict):
        algorithms = list(results_dict.keys())
        if len(algorithms) < 2:
            print("Need at least 2 algorithms for comparison")
            return
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        metrics_data = {}
        for algo_name, results in results_dict.items():
            successful_results = [r for r in results if r.found]
            if successful_results:
                metrics_data[algo_name] = {
                    'nodes_expanded': [r.nodes_expanded for r in successful_results],
                    'computation_time': [r.computation_time for r in successful_results],
                    'memory_usage': [r.memory_usage for r in successful_results],
                    'path_length': [r.path_length for r in successful_results]
                }
        
        if not metrics_data:
            print("No successful results to plot")
            return
        
        metrics = ['nodes_expanded', 'computation_time', 'memory_usage', 'path_length']
        titles = ['Nodes Expanded', 'Computation Time (s)', 'Memory Usage (MB)', 'Path Length']
        
        for i, (metric, title) in enumerate(zip(metrics, titles)):
            ax = axes[i//2, i%2]
            
            data_to_plot = []
            labels = []
            
            for algo_name, data in metrics_data.items():
                if metric in data:
                    data_to_plot.append(data[metric])
                    labels.append(algo_name)
            
            if data_to_plot:
                ax.boxplot(data_to_plot, labels=labels)
                ax.set_title(title)
                ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.suptitle('Performance Comparison', fontsize=16)
        plt.subplots_adjust(top=0.93)
        return fig
    
    def save_plot(self, filename: str, dpi: int = 300):
        plt.savefig(filename, dpi=dpi, bbox_inches='tight')
        print(f"Plot saved to {filename}")
    
    def show_plot(self):
        """Display the current plot."""
        plt.show()
    
    def close_all(self):
        """Close all open plots."""
        plt.close('all') 