# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#
# https://leetcode.com/problems/construct-quad-tree/description/
#
# algorithms
# Medium (63.46%)
# Likes:    373
# Dislikes: 542
# Total Accepted:    31.9K
# Total Submissions: 50.2K
# Testcase Example:  '[[0,1],[1,0]]'
#
# Given a n * n matrix grid of 0's and 1's only. We want to represent the grid
# with a Quad-Tree.
#
# Return the root of the Quad-Tree representing the grid.
#
# Notice that you can assign the value of a node to True or False when isLeaf
# is False, and both are accepted in the answer.
#
# A Quad-Tree is a tree data structure in which each internal node has exactly
# four children. Besides, each node has two attributes:
#
#
# val: True if the node represents a grid of 1's or False if the node
# represents a grid of 0's.
# isLeaf: True if the node is leaf node on the tree or False if the node has
# the four children.
#
#
#
# class Node {
# ⁠   public boolean val;
# public boolean isLeaf;
# public Node topLeft;
# public Node topRight;
# public Node bottomLeft;
# public Node bottomRight;
# }
#
# We can construct a Quad-Tree from a two-dimensional area using the following
# steps:
#
#
# If the current grid has the same value (i.e all 1's or all 0's) set isLeaf
# True and set val to the value of the grid and set the four children to Null
# and stop.
# If the current grid has different values, set isLeaf to False and set val to
# any value and divide the current grid into four sub-grids as shown in the
# photo.
# Recurse for each of the children with the proper sub-grid.
#
#
# If you want to know more about the Quad-Tree, you can refer to the wiki.
#
# Quad-Tree format:
#
# The output represents the serialized format of a Quad-Tree using level order
# traversal, where null signifies a path terminator where no node exists
# below.
#
# It is very similar to the serialization of the binary tree. The only
# difference is that the node is represented as a list [isLeaf, val].
#
# If the value of isLeaf or val is True we represent it as 1 in the list
# [isLeaf, val] and if the value of isLeaf or val is False we represent it as
# 0.
#
#
# Example 1:
#
#
# Input: grid = [[0,1],[1,0]]
# Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
# Explanation: The explanation of this example is shown below:
# Notice that 0 represnts False and 1 represents True in the photo representing
# the Quad-Tree.
#
#
#
# Example 2:
#
#
#
#
# Input: grid =
# [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
# Output:
# [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
# Explanation: All values in the grid are not the same. We divide the grid into
# four sub-grids.
# The topLeft, bottomLeft and bottomRight each has the same value.
# The topRight have different values so we divide it into 4 sub-grids where
# each has the same value.
# Explanation is shown in the photo below:
#
#
#
# Example 3:
#
#
# Input: grid = [[1,1],[1,1]]
# Output: [[1,1]]
#
#
# Example 4:
#
#
# Input: grid = [[0]]
# Output: [[1,0]]
#
#
# Example 5:
#
#
# Input: grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
# Output: [[0,1],[1,1],[1,0],[1,0],[1,1]]
#
#
#
# Constraints:
#
#
# n == grid.length == grid[i].length
# n == 2^x where 0 <= x <= 6
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 四叉树。
# 直接动态规划。
#
# @lc idea=end

# @lc group=


# @lc rank=
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft,
                 bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def __str__(self):
        s = [[1 if self.isLeaf else 0, 1 if self.val else 0]]
        import queue
        q = queue.Queue()
        q.put(self)
        while not q.empty():
            node = q.get()

            if node.isLeaf:

                s.append(None)
                s.append(None)
                s.append(None)
                s.append(None)
            else:
                s.append([
                    1 if node.topLeft.isLeaf else 0,
                    1 if node.topLeft.val else 0
                ])
                s.append([
                    1 if node.topRight.isLeaf else 0,
                    1 if node.topRight.val else 0
                ])
                s.append([
                    1 if node.bottomLeft.isLeaf else 0,
                    1 if node.bottomLeft.val else 0
                ])
                s.append([
                    1 if node.bottomRight.isLeaf else 0,
                    1 if node.bottomRight.val else 0
                ])
                q.put(node.topLeft)
                q.put(node.topRight)
                q.put(node.bottomLeft)
                q.put(node.bottomRight)

        while len(s) > 0 and s[-1] == None:
            s.pop()

        return str(s)

    def __repr__(self):
        return self.__str__()


# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
    
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        rows = len(grid)

        buffer = [[
            Node(grid[i][j] == 1, True, None, None, None, None)
            for j in range(rows)
        ] for i in range(rows)]
        while rows != 1:
            rows //= 2
            bufferOld = buffer
            buffer = [[
                Node(False, False, bufferOld[i * 2][j * 2],
                     bufferOld[i * 2][j * 2 + 1], bufferOld[i * 2 + 1][j * 2],
                     bufferOld[i * 2 + 1][j * 2 + 1]) for j in range(rows)
            ] for i in range(rows)]

            for i in range(rows):
                for j in range(rows):
                    node = buffer[i][j]
                    node.isLeaf = node.bottomRight.isLeaf\
                     and node.bottomLeft.isLeaf \
                     and node.topRight.isLeaf \
                     and node.topLeft.isLeaf \
                     and node.topRight.val == node.topLeft.val \
                     and node.topRight.val == node.bottomLeft.val \
                     and node.topRight.val == node.bottomRight.val
                    if node.isLeaf:
                        node.val = node.topLeft.val
                        node.bottomRight = None
                        node.bottomLeft = None
                        node.topRight = None
                        node.topLeft = None
        node = buffer[0][0]
        return node


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[0,1],[1,0]]')
    print('Exception :')
    print('[[0,1],[1,0],[1,1],[1,1],[1,0]]')
    print('Output :')
    print(str(Solution().construct([[0, 1], [1, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'grid =[[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]'
    )
    print('Exception :')
    print(
        '[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]'
    )
    print('Output :')
    print(
        str(Solution().construct([[1, 1, 1, 1, 0, 0, 0, 0],
                                  [1, 1, 1, 1, 0, 0, 0, 0],
                                  [1, 1, 1, 1, 1, 1, 1, 1],
                                  [1, 1, 1, 1, 1, 1, 1, 1],
                                  [1, 1, 1, 1, 0, 0, 0, 0],
                                  [1, 1, 1, 1, 0, 0, 0, 0],
                                  [1, 1, 1, 1, 0, 0, 0, 0],
                                  [1, 1, 1, 1, 0, 0, 0, 0]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('grid = [[1,1],[1,1]]')
    print('Exception :')
    print('[[1,1]]')
    print('Output :')
    print(str(Solution().construct([[1, 1], [1, 1]])))
    print()

    print('Example 4:')
    print('Input : ')
    print('grid = [[0]]')
    print('Exception :')
    print('[[1,0]]')
    print('Output :')
    print(str(Solution().construct([[0]])))
    print()

    print('Example 5:')
    print('Input : ')
    print('grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]')
    print('Exception :')
    print('[[0,1],[1,1],[1,0],[1,0],[1,1]]')
    print('Output :')
    print(
        str(Solution().construct([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1],
                                  [0, 0, 1, 1]])))
    print()

    pass
# @lc main=end