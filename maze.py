############################### 72 chars ###############################


class Maze:
    """Encapsulates a Maze game and its methods.
    
    Arguments
    ---------
    - filename: str
      The path name of the maze data file.

    Attributes
    ----------
    - filename: str
      The path name of the maze data file from which maze data was
      imported.
    - start: coord
      The starting coordinate of the maze.
    - end: coord
      The ending coordinate of the maze.
    - x_size: int
      The width of the maze.
    - y_size: int
      The height of the maze.

    Methods
    -------
    - import_from(filename)
    - 
    """

    def __init__(self, filename: str) -> None:
        self.import_from(filename)

        first_row_data = self._data[0]
        index_of_start = first_row_data.index('0')
        start_coord_tuple = (0, index_of_start)
        self.start = start_coord_tuple

        last_row_data = self._data[-1]
        index_of_end = last_row_data.index('0')
        y_size = len(self.maze())
        end_coord_tuple = (y_size - 1, index_of_end)
        self.end = end_coord_tuple
        self.y_size = len(self.maze())
        self.x_size = len(self.maze()[0])

    def __repr__(self) -> str:
        return f'Maze({self.filename})'

    def import_from(self, filename) -> None:
        """Import maze data from a file into the instance.

        Arguments
        ---------
        - filename: str

        Return: None
        """
        with open(filename, 'r') as f:
            maze = f.readlines()
        for r in range(len(maze)):
            maze[r] = maze[r].strip()
        self._data = maze
        self.filename = filename

    def maze(self) -> "list[str]":
        """
        Get maze data.

        Arguments
        ---------
        None

        Return: ['1101...', ...]
        """
        return self._data

    def ispath(self, y, x) -> bool:
        """Returns True if the coordinate is a valid path.

        Arguments
        ---------
        - y: int
          The y-coordinate.
        -x: int
          The x-coordinate.

        Returns: True if the coordinate is a valid path,
        otherwise False.
        """
        return self._data[y][x] == '0'

    def around(self, here) -> "list[str]":
        """
        Determine possible path coordinates around here.

        Arguments
        ---------
        - here: (int, int)
          The target coordinate, as a 2-integer tuple.

        Return: [(y, x), ...]
        """
        _y, _x = here
        paths = list()
        for y, x in [
            (_y - 1, _x),
            (_y, _x - 1),
            (_y, _x + 1),
            (_y + 1, _x),
        ]:
            if (0 <= x < self.x_size and 0 <= y < self.y_size
                    and self.ispath(y, x)):
                paths.append((y, x))
        return paths

    def display(self, here=None, options=None, visited=None) -> None:
        """Print the maze."""
        char = {
            'wall': '█',
            'space': ' ',
            'here': 'H',
            'option': '?',
            'visited': '.',
        }

        for y, row in enumerate(self.maze()):
            for x, cell in enumerate(row):
                if cell == '1':
                    print(char['wall'], end='')
                elif here and (y, x) == here:
                    print(char['here'], end='')
                # elif options and (y, x) in options: # For Circular Queues
                elif options and options.contains((y, x)): # for Queues and Stacks
                    print(char['option'], end='')
                elif visited and (y, x) in visited:
                    print(char['visited'], end='')
                elif cell == '0':
                    print(char['space'], end='')
            print()  # linebreak
