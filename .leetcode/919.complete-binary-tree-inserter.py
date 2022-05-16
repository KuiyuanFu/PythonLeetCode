# @lc app=leetcode id=919 lang=python3
#
# [919] Complete Binary Tree Inserter
#
# https://leetcode.com/problems/complete-binary-tree-inserter/description/
#
# algorithms
# Medium (63.97%)
# Likes:    778
# Dislikes: 82
# Total Accepted:    39K
# Total Submissions: 60.8K
# Testcase Example:  '["CBTInserter","insert","insert","get_root"]\n[[[1,2]],[3],[4],[]]'
#
# A complete binary tree is a binary tree in which every level, except possibly
# the last, is completely filled, and all nodes are as far left as possible.
#
# Design an algorithm to insert a new node to a complete binary tree keeping it
# complete after the insertion.
#
# Implement the CBTInserter class:
#
#
# CBTInserter(TreeNode root) Initializes the data structure with the root of
# the complete binary tree.
# int insert(int v) Inserts a TreeNode into the tree with value Node.val == val
# so that the tree remains complete, and returns the value of the parent of the
# inserted TreeNode.
# TreeNode get_root() Returns the root node of the tree.
#
#
#
# Example 1:
#
#
# Input
# ["CBTInserter", "insert", "insert", "get_root"]
# [[[1, 2]], [3], [4], []]
# Output
# [null, 1, 2, [1, 2, 3, 4]]
#
# Explanation
# CBTInserter cBTInserter = new CBTInserter([1, 2]);
# cBTInserter.insert(3);  // return 1
# cBTInserter.insert(4);  // return 2
# cBTInserter.get_root(); // return [1, 2, 3, 4]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree will be in the range [1, 1000].
# 0 <= Node.val <= 5000
# root is a complete binary tree.
# 0 <= val <= 5000
# At most 10^4 calls will be made to insert and get_root.
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 完全二叉树，插入。
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
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.l = [self.root]
        self.idx = 0

        while True:
            node = self.l[self.idx]
            if node.left is None:
                break
            self.l.append(node.left)
            if node.right is None:
                break
            self.l.append(node.right)
            self.idx += 1

    def insert(self, val: int) -> int:
        node = self.l[self.idx]
        if node.left is None:
            node.left = TreeNode(val=val)
            self.l.append(node.left)
        else:
            node.right = TreeNode(val=val)
            self.l.append(node.right)
            self.idx += 1
        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root

        # Your CBTInserter object will be instantiated and called as such:
        # obj = CBTInserter(root)
        # param_1 = obj.insert(val)
        # param_2 = obj.get_root()
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error)))
    print()

    pass
# @lc main=end