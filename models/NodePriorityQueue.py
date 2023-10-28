import heapq
from .Node import Node


class NodePriorityQueue:
    """
    Implementation of the priority queue used for min cost sort
    """

    def __init__(self, initial_state: list[Node]):
        self.__queue = initial_state

    def get(self, idx) -> Node:
        """
        Get the element a the given index
        """
        return self.__queue[idx]

    def index(self, elmnt) -> int:
        """
        Get the index of the element in the current queue
        """
        for idx in range(len(self.__queue)):
            if self.__queue[idx].state == elmnt.state:
                return idx
        return -1

    def replace(self, index, elmnt):
        """
        Replace the value at a given index and reorder the ranking
        """
        self.__queue[index] = elmnt

    def empty(self) -> bool:
        """
        Check whether the current queue is empty
        """
        return len(self.__queue) == 0

    def poll(self) -> Node:
        """
        Returns and remove the highest priority element in the queue
        """
        return heapq.heappop(self.__queue)

    def put(self, new_val):
        """
        Add an element to the queue and re-order the queue
        """
        heapq.heappush(self.__queue, new_val)
