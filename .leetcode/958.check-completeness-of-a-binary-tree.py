# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
#
# algorithms
# Medium (53.78%)
# Likes:    2173
# Dislikes: 30
# Total Accepted:    124.8K
# Total Submissions: 232K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given the root of a binary tree, determine if it is a complete binary tree.
#
# In a complete binary tree, every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2^h nodes inclusive at the last level
# h.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values
# {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left
# as possible.
#
#
# Example 2:
#
#
# Input: root = [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 100].
# 1 <= Node.val <= 1000
#
#
#

# @lc tags=array;sort

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断是否是满二叉树。
# 直接双向队列，迭代。出现子节点为空后，不能出现非空子节点。
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

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        f = True
        q = deque([root])
        while q:
            p = q.popleft()
            if p.left:
                if not f:
                    return False
                q.append(p.left)
            else:
                f = False
            if p.right:
                if not f:
                    return False
                q.append(p.right)
            else:
                f = False

        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,4,5,6]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isCompleteTree(listToTreeNode([1, 2, 3, 4, 5, 6]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,3,4,5,null,7]')
    print('Exception :')
    print('false')
    print('Output :')
    print(
        str(Solution().isCompleteTree(listToTreeNode([1, 2, 3, 4, 5, None,
                                                      7]))))
    print()

    pass
# @lc main=end