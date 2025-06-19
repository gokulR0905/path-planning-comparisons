import time
import statistics
from typing import List, Dict, Any
from algorithms.base import PathResult


class PerformanceAnalyzer:
    def __init__(self):
        self.results: List[PathResult] = []
    
    def add_result(self, result: PathResult):
        self.results.append(result)
    
    def clear_results(self):
        self.results.clear()
    
    def analyze_algorithm_performance(self, algorithm_name: str) -> Dict[str, Any]:
        #performance analysis for a specific algorithm
        algorithm_results = [r for r in self.results if r.algorithm_name == algorithm_name]
        
        if not algorithm_results:
            return {}
        
        successful_results = [r for r in algorithm_results if r.found]
        
        analysis = {
            'algorithm_name': algorithm_name,
            'total_runs': len(algorithm_results),
            'successful_runs': len(successful_results),
        }
        
        if successful_results:
            nodes_expanded = [r.nodes_expanded for r in successful_results]
            computation_times = [r.computation_time for r in successful_results]
            memory_usage = [r.memory_usage for r in successful_results]
            path_lengths = [r.path_length for r in successful_results]
            
            analysis.update({
                'nodes_expanded': {
                    'mean': statistics.mean(nodes_expanded),
                    'median': statistics.median(nodes_expanded),
                    'min': min(nodes_expanded),
                    'max': max(nodes_expanded),
                    'std_dev': statistics.stdev(nodes_expanded) if len(nodes_expanded) > 1 else 0
                },
                'computation_time': {
                    'mean': statistics.mean(computation_times),
                    'median': statistics.median(computation_times),
                    'min': min(computation_times),
                    'max': max(computation_times),
                    'std_dev': statistics.stdev(computation_times) if len(computation_times) > 1 else 0
                },
                'memory_usage': {
                    'mean': statistics.mean(memory_usage),
                    'median': statistics.median(memory_usage),
                    'min': min(memory_usage),
                    'max': max(memory_usage),
                    'std_dev': statistics.stdev(memory_usage) if len(memory_usage) > 1 else 0
                },
                'path_length': {
                    'mean': statistics.mean(path_lengths),
                    'median': statistics.median(path_lengths),
                    'min': min(path_lengths),
                    'max': max(path_lengths),
                    'std_dev': statistics.stdev(path_lengths) if len(path_lengths) > 1 else 0
                }
            })
        
        return analysis
    
    def compare_algorithms(self, algorithm1: str, algorithm2: str) -> Dict[str, Any]:
        analysis1 = self.analyze_algorithm_performance(algorithm1)
        analysis2 = self.analyze_algorithm_performance(algorithm2)
        
        if not analysis1 or not analysis2:
            return {}
        
        comparison = {
            'algorithm1': algorithm1,
            'algorithm2': algorithm2,
        }
        
        # Compare metrics if both have successful runs
        if 'nodes_expanded' in analysis1 and 'nodes_expanded' in analysis2:
            metrics = ['nodes_expanded', 'computation_time', 'memory_usage', 'path_length']
            
            for metric in metrics:
                mean1 = analysis1[metric]['mean']
                mean2 = analysis2[metric]['mean']
                
                improvement = (mean1 - mean2) / mean1 * 100 if mean1 != 0 else 0
                
                comparison[f'{metric}_improvement'] = {
                    'algorithm2_vs_algorithm1_percent': improvement,
                    'algorithm1_mean': mean1,
                    'algorithm2_mean': mean2
                }
        
        return comparison
    
    def generate_summary_report(self) -> str:
        if not self.results:
            return "No results to analyze."
        
        algorithms = list(set(r.algorithm_name for r in self.results))
        
        report = ["PATHFINDING ALGORITHM PERFORMANCE ANALYSIS"]
        report.append("=" * 50)
        report.append("")
        
        #Individual algorithm analysis
        for algorithm in algorithms:
            analysis = self.analyze_algorithm_performance(algorithm)
            if analysis:
                report.append(f"{algorithm} Performance:")
                report.append(f"  Successful Runs: {analysis['successful_runs']}/{analysis['total_runs']}")
                
                if 'nodes_expanded' in analysis:
                    report.append(f"  Nodes Expanded: {analysis['nodes_expanded']['mean']:.1f} ± {analysis['nodes_expanded']['std_dev']:.1f}")
                    report.append(f"  Computation Time: {analysis['computation_time']['mean']:.4f}s ± {analysis['computation_time']['std_dev']:.4f}s")
                    report.append(f"  Memory Usage: {analysis['memory_usage']['mean']:.2f}MB ± {analysis['memory_usage']['std_dev']:.2f}MB")
                    report.append(f"  Path Length: {analysis['path_length']['mean']:.2f} ± {analysis['path_length']['std_dev']:.2f}")
                
                report.append("")
        
        #Algorithm comparison
        if len(algorithms) == 2:
            comparison = self.compare_algorithms(algorithms[0], algorithms[1])
            if comparison:
                report.append("ALGORITHM COMPARISON:")
                report.append(f"{comparison['algorithm2']} vs {comparison['algorithm1']}:")
                
                for metric in ['nodes_expanded', 'computation_time', 'memory_usage']:
                    if f'{metric}_improvement' in comparison:
                        improvement = comparison[f'{metric}_improvement']['algorithm2_vs_algorithm1_percent']
                        report.append(f"  {metric.replace('_', ' ').title()} Improvement: {improvement:.1f}%")
                
                report.append("")
        
        return "\n".join(report)
    
    def get_efficiency_metrics(self, algorithm_name: str) -> Dict[str, float]:
        algorithm_results = [r for r in self.results if r.algorithm_name == algorithm_name and r.found]
        
        if not algorithm_results:
            return {}
        
        #Calculate efficiency ratios
        efficiency_metrics = {}
        
        for result in algorithm_results:
            path_length = result.path_length
            nodes_expanded = result.nodes_expanded
            
            if path_length > 0 and nodes_expanded > 0:
                path_efficiency = nodes_expanded / path_length
                time_efficiency = result.computation_time / path_length
                
                if 'path_efficiency' not in efficiency_metrics:
                    efficiency_metrics['path_efficiency'] = []
                    efficiency_metrics['time_efficiency'] = []
                
                efficiency_metrics['path_efficiency'].append(path_efficiency)
                efficiency_metrics['time_efficiency'].append(time_efficiency)
        
        if efficiency_metrics:
            return {
                'avg_path_efficiency': statistics.mean(efficiency_metrics['path_efficiency']),
                'avg_time_efficiency': statistics.mean(efficiency_metrics['time_efficiency']),
                'path_efficiency_std': statistics.stdev(efficiency_metrics['path_efficiency']) if len(efficiency_metrics['path_efficiency']) > 1 else 0,
                'time_efficiency_std': statistics.stdev(efficiency_metrics['time_efficiency']) if len(efficiency_metrics['time_efficiency']) > 1 else 0
            }
        
        return {} 