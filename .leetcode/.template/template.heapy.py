from ..imports import *


class HeapNode:
    def __init__(self):
        self.weight = 5002
        self.pos = -1

        pass


class DijkstraNode(HeapNode):
    def __init__(self, word):
        super(DijkstraNode, self).__init__()
        self.word = word
        self.adjacency: List[DijkstraNode] = []
        self.state = 0
        pass


def heapify(x: List[HeapNode]):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    for i in reversed(range((n + 1) // 2)):
        _siftup(x, i)


def heappop(heap: List[HeapNode]):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()  # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        heap[0].pos = 0
        _siftup(heap, 0)
        return returnitem
    return lastelt


def _siftdown(heap: List[HeapNode], pos: int):
    ''' to root '''
    newitem = heap[pos]

    while pos > 0:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem.weight < parent.weight:
            heap[pos] = parent
            heap[pos].pos = pos
            pos = parentpos
            continue
        break
    heap[pos] = newitem
    heap[pos].pos = pos


def _siftup(heap: List[HeapNode], pos: int):
    ''' to left '''
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2 * pos + 1  # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos].weight < heap[
                rightpos].weight:
            childpos = rightpos

        if newitem.weight < heap[childpos].weight:
            break
        else:
            # Move the smaller child up.
            heap[pos] = heap[childpos]
            heap[pos].pos = pos
        pos = childpos
        childpos = 2 * pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    heap[pos].pos = pos
