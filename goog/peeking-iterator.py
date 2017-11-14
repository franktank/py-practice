class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.itr = iterator
        self.store = []

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.store:
            return self.store[0]
        else:
            self.store.append(self.itr.next())
            return self.store[0]

    def next(self):
        """
        :rtype: int
        """
        if self.store:
            return self.store.pop(0)
        if self.itr.hasNext():
            return self.itr.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.itr.hasNext() or self.store:
            return True
        return False
