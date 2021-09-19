# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#
# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (45.24%)
# Likes:    1664
# Dislikes: 473
# Total Accepted:    125.5K
# Total Submissions: 276.4K
# Testcase Example:  '[1,null,2,2]'
#
# Given the root of a binary search tree (BST) with duplicates, return all the
# mode(s) (i.e., the most frequently occurred element) in it.
#
# If the tree has more than one mode, return them in any order.
#
# Assume a BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than or equal
# to the node's key.
# The right subtree of a node contains only nodes with keys greater than or
# equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
# Example 1:
#
#
# Input: root = [1,null,2,2]
# Output: [2]
#
#
# Example 2:
#
#
# Input: root = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -10^5 <= Node.val <= 10^5
#
#
#
# Follow up: Could you do that without using any extra space? (Assume that the
# implicit stack space incurred due to recursion does not count).
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 得到重复次数最多的元素。
# 直接遍历。
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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s = [(root, True)]
        res = []
        maxTimes = 0
        time = 0
        n = -10000 - 1
        while s:
            p, f = s.pop()
            if f:
                s.append((p, False))
                if p.left:
                    s.append((p.left, True))
            else:
                if p.val == n:
                    time += 1
                else:
                    time = 1
                n = p.val
                if time == maxTimes:
                    res.append(n)
                elif time > maxTimes:
                    maxTimes = time
                    res.clear()
                    res.append(n)

                if p.right:
                    s.append((p.right, True))

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,2,2]')
    print('Exception :')
    print('[2]')
    print('Output :')
    print(str(Solution().findMode(listToTreeNode([1, None, 2, 2]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().findMode(listToTreeNode([0]))))

    pass
# @lc main=end