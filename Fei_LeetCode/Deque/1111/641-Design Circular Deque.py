class MyCircularDeque(object):
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.list, self.size = [], k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.list) < self.size:
            self.list.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.list) < self.size:
            self.list.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.list) > 0:
            self.list.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.list) > 0:
            self.list.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            temp = self.list.pop(0)
            self.insertFront(temp)
            return temp

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            temp = self.list.pop()
            self.insertLast(temp)
            return temp

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if len(self.list) == 0:
            return True

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if len(self.list) == self.size:
            return True

