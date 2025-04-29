############################### 72 chars ###############################
"""This module solves a maze using breadth-first or depth-first search.

Depth-first search (DFS) is carried out with a stack, while breadth-
first search (BFS) is carried out with a queue.

Submodules:
- maze.py
  Maze class encapsulates maze data and provides methods for accessing
  and displaying it.

- datastruct.py
  Contains the LinkedList class which Stack and Queue inherit.

- adt.py
  Contains the Stack and Queue classes, which are used to keep track of
  unexplored paths.

- cq.py
  Contains the CircularQueue class, as an alternative to Queue.
"""

# Builtin imports
import time

# Local imports
from adt import Stack, Queue
from cq import CircularQueue
from maze import Maze


class OutOfOptionsError(Exception):
    pass


# Initialise options as a Stack or Queue (choose one)
# Used to store available path options for the next step.
# options = Stack() # works
# options = Queue() # works
options = CircularQueue(5) # does not work/ not implemented yet

# Stores a list of visited coords
visited = []

maze = Maze('maze.txt')

here = maze.start
counter = 0
while here != maze.end:
    print(f'== STEP {counter} ==')
    maze.display(
        here,
        options=options,
        visited=visited,
    )
    # Slow down program so that humans can follow
    time.sleep(0.5)

    # maze.around(here) returns a collection of coordinates around here
    for coord in maze.around(here):
        if coord not in visited:
            # options.insert(0, coord)
            # options.push(coord) # works for Stack
            options.enqueue(coord) # works for Queue

    # Store visited coord
    visited.append(here)

    # Pop the next here from options
    try:
        # here = options.pop() # works for Stack
        here = options.dequeue() # works for Queue
    except IndexError:
        raise OutOfOptionsError("No available paths")
    else:
        print(f'here: {here}')
        print(f'visited: {visited}')
    counter += 1
