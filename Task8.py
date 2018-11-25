class QueueNode:
    """ Node: Class for single node of LinkedQueue """

    def __init__(self, elem, nextnode):
        """ Initializes new node """
        self.item = elem
        self.next = nextnode
        

class QueueIterator:
    """ QueueIterator: Iterator for LinkedQueue """

    def __init__(self, node, count):
        """ Initializes new Iterator """
        self.current = node
        self.size = count
    def __next__(self):
        """ Returns next element of queue: next(iter) """
        if self.size == 0:
            raise StopIteration
        else:
            current = self.current.value
            self.current = self.current.next
            self.size -= 1
            return current



class LinkedQueue:
    """ LinkedQueue """

    def __init__(self):
        """ Initializes new queue """
        self.enter = None
        self.out = None
        self.size = 0
        self.items = []

    def push(self, elem):
        """ Pushes 'elem' to queue """
        if elem not in self.items:
            self.items.append(elem)
            return True
        return False

        
    def pop(self):
        """ Removes front of queue and returns it """
        if len(self.items) <= 0:
            return ("List Empty!")
        return self.items.pop()


    def front(self):
        """ Returns front of queue """
        return self.out.value


    def empty(self):
        """ Checks whether queue is empty """
        return self.front == None


    def __iter__(self):
        """ Returns Iterator for queue: iter(queue) """
        return QueueIterator(self.out, self.size)


    def __len__(self):
        """ Returns size of queue: len(queue) """
        return len(self.items)

    def clear(self):
        """ Makes queue empty """
        self.enter = None
        self.out = None
        self.size = 0

