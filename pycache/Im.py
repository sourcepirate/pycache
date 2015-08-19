__author__ = 'plasmashadow'

#IM stands for In Memory

class IMNode(object):

    def __init__(self, item):
        '''
          A datastructure representing the fully linked stack
        :param item:
        :return:
        '''
        self.prev = None
        self.next = None
        self.item = item

class IMStack(object):

    '''
       The IMStack representing the Stack of
       hashed IMNodes
    '''

    def __init__(self):
        '''
          Initialy when a node has been initialized
          it does have another link with different
          memory locations.
          :return:
        '''

        self.prev = self
        self.next = self
        self.keys = {}

    def update(self, item):

        '''
         Since Memory cannot be directly updated we remove and
         re add the same item.
        :param item:
        :return:
        '''

        self.discard(item)
        self.add(item)

    def add(self, item):

        '''
        Add a given item on to the IMStack
        :param item:
        :return:
        '''

        node = IMNode(item)
        self.keys[item] = node
        node.next = self
        node.prev = self.prev
        node.prev.next = node
        self.prev = node

    def pop(self):

        '''
         Get the latest node from the stack
        :return:
        '''

        if self.next is self:
            return None
        return self.next.item

    def __iter__(self):
        '''
        Return an iterator to the ordered stock
        '''
        item = self
        while item.next != self:
            item = item.next
            yield item.item

    def tolist(self):
        '''
        Convert to list
        '''
        return [item for item in self]

    def __str__(self):

        '''
          String representation
        :return:
        '''

        s = []
        node = self.prev
        while node is not self:
            s.append(str(node.item))
            node = node.prev
        res = " <- ".join(s)
        s = []
        node = self.next
        while node is not self:
            s.append(str(node.item))
            node = node.next
        res += " / " + " -> ".join(s)
        return res

    def clear(self):

        '''
          Clear the entire stack
        :return:
        '''

        self.keys.clear()
        self.next = self
        self.prev = self

    def __len__(self):

        return len(self.keys)
