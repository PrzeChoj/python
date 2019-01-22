class LinkedList:
    """ lista jednokierunkowa z dowiazaniami """

    class Node:
        def __init__(self, data, next):
            self.data = data
            self.next = next

    def __init__(self):
        """ konstruujemy pusta liste """
        self.head = None

    def push_front(self, data):

        self.head = LinkedList.Node(data, self.head)

    def pop_front(self):
        assert self.head  # nie jest None -> lista nie jest pusta
        data = self.head.data
        self.head = self.head.next
        return data

    def push_back(self, data):
        if self.head is None:
            self.push_front(data)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next

        # teraz cur.next is None,
        # chce wstawic el jako nowy cur.next (po cur)
        cur.next = LinkedList.Node(data, None)

    """
    def is_empty(self):
        return (self.head is None)
#         if self.head is None:
#             return True
#         else:
#             return False
    """

l = LinkedList()
l.push_back(1)
l.push_back(2)
print(l.pop_front())
print(l.pop_front())


"""
for i in range(5):
    l.push_front(i)

print(l.pop_front())

for i in range(5, 8):
    l.push_front(i)
while not l.is_empty():
    print(l.pop_front())
"""