############################### 72 chars ###############################


class CircularQueue: # make List as the superclass??
    """
    Circular Queue implemented as Array.

    Methods
    -------
    - enqueue(item)
      Adds item at the end of the queue.
    
    - dequeue()
      Returns the first item in the queue.
    """

    def __init__(self, size: int):
        """
        Rules:
        Empty -> head = -1
        Full -> tail = -1
        """
        # Delete the line below and write your code here
        # super().__init__([None] * size) maybe?
        self.cq = [None] * size
        self.head = -1
        self.tail = 0
        self.size = size

    def __repr__(self) -> str:
        return f"CircularQueue({self.size})"

    def enqueue(self, data) -> None:
        """
        Add item at the end of the queue.

        Arguments
        ---------
        - item
          The item to be added.

        Return: None
        """
        # Delete the line below and write your code here
        if self.tail == -1:
            raise Exception("Queue is full")
        self.cq[self.tail] = data
        self.tail = (self.tail + 1) % self.size
        if self.head == -1:
            pos = 0
            for i in range(self.size):
                if not (self.cq[i] is None):
                    break
                pos += 1
            self.head = pos
        if self.head == self.tail:
            self.tail = -1
        return


    def dequeue(self) -> "item":
        """
        Return the item at the head of the queue.

        Arguments
        ---------
        None

        Return: item
        """
        # Delete the line below and write your code here
        if self.head == -1:
            raise Exception("Queue is empty")
        data = self.cq[self.head]
        self.cq[self.head] = None
        self.head = (self.head + 1) % self.size
        if self.tail == -1:
            pos = 0
            for i in range(self.size):
                if not (self.cq[i] is None):
                    break
                pos += 1
            self.tail = pos
        if self.head == self.tail:
            self.head = -1
        return data
    
    def contains(self, item) -> bool:
        return item in self.cq