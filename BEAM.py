
from Utility import Node
from Algorithm import Algorithm

class BEAM(Algorithm):
    def __init__(self, grid, beam_width=2):
        super().__init__(grid)
        self.beam_width = beam_width

    def run_algorithm(self, snake):
        # Use existing path if available
        if len(self.path) != 0:
            path = self.path.pop()
            if self.inside_body(snake, path):
                self.path = []
            else:
                return path

        # Reset search variables
        self.frontier = []
        self.explored_set = []
        self.path = []

        # Get initial and goal states
        initialstate, goalstate = self.get_initstate_and_goalstate(snake)
        
        # Add initial state to frontier
        self.frontier.append(initialstate)

        while len(self.frontier) > 0:
            # Sort frontier by heuristic distance to goal
            self.frontier.sort(key=lambda x: self.manhattan_distance(x, goalstate))
            self.frontier = self.frontier[:self.beam_width]  # Keep only the best beam_width states
            currentstate = self.frontier.pop(0)

            if currentstate.equal(goalstate):
                return self.get_path(currentstate)

            if currentstate not in self.explored_set:
                self.explored_set.append(currentstate)

                # Get and process neighbors
                neighbors = self.get_neighbors(currentstate)
                for neighbor in neighbors:
                    if not self.inside_body(snake, neighbor) and \
                       not self.outside_boundary(neighbor) and \
                       neighbor not in self.explored_set:
                        neighbor.parent = currentstate
                        self.frontier.append(neighbor)

        # If no path found, return None
        return None