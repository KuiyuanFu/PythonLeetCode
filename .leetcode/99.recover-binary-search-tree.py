# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (42.89%)
# Likes:    2438
# Dislikes: 91
# Total Accepted:    211.2K
# Total Submissions: 490.8K
# Testcase Example:  '[1,3,null,null,2]'
#
# You are given the root of a binary search tree (BST), where exactly two nodes
# of the tree were swapped by mistake. Recover the tree without changing its
# structure.
#
# Follow up: A solution using O(n) space is pretty straight forward. Could you
# devise a constant space solution?
#
#
# Example 1:
#
#
# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3
# makes the BST valid.
#
#
# Example 2:
#
#
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2
# and 3 makes the BST valid.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 1000].
# -2^31 <= Node.val <= 2^31 - 1
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个二叉搜索树，其中两个节点的值是交换了的。要恢复这个树，使用固定额外空间。
# 思想是，交换了的节点，一定是不符合二叉搜索关系的，只要找到这两个节点就可以了。
# 如果交换的两个节点，按照中序遍历的顺序，将会导致这个区间所有节点都不符合二叉搜索关系。
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
    def recoverTree(self, root: TreeNode) -> None:
        buffer = []
        buffer.append((root, True))
        first = None
        pre = None
        flag = True
        l = None
        while buffer:
            node, isFirstTime = buffer.pop()
            if isFirstTime:
                buffer.append((node, not isFirstTime))
                # 左侧
                if node.left:
                    buffer.append((node.left, True))

            else:
                # 右侧
                if node.right:
                    buffer.append((node.right, True))

                # 自己
                if not l:
                    l = node.val
                else:
                    # 找第一个
                    if flag:
                        if l > node.val:
                            first = pre
                            flag = False
                    # 找最后一个
                    else:
                        if l < node.val:
                            break
                l = max(l, node.val)
                pre = node

        first.val, pre.val = pre.val, first.val

        return root


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,3,null,null,2]')
    print('Output :')
    print(str(Solution().recoverTree(listToTreeNode([1, 3, None, None, 2]))))
    print('Exception :')
    print('[3,1,null,null,2]')
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [3,1,4,null,null,2]')
    print('Output :')
    print(str(Solution().recoverTree(listToTreeNode([3, 1, 4, None, None,
                                                     2]))))
    print('Exception :')
    print('[2,1,4,null,null,3]')
    print()

    pass
# @lc main=end