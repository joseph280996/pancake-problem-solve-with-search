from constants import ASTAR_ALGO


class Node:
    """
    This class represent a state node in the search tree
    Attributes:
        state           The state that the node instance represent
        backward_cost   The backward cost value of the current node (it is the number of pancakes that was flipped to reach this state)
        parent          The reference to the parent node so that we can trace back later
        flip_at         The level at which the pancake was flipped
    """

    type = ASTAR_ALGO
    """
    The type of the node to determine which cost to return
    """

    def __init__(self, state, backward_cost, parent, flip_level):
        self.state = state
        self.backward_cost = backward_cost
        self.parent = parent
        self.flip_at = flip_level
        self.__forward_cost = self.__heuristic_function()

    def __lt__(self, other) -> bool:
        """
        Comparison function for heap sorting.
        If 2 values have the same cost, we rank them by the order in which it was put into the frontier to make the order consistent with each sort
        """
        return self.total_cost < other.total_cost

    @property
    def is_goal(self) -> bool:
        """
        This function is the determination of the whether the current node is the goal
        """
        return self.__forward_cost == 0

    @property
    def total_cost(self) -> int:
        """
        Calculate the total cost using backward_cost and heuristic value
        """
        if Node.type == ASTAR_ALGO:
            return self.backward_cost + self.__forward_cost

        return self.backward_cost

    def flip(self, level) -> list:
        return self.state[:level][::-1] + self.state[level:]

    def __heuristic_function(self) -> int:
        hgap = 0
        for i in range(1, len(self.state)):
            if abs(self.state[i] - self.state[i - 1]) != 1:
                hgap += 1
        return hgap
