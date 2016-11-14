class DNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.anchor = DNode(-1, -1)
        self.anchor.next = self.anchor
        self.anchor.prev = self.anchor
        self.lookup = dict()

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.lookup:
            return -1
        else:
            prevNode = self.lookup[key].prev
            nextNode = self.lookup[key].next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            prevIn = self.anchor.prev
            prevIn.next = self.lookup[key]
            self.anchor.prev = self.lookup[key]
            self.lookup[key].next = self.anchor
            self.lookup[key].prev = prevIn
            return self.lookup[key].value

    def checkDel(self):
        if self.cap < 0:
            toDel = self.anchor.next
            self.anchor.next = toDel.next
            toDel.next.prev = self.anchor
            toDel.next = None
            toDel.prev = None
            self.cap += 1
            self.lookup.pop(toDel.key, None)

    def set(self, key, value=1):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.lookup:
            lastNode = self.anchor.prev
            curNode = DNode(key, value)
            lastNode.next = curNode
            curNode.prev = lastNode
            curNode.next = self.anchor
            self.anchor.prev = curNode
            self.lookup[key] = curNode
            self.cap -= 1
            self.checkDel()
        else:
            self.lookup[key].value = value
            self.get(key)
"""
lru = LRUCache(1)
l = [0, 2, 1, 1, 2]
for i in l:
    lru.set(i)
print(lru.get(2))
"""

lru2 = LRUCache(2)
l = [0,2,1,0,1,1,0,2,3,0,4,1,1,1,1,2]
for i in l:
    lru2.set(i)
print(lru2.get(2))

