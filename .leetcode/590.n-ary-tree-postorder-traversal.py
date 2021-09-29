# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
#
# algorithms
# Easy (74.99%)
# Likes:    1257
# Dislikes: 76
# Total Accepted:    152.5K
# Total Submissions: 203.1K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# Given the root of an n-ary tree, return the postorder traversal of its nodes'
# values.
#
# Nary-Tree input serialization is represented in their level order traversal.
# Each group of children is separated by the null value (See examples)
#
#
# Example 1:
#
#
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [5,6,3,2,4,1]
#
#
# Example 2:
#
#
# Input: root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# 0 <= Node.val <= 10^4
# The height of the n-ary tree is less than or equal to 1000.
#
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 后序遍历n叉树。
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
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def recur(p: 'Node'):
            if not p:
                return

            for c in p.children:
                recur(c)
            res.append(p.val)

        recur(root)
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,3,2,4,null,5,6]')
    print('Exception :')
    print('[5,6,3,2,4,1]')
    print('Output :')
    print(str(Solution().__init__(error, error)))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'root =[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]'
    )
    print('Exception :')
    print('[2,6,14,11,7,3,12,8,4,13,9,10,5,1]')
    print('Output :')
    print(str(Solution().__init__(error, error)))
    print()

    pass
# @lc main=end