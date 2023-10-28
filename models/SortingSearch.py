from .Node import Node
from .NodePriorityQueue import NodePriorityQueue


class SortingSearch:
    """
    This class represent the A* search
    """

    def __init__(self, initial_state):
        self.frontier = NodePriorityQueue([Node(initial_state, 0, None, 0)])
        self.visited = []
        self.solution = None

    def find_solution(self):
        """
        Find the solution for the given search space
        """
        while not self.frontier.empty():
            # Choose node with min cost
            curr_node = self.frontier.poll()
            self.visited.append(curr_node.state)

            # Goal Test
            if curr_node.is_goal:
                print("Goal state found!")
                self.solution = curr_node
                self.__unify_direction()
                break

            self.__add_children_to_frontier(curr_node)

    def has_solution(self) -> bool:
        """
        Determine whether a solution was found
        """
        return self.solution is not None

    def print_solution(self):
        """
        Print the found solution to the consol
        """
        steps = []

        curr_node = self.solution
        while curr_node is not None:
            steps.insert(0, curr_node)
            curr_node = curr_node.parent

        for step_num, step in enumerate(steps[1:]):
            print("\n\nStep: " + str(step_num + 1))
            print(
                "Flipping! Insert Spatula at ["
                + str(step.flip_at)
                + "] and flip all with index before it"
            )
            print("State post flipping: " + str(step.state[: len(step.state)]))
            print("Total Cost: " + str(step.total_cost))

    def __unify_direction(self):
        first = self.solution.state[0]
        second = self.solution.state[1]
        if second - first == 1:
            print(
                "The solution direction is in ascending order detected! Add one more step to reverse the order."
            )
            reverse_order_node = Node(
                self.solution.state[::-1],
                len(self.solution.state) + self.solution.backward_cost,
                self.solution,
                len(self.solution.state) + 1,
            )
            self.solution = reverse_order_node

    def __add_children_to_frontier(self, curr_node: Node):
        for level in range(2, len(curr_node.state) + 1):
            next_state = curr_node.flip(level)
            child = Node(next_state, level + curr_node.backward_cost, curr_node, level)

            child_index = self.frontier.index(child)

            # If child is not visited, add to frontier immediately
            if next_state in self.visited:
                continue

            if next_state not in self.visited and child_index == -1:
                self.frontier.put(child)
                continue

            # Replace if is in frontier and has lower cost
            if child_index > -1:
                element = self.frontier.get(child_index)

                if element.total_cost < child.total_cost:
                    self.frontier.replace(child_index, child)
