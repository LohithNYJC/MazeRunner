############################### 72 chars ###############################


class Node:
    """
    Represents a node in a linkedlist.

    Arguments
    ---------
    - data
      The data encapsulated in the node.

    Attributes
    ----------
    - next: Node | None
      The next node in the linkedlist, or None if the node is the tail.

    Methods
    -------
    - get() -> data
      Return the data stored in the node.
    """

    def __init__(self, data):
        # Replace the line below with your code
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self):
        """Return the data stored in the node.

        Arguments
        ---------
        None

        Return: data
        """
        return self.data


class LinkedList:
    """
    Represents a sequence of data items.

    Arguments
    ---------
    None

    Attributes
    ----------
    None

    Methods
    -------
    - length() -> int
    - get(index) -> item
    - insert(index, item) -> None
    - append(item) -> None
    - delete(index) -> None
    """

    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.

        Arguments
        ---------
        None

        Return: int
        """
        # Replace the line below with your code
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.next
        return count

    def get(self, n: int) -> "item":
        """Returns item at n-th node.

        Arguments
        ---------
        - n: int
          sequence number of item to be retrieved.

        Returns: item

        Raises: IndexError if n > length
        """
        # Replace the line below with your code
        if n > self.length():
            raise IndexError("Index out of range")
        current = self._head
        for i in range(n-1):
          current = current.next
        return current.data

    def insert(self, n: int, item) -> None:
        """Insert item into linkedlist at position n.
        insert at head -> n == 0
        append -> n == length

        Arguments
        ---------
        - n: int
          sequence number of item to be inserted.

        Returns: None

        Raises: IndexError if n > length
        """
        # Replace the line below with your code
        new_node = Node(item)
        if not self.length():
            self._head = new_node
            return
        if n > self.length():
            raise IndexError("Index out of range")
        if n == 1:
            new_node.next = self._head  
            self._head = new_node  
            return
        current = self._head
        for i in range(n):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def append(self, item) -> None:
        """Append item at the end of linkedlist.

        Arguments
        ---------
        - item
          The item to be appended.

        Returns: None
        """
        # Replace the line below with your code
        current = self._head
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
            return 
        while current is not None:
            if current.next is None:
                current.next = new_node
                return
            current = current.next

    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
        ---------
        - n: int
          sequence number of item to be retrieved.

        Returns: None

        Raises: IndexError if n > length
        """
        # Replace the line below with your code
        counter = 0 
        if n > self.length():
            raise IndexError("Index out of range")
        current = self._head
        if n == 1:
            self._head = current.next
            return
        previous = None     
        while counter != n:
          previous = current
          current = current.next
          counter += 1
        if current is not None:
          previous.next = current.next
       
    def contains(self, item) -> bool:
        """Checks whether an item is in the linkedlist and returns
        a boolean value to indicate the status of the search

        Arguments
        ---------
        - item
          The item to be searched for.

        Returns: True if item is found in the linkedlist,
        otherwise False
        """
        # Replace the line below with your code
        current = self._head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False


# d = LinkedList()
# d.append(10)
# print(d.length())
# d.append(20)
# d.append(30)
# d.append(40)
# print(d.length())
# print()
# print(d.get(2))
# print(d.contains(12))
# d.insert(1,25)
# print(d.get(1))
# d.insert(1,20)
# print(d.get(2))
# d.insert(1,15)
# print(d.get(3))
# d.insert(1,10)
# print(d.get(4))
# print(d.length())
# print(d.get(3))
# d.delete(3)
# 10 20 25 30 40