# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (67.09%)
# Likes:    2409
# Dislikes: 215
# Total Accepted:    223.8K
# Total Submissions: 332.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the average value of the nodes on
# each level in the form of an array. Answers within 10^-5 of the actual answer
# will be accepted.
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5,
# and on level 2 is 11.
# Hence return [3, 14.5, 11].
#
#
# Example 2:
#
#
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 广度优先遍历二叉树。
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = [root] if root else []
        while q:
            qn = []
            s = 0
            for p in q:
                s += p.val
                if p.left:
                    qn.append(p.left)
                if p.right:
                    qn.append(p.right)
            res.append(s / len(q))
            q = qn
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Exception :')
    print('[3.00000,14.50000,11.00000]')
    print('Output :')
    print(
        str(Solution().averageOfLevels(
            listToTreeNode([3, 9, 20, None, None, 15, 7]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [3,9,20,15,7]')
    print('Exception :')
    print('[3.00000,14.50000,11.00000]')
    print('Output :')
    print(str(Solution().averageOfLevels(listToTreeNode([3, 9, 20, 15, 7]))))
    print()

    pass
# @lc main=end