# Pancake sorting with A* and Uniform-Cost search algorithm

> [!WARNING]  
> In order to test this, I would recommend not testing the 2nd option with 10 digits. With the total combinations of 10! = 3,628,800 in the worst case scenario, the performance is not very great.

# Design and Assumptions:
- For manually input, the values are assume to be a list of continuous values from 1-10 separated by space, just unordered. Otherwise, it will keep prompting to input correctly.
- For auto generated, the values is going to be an unordered list of continuous values from 1 to the value that the user specifies.
- The cost of flipping one pancake is going to be 1.
- The direction of the ordering doesn't matter as long as the heuristic function is 0.

To run the program:

```
python3 main.py
```
