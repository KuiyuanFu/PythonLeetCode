# @lc app=leetcode id=1028 lang=python3
#
# [1028] Recover a Tree From Preorder Traversal
#
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/
#
# algorithms
# Hard (73.13%)
# Likes:    1326
# Dislikes: 36
# Total Accepted:    40.6K
# Total Submissions: 55.5K
# Testcase Example:  '"1-2--3--4-5--6--7"'
#
# We run a preorder depth-first search (DFS) on the root of a binary tree.
#
# At each node in this traversal, we output D dashes (where D is the depth of
# this node), then we output the value of this node.  If the depth of a node is
# D, the depth of its immediate child is D + 1.  The depth of the root node is
# 0.
#
# If a node has only one child, that child is guaranteed to be the left child.
#
# Given the output traversal of this traversal, recover the tree and return its
# root.
#
#
# Example 1:
#
#
# Input: traversal = "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
#
#
# Example 2:
#
#
# Input: traversal = "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
#
#
# Example 3:
#
#
# Input: traversal = "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
#
#
#
# Constraints:
#
#
# The number of nodes in the original tree is in the range [1, 1000].
# 1 <= Node.val <= 10^9
#
#
#

# @lc tags=two-pointers

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定先序遍历二叉树的结果，每个节点根据层数输出额外的‘-’，默认是左节点，恢复树。
# 直接递归，split('-')，根据连续空白结果的个数得到层数。
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

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        pesudo = TreeNode()

        s = [pesudo]
        l = 0
        for c in traversal.split('-'):
            if c == '':
                l += 1
            else:
                while len(s) > l + 1:
                    s.pop()
                t = s[-1]
                p = TreeNode(int(c))
                s.append(p)
                if t.left is None:
                    t.left = p
                else:
                    t.right = p
                l = 1

        return pesudo.left

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('traversal = "1-2--3--4-5--6--7"')
    print('Exception :')
    print('[1,2,5,3,4,6,7]')
    print('Output :')
    print(str(Solution().recoverFromPreorder("1-2--3--4-5--6--7")))
    print()

    print('Example 2:')
    print('Input : ')
    print('traversal = "1-2--3---4-5--6---7"')
    print('Exception :')
    print('[1,2,5,3,null,6,null,4,null,7]')
    print('Output :')
    print(str(Solution().recoverFromPreorder("1-2--3---4-5--6---7")))
    print()

    print('Example 3:')
    print('Input : ')
    print('traversal = "1-401--349---90--88"')
    print('Exception :')
    print('[1,401,null,349,88,90]')
    print('Output :')
    print(str(Solution().recoverFromPreorder("1-401--349---90--88")))
    print()

    pass
# @lc main=end