"""CPE202
John Wright
Lab 4
"""
class Node:
    """ A node of a list
    Attributes:
        val (int): the payload
        next (Node): the next item in the list
        prev (Node): the previous item in the list
    """
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        pass

    def __eq__(self, other):
        if self.val == other.val and self.next == other.next  and self.prev == other.prev:
            return True
        return False

class OrderedList:
    """an ordered list
    Attributes:
        head (Node): a ponter to the head of the list
        tail (Node): a pointer to the tail of the list
        num_items (int): the number of items stored in the list
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_items = 0

    def __eq__(self, other):
        if self.head == other.head:
            return True
        return False

    def __repr__(self):
        pass

    def add(self, item):
        """adds a specified value as an item in the list while maintaining ascending order.
        Args:
            item (int): a value to be added as an item in the list
        """
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
            self.num_items += 1

        elif item < self.head.val:
            temp = self.head
            self.head = Node(item, temp, temp.prev)
            self.tail = self.head.next
            self.num_items += 1
        else:
            current = self.head
            while current.next is not None and current.next.val < item:
                current = current.next
            node = Node(item, current.next, current)
            current.next = node
            if current.next.next is not None:
                self.tail = current.next.next
            else:
                self.tail = current.next
            self.num_items += 1

    def remove(self, item):
        """removes the first occurrence of a specified value in the list while
        maintaining ascending order.
        Args:
            item (int): a value to be removed
        Returns:
            int: the position where the item removed
        Raises:
            ValueError: when the item is not found in the list
        """
        pos = 0
        if self.head is None:
            raise ValueError
        if self.head.val == item:
            self.head = self.head.next
            return self.index(item)
        current = self.head
        while current.next is not None and current.next.val != item:
            current = current.next
            pos += 1
        if current.next is None:
            raise ValueError
        if current.next.val == item:
            current.next = current.next.next
            pos += 1
            return pos

    def search_forward(self, item):
        """searches a specified item in the list starting from the head.
        Args:
            item (int): the value to be searched in the list
        Returns:
            bool: True if found, False otherwise.
        """
        if self.head.val == item:
            return True
        current = self.head
        while current.next is not None and current.next.val != item:
            current = current.next
        if current.next is None:
            return False
        if current.next.val == item:
            return True

    def search_backward(self, item):
        """searches a specified item in the list backward starting from the tail.
        Args:
            item (int): the value to be searched in the list
        Returns:
            bool: True if found, False otherwise.
        """
        if self.tail is None:
            return False
        current = self.tail
        while current.prev is not None and current.val != item:
            current = current.prev
        if current.prev is None:
            return False
        if current.val == item:
            return True

    def is_empty(self):
        """checks if the list is empty.
        Returns:
            bool: True if it is empty, False otherwise.
        """
        if self.num_items == 0:
            return True
        return False

    def size(self):
        """gets the number of items stored in the list.
        Returns:
            int: the number of items in the list.
        """
        return self.num_items

    def index(self, item):
        """gets the position of the first occurrence of a specified item in the list.
        Args:
            item (int): the value to be found
        Returns:
            int: the position in the list
        Raises:
            LookupError: if the value is not found in the list
        """
        pos = 0
        if self.head.val == item:
            return pos
        if self.head.next.val == item:
            pos += 1
            return pos
        current = self.head
        while current.next is not None and current.next.val != item:
            current = current.next
            pos += 1
        if current.next is None:
            raise LookupError
        if current.next.val == item:
            pos += 1
            return pos


    def pop(self, pos=None):
        """removes the item at a specified position and returns its value.
        The last item in the list is removed if the argument is not passed.

        Args:
            pos (int): the position of the item to be removed. The default value is None
        Returns:
            int: the value of the item that is removed
        Raises:
            IndexError: if the position is out of bound
        """
        temp = None
        idx = 0
        current = None
        if pos is None:
            pos = self.num_items - 1
        if pos >= self.num_items:
            raise IndexError
        if pos > self.num_items / 2:
            current = self.tail
            idx = self.num_items - 1
            while current.prev is not None and idx > pos + 1:
                current = current.prev
                idx -= 1
            temp = current.prev
            current.prev = current
            return temp
        if pos <= self.num_items / 2:
            current = self.head
            while current.next is not None and idx < pos - 1:
                current = current.next
            temp = current.next
            current.next = None
            return temp