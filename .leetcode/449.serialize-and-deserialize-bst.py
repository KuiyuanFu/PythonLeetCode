# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#
# https://leetcode.com/problems/serialize-and-deserialize-bst/description/
#
# algorithms
# Medium (55.04%)
# Likes:    2226
# Dislikes: 107
# Total Accepted:    166.5K
# Total Submissions: 302K
# Testcase Example:  '[2,1,3]'
#
# Serialization is converting a data structure or object into a sequence of
# bits so that it can be stored in a file or memory buffer, or transmitted
# across a network connection link to be reconstructed later in the same or
# another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree. There
# is no restriction on how your serialization/deserialization algorithm should
# work. You need to ensure that a binary search tree can be serialized to a
# string, and this string can be deserialized to the original tree structure.
#
# The encoded string should be as compact as possible.
#
#
# Example 1:
# Input: root = [2,1,3]
# Output: [2,1,3]
# Example 2:
# Input: root = []
# Output: []
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# 0 <= Node.val <= 10^4
# The input tree is guaranteed to be a binary search tree.
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 序列化二叉树。
# 使用队列，像leetcode那种序列化方式。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:

        data = []
        q = deque([root])
        while q:
            p = q.popleft()
            if p:
                data.append(p.val)
                q.append(p.left)
                q.append(p.right)
            else:
                data.append(-1)
        return '.'.join([str(d) for d in data])

    def deserialize(self, data: str) -> TreeNode:
        data = [int(d) for d in data.split('.')]
        pseudo = TreeNode()
        q = deque([[pseudo, False]])
        f = False
        for d in data:
            p, f = q[0]
            if f:
                q[0][1] = False
            else:
                q.popleft()
            if d != -1:
                pn = TreeNode(d)
                q.append([pn, True])
                if f:
                    p.left = pn
                else:
                    p.right = pn
        return pseudo.right

        # Your Codec object will be instantiated and called as such:
        # Your Codec object will be instantiated and called as such:
        # ser = Codec()
        # deser = Codec()
        # deser = Codec()
        # tree = ser.serialize(root)
        # ans = deser.deserialize(tree)
        # return ans
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    pass
# @lc main=end