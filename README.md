> [!WARNING]  
> In order to test this, I would recommend not testing the 2nd option with 10 digits. With the total combinations of 10! = 3,628,800 in the worst case scenario, the performance is not very great.

# Assumptions:

In this assignment, I'm going to assume the following:

- User can choose between auto generated values or manually input those values into the system.
- For manually input, the values are assume to be a list of continuous values from 1-10 separated by space, just unordered. Otherwise, it will keep prompting user to input correctly.
- For auto generated, the values is going to be an unordered list of continuous values from 1 to the value that the user specifies
- The cost of flipping one pancake is going to be 1.
- The priority queue is not provided.
- The priority queue is a wrap around on heapq package.
- The priority queue is implemented in this assignment for ease of use and better representation of the algorithm with simpler functionality.
- We can returns a reversed linked list of the solution.
- The direction of the ordering doesn't matter as long as the heuristic function is 0.

To run the program:

```
python3 main.py
```

# Notes

1. Define the problem as a searching problem.

This is a search problem because it satisfies the following:

- We know the **initial state** of the problem since it was provided by the user input.
- The possible action where we insert the spatula at any given location and flip the order of the top.
- We also have the successor function where we can generate the list of next states through flipping each level.
- Goal test is whether all the elements in the list are in ascending ordered.
- A path cost function will returns a value that is the number of flip has been done on that approach

2. Define a possible cost function (backward cost).

The possible cost function is going to be the number of pancake needs to be flipped. Assuming that each pancake cost 1 cost unit to flip.

3. Define a possible heuristic function (forward cost).

The heuristic function is going to be the h-gap function that was listed in "Landmark Heuristics for the Pancake Problem".
It will determine the total number of elements that has gap greater than 1.

4. Implement an A\* algorithm in Python.

5. Could the Uniform-Cost-Search algorithm be used? If so, provide also an implementation of the same Pancake Problem with UCS.

Yes, it could. Just that the solution may not be as optimal as fast and may be incomplete with bigger input.

