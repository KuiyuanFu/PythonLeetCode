# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (63.24%)
# Likes:    1586
# Dislikes: 74
# Total Accepted:    153.9K
# Total Submissions: 242.9K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# Given the root of a binary tree, return an array of the largest value in each
# row of the tree (0-indexed).
#
#
#
#
# Example 1:
#
#
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
#
#
# Example 2:
#
#
# Input: root = [1,2,3]
# Output: [1,3]
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: [1]
#
#
# Example 4:
#
#
# Input: root = [1,null,2]
# Output: [1,2]
#
#
# Example 5:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree will be in the range [0, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
#
#
#

# @lc tags=tree;depth-first-search;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找树中，每一层最大的值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        q = [root] if root else []
        r = []
        while q:
            qn = []
            m = -(2**31)
            for p in q:
                m = max(m, p.val)
                if p.left:
                    qn.append(p.left)
                if p.right:
                    qn.append(p.right)
            r.append(m)
            q = qn
        return r

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,3,2,5,3,null,9]')
    print('Exception :')
    print('[1,3,9]')
    print('Output :')
    print(
        str(Solution().largestValues(listToTreeNode([1, 3, 2, 5, 3, None,
                                                     9]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,3]')
    print('Exception :')
    print('[1,3]')
    print('Output :')
    print(str(Solution().largestValues(listToTreeNode([1, 2, 3]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().largestValues(listToTreeNode([1]))))
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [1,null,2]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().largestValues(listToTreeNode([1, None, 2]))))
    print()

    print('Example 5:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().largestValues(listToTreeNode([]))))
    print()

    pass
# @lc main=end