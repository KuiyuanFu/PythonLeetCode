# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (70.21%)
# Likes:    1629
# Dislikes: 65
# Total Accepted:    181.8K
# Total Submissions: 258.6K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# Given a n-ary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
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
# Output: 3
#
#
# Example 2:
#
#
#
#
# Input: root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: 5
#
#
#
# Constraints:
#
#
# The total number of nodes is in the range [0, 10^4].
# The depth of the n-ary tree is less than or equal to 1000.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求一个树的深度。
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
    def maxDepth(self, root: 'Node') -> int:
        res = 0
        s = [root] if root else []
        while s:
            res += 1
            sn = []
            for p in s:
                for nn in p.children:
                    sn.append(nn)
            s = sn
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,3,2,4,null,5,6]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().__init__(error, error)))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'root =[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]'
    )
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().__init__(error, error)))
    print()

    pass
# @lc main=end