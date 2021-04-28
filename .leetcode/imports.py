from typing import *
from collections import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = [self.val]
        p = self.next
        while p:
            s.append(p.val)
            p = p.next
        return str(s)

    def __repr__(self):
        return self.__str__()


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        s = [self.val]
        import queue
        q = queue.Queue()
        q.put(self)
        while not q.empty():
            node = q.get()

            if node.left:
                q.put(node.left)
                s.append(node.left.val)
            else:
                s.append('null')
            if node.right:
                q.put(node.right)
                s.append(node.right.val)
            else:
                s.append('null')
        return str(s)

    def __repr__(self):
        return self.__str__()


def listToListNode(l: List[int]) -> ListNode:
    ''' List[int] to ListNode '''
    pseudo = ListNode()
    p = pseudo
    for i in l:
        p.next = ListNode(i)
        p = p.next
    return pseudo.next


def listToTreeNode(l: List[int]) -> TreeNode:
    ''' List[int] to TreeNode '''
    if len(l) == 0:
        return None
    buff = [None] * len(l)

    for i, n in enumerate(l):
        if n:
            buff[i] = TreeNode(val=n)

    for i, n in enumerate(buff[:(len(l) - 1) // 2]):
        if n:
            n.left = buff[i * 2 + 1]
            n.right = buff[i * 2 + 2]

    return buff[0]
