# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (42.01%)
# Likes:    4183
# Dislikes: 123
# Total Accepted:    191.7K
# Total Submissions: 456.2K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
#
#
# Example 1:
#
#
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
#
# Example 2:
#
#
# Input: nums = [-1]
# Output: [0]
#
#
# Example 3:
#
#
# Input: nums = [-1,-1]
# Output: [0,0]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc tags=binary-search;divide-and-conquer;sort;binary-indexed-tree;segment-tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个数组，求数组中每一个值对应有多少个元素小于其。
# 构建一棵搜索树，结点内存储此结点的元素个数，及在子树上小于其的个数。。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class TreeNode:
    def __init__(
        self,
        smallerCount: int = 0,
        appearTimes: int = 0,
        father: 'TreeNode' = None,
        left: 'TreeNode' = None,
        right: 'TreeNode' = None,
    ):
        self.smallerCount = smallerCount
        self.appearTimes = appearTimes
        self.father = father
        self.left = left
        self.right = right


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums)
        size = 20001
        nodes = [TreeNode() for _ in range(size)]

        def rMakeTree(father, l, r):
            if l > r:
                return None
            m = (l + r) // 2
            p = nodes[m]
            p.father = father
            p.left = rMakeTree(p, l, m - 1)
            p.right = rMakeTree(p, m + 1, r)
            return p

        rMakeTree(None, 0, size - 1)

        for n in nums:
            n = n + size // 2
            p = nodes[n]
            p.appearTimes += 1
            while p.father:
                if p == p.father.left:
                    p.father.smallerCount += 1
                p = p.father
        for i, n in enumerate(nums):
            n = n + size // 2
            p = nodes[n]

            p.appearTimes -= 1
            smallerCount = p.smallerCount

            while p.father:
                if p == p.father.right:
                    smallerCount += p.father.smallerCount + p.father.appearTimes
                else:
                    p.father.smallerCount -= 1
                p = p.father
            ret[i] = smallerCount

        return ret


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [5,2,6,1]')
    print('Exception :')
    print('[2,1,1,0]')
    print('Output :')
    print(str(Solution().countSmaller([5, 2, 6, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [-1]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().countSmaller([-1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [-1,-1]')
    print('Exception :')
    print('[0,0]')
    print('Output :')
    print(str(Solution().countSmaller([-1, -1])))
    print()

    pass
# @lc main=end