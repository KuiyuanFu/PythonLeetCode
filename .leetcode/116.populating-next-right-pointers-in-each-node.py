# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (49.86%)
# Likes:    3399
# Dislikes: 168
# Total Accepted:    492.7K
# Total Submissions: 982.5K
# Testcase Example:  '[1,2,3,4,5,6,7]'
#
# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following
# definition:
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
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer to point to its next right node, just like
# in Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
#
#
#
# Constraints:
#
#
# The number of nodes in the given tree is less than 4096.
# -1000 <= node.val <= 1000
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个完美的二叉树，除了叶子结点都是满子结点的。
# 使每个结点，next 指向同层的下一个结点。
# 使用固定额外空间。
# 利用 next 指针，先指向父结点，之后根据父结点来确定下一个结点。
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
        if not root:
            return root
        # set fathe
        p = root
        while p:
            if p.left:
                p.left.next = p
                p.right.next = p
                p = p.left
            else:
                while p.next:
                    if p == p.next.left:
                        p = p.next.right
                        break
                    else:
                        p = p.next
                # root
                if not p.next:
                    break
        # find next
        def findNext(p: 'Node'):
            depth = 0
            while p.next:
                if p == p.next.left:
                    p = p.next.right
                    for _ in range(depth):
                        p = p.left
                    return p
                else:
                    p = p.next
                    depth += 1
            return None

        # find max left
        pNextLevel = root
        while pNextLevel.left:
            pNextLevel = pNextLevel.left
        # set
        while pNextLevel:
            p, pNextLevel = pNextLevel, pNextLevel.next
            while p:
                pNext = findNext(p)
                p.next = pNext
                p = pNext

        return root


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,4,5,6,7]')
    print('Output :')
    print(str(Solution().connect(listToTreeNode([1, 2, 3, 4, 5, 6, 7]))))
    print('Exception :')
    print('[1,#,2,3,#,4,5,6,7,#]')
    print()

    pass
# @lc main=end