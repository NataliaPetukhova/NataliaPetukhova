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
            current = self.current.item
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


    def push(self, elem):
        """ Pushes 'elem' to queue """
        if not self.size:
            self.enter = QueueNode(elem, None)
            self.out = self.enter
            self.size = 1
        else:
            new_node = QueueNode(elem, None)
            self.enter.next = new_node
            self.enter = new_node
            self.size += 1


    def pop(self):
        """ Removes front of queue and returns it """
        if not self.size:
            return None
        else:
            out = self.out.item
            self.out = self.out.next
            self.size -= 1
            return out


    def front(self):
        """ Returns front of queue """
        if not self.size:
            return None
        else:
            return self.out.item


    def empty(self):
        """ Checks whether queue is empty """
        return not self.size


    def __iter__(self):
        """ Returns Iterator for queue: iter(queue) """
        return QueueIterator(self.out, self.size)


    def __len__(self):
        """ Returns size of queue: len(queue) """
        return self.size 


    def clear(self):
        """ Makes queue empty """
        self.enter = None
        self.out = None
        self.size = 0


def main():

    q = LinkedQueue()
    print(q.push(1))
    print(q.empty())
    for x in q:
        print(x)

main()
