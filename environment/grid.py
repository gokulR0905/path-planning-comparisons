"""
Grid-based environment for pathfinding algorithms.
"""

class Grid:
    """Simple 2D grid representation for pathfinding."""
    
    def __init__(self, width: int, height: int):
        """
        Initialize the grid.
        
        Args:
            width: Grid width
            height: Grid height
        """
        self.width = width
        self.height = height
        self.obstacles = set()  # Set of (x, y) obstacle positions
    
    def add_obstacle(self, x: int, y: int):
        """Add an obstacle at position (x, y)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.obstacles.add((x, y))
    
    def is_obstacle(self, x: int, y: int) -> bool:
        """Check if position (x, y) contains an obstacle."""
        return (x, y) in self.obstacles
    
    def is_valid_position(self, x: int, y: int) -> bool:
        """Check if position is within bounds and not an obstacle."""
        return (0 <= x < self.width and 
                0 <= y < self.height and 
                not self.is_obstacle(x, y))
    
    def get_neighbors(self, x: int, y: int):
        """Get valid neighboring positions for a given coordinate."""
        neighbours = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy
            
            if self.is_valid_position(new_x, new_y):
                neighbours.append(((new_x, new_y), 1.0))
        return neighbours   
            
    
    def __str__(self) -> str:
        """Simple string representation of the grid."""
        result = []
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if self.is_obstacle(x, y):
                    row += "█"  # Obstacle
                else:
                    row += "·"  # Free space
            result.append(row)
        return "\n".join(result) 