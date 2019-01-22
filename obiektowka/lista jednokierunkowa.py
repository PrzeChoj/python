class LinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, data, old):
            self.data = data
            self.old = old

    def push_front(self, data):
        self.head = LinkedList.Node(data, self.head)

    def pop_front(self):
        assert self.head
        data = self.head.data
        self.head = self.head.old
        return data

    def push_back(self, data):
        if self.head is None:
            self.push_front(data)
            return

        cur = self.head
        while cur.old is not None:
            cur = cur.old

        cur.old = LinkedList.Node(data, None)

l = LinkedList()
l.push_back(1)
l.push_back(2)
print(l.pop_front())
print(l.pop_front())



