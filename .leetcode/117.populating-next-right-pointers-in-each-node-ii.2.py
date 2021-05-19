# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (42.56%)
# Likes:    2446
# Dislikes: 200
# Total Accepted:    335.1K
# Total Submissions: 784.1K
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# Given a binary tree
#
#
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
#
#
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#
#
# Follow up:
#
#
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not
# count as extra space for this problem.
#
#
#
# Example 1:
#
#
#
#
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should
# populate each next pointer to point to its next right node, just like in
# Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
#
#
#
# Constraints:
#
#
# The number of nodes in the given tree is less than 6000.
# -100 <= node.val <= 100
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
import re
from imports import *

# @lc imports=end
# @lc idea=start
#
# 给定一个二叉树，使每个结点，next 指向同层的下一个结点。
# 发现之前都是想复杂了，每次只需要使用上层的结点，就可以直接得到下层结点的顺序了。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


# Definition for a Node.
class Node:
    def __init__(self,
                 val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        next = root
        while next:
            pre, p, next = None, next, None

            while p:

                if p.left:
                    if not next:
                        next = p.left
                    if pre:
                        pre.next = p.left
                    pre = p.left
                if p.right:
                    if not next:
                        next = p.right
                    if pre:
                        pre.next = p.right
                    pre = p.right
                p = p.next
        return root


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    print(str(Solution().connect(listToTreeNode([1, 2, 3, 4, 5, 6, 7]))))
    print(str(Solution().connect(listToTreeNode([1, 2, 3, 4, 5, None, 7]))))

    pass
# @lc main=end