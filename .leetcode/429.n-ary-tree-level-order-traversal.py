# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Medium (67.87%)
# Likes:    1378
# Dislikes: 77
# Total Accepted:    141.1K
# Total Submissions: 207.8K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# Given an n-ary tree, return the level order traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).
#
#
# Example 1:
#
#
#
#
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]
#
#
# Example 2:
#
#
#
#
# Input: root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
#
#
#
# Constraints:
#
#
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一个n叉树，层次序列化。
# 直接遍历。
#
# @lc idea=end

# @lc group=


# @lc rank=
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        res = []
        ns = [root] if root else []
        while ns:
            nsn = []
            l = []
            res.append(l)
            for n in ns:
                l.append(n.val)
                for c in n.children:
                    nsn.append(c)
            ns = nsn
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,3,2,4,null,5,6]')
    print('Exception :')
    print('[[1],[3,2,4],[5,6]]')
    print('Output :')
    print(str(Solution().__init__(error, error)))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'root =[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]'
    )
    print('Exception :')
    print('[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]')
    print('Output :')
    print(str(Solution().__init__(error, error)))
    print()

    pass
# @lc main=end