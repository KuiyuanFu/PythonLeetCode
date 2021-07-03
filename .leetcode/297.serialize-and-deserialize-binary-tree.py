# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (50.73%)
# Likes:    4576
# Dislikes: 207
# Total Accepted:    465.6K
# Total Submissions: 912K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
#
# Clarification: The input/output format is the same as how LeetCode serializes
# a binary tree. You do not necessarily need to follow this format, so please
# be creative and come up with different approaches yourself.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
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
# Input: root = [1,2]
# Output: [1,2]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
#
#
#

# @lc tags=tree;design

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 序列化和反序列化一个二叉树。
# 仿照leetcode的序列化方式，使用广度优先的队列来实现。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Codec:
    def serialize(self, root):
        if not root:
            return ''
        s = [root.val]
        import queue
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            node = q.get()

            if node.left:
                q.put(node.left)
                s.append(node.left.val)
            else:
                s.append(None)
            if node.right:
                q.put(node.right)
                s.append(node.right.val)
            else:
                s.append(None)

        while len(s) > 0 and s[-1] == None:
            s.pop()
        return ','.join([str(c) for c in s])

    def deserialize(self, data: str):
        if len(data) == 0:
            return None
        l = [None if c == 'None' else int(c) for c in data.split(',')]

        head = TreeNode(val=l[0])
        if len(l) == 1:
            return head

        import queue
        q = queue.Queue()
        q.put(head)
        f = None
        flag = True
        for n in range(1, len(l)):

            n = l[n]
            if n != None:
                n = TreeNode(val=n)
                q.put(n)
            if flag:
                f = q.get()
                f.left = n
            else:
                f.right = n
            flag = not flag

        return head


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,null,null,4,5]')
    print('Exception :')
    print('[1,2,3,null,null,4,5]')
    print('Output :')
    print(str(Solution().serialize([1, 2, 3, null, null, 4, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().serialize([])))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().serialize([1])))
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [1,2]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().serialize([1, 2])))
    print()

    pass
# @lc main=end