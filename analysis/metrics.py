import time
import psutil
import os
from typing import Dict, Any, List
from dataclasses import dataclass


@dataclass
class RuntimeMetrics:
    start_time: float
    end_time: float
    execution_time: float
    memory_start: float
    memory_end: float
    memory_delta: float
    cpu_percent: float


class MetricsCollector:
    
    def __init__(self):
        self.process = psutil.Process(os.getpid())
        self.active_measurements: Dict[str, RuntimeMetrics] = {}
    
    def start_measurement(self, measurement_id: str):
        start_time = time.time()
        memory_start = self.process.memory_info().rss / 1024 / 1024
        cpu_start = self.process.cpu_percent()
        
        self.active_measurements[measurement_id] = RuntimeMetrics(
            start_time=start_time,
            end_time=0.0,
            execution_time=0.0,
            memory_start=memory_start,
            memory_end=0.0,
            memory_delta=0.0,
            cpu_percent=cpu_start
        )
    
    def end_measurement(self, measurement_id: str) -> RuntimeMetrics:
        if measurement_id not in self.active_measurements:
            raise ValueError(f"No active measurement found for ID: {measurement_id}")
        
        metrics = self.active_measurements[measurement_id]
        metrics.end_time = time.time()
        metrics.execution_time = metrics.end_time - metrics.start_time
        metrics.memory_end = self.process.memory_info().rss / 1024 / 1024
        metrics.memory_delta = metrics.memory_end - metrics.memory_start
        metrics.cpu_percent = self.process.cpu_percent()
        
        del self.active_measurements[measurement_id]
        return metrics 