
from Utility import Node
from Algorithm import Algorithm

class HILL_CLIMBING(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        
        # If no path found, return None
        return None