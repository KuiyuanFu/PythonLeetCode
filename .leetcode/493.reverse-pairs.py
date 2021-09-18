# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#
# https://leetcode.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (28.43%)
# Likes:    1947
# Dislikes: 161
# Total Accepted:    65.1K
# Total Submissions: 228.1K
# Testcase Example:  '[1,3,2,3,1]'
#
# Given an integer array nums, return the number of reverse pairs in the
# array.
#
# A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] >
# 2 * nums[j].
#
#
# Example 1:
# Input: nums = [1,3,2,3,1]
# Output: 2
# Example 2:
# Input: nums = [2,4,3,5,1]
# Output: 3
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#

# @lc tags=binary-search;divide-and-conquer;sort;binary-indexed-tree;segment-tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求翻转对数。
# 直接平衡二叉搜索树。
#
# @lc idea=end

# @lc group=binary-indexed-tree

# @lc rank=10


# @lc code=start
class Node:
    def __init__(self, v, c=0, a=0, l=None, r=None, f=None, h=1) -> None:
        self.l = l
        self.r = r
        self.f = f
        self.c = c
        self.a = a
        self.v = v
        self.h = h
        pass


class Solution:
    def getc(self, p):
        return p.c if p else 0

    def geth(self, p):
        return p.h if p else 0

    def geta(self, p):
        return p.a if p else 0

    def updateh(self, p):
        p.h = 1 + max(self.geth(p.l), self.geth(p.r))

    def updatea(self, p):
        p.a = p.c + self.geta(p.l) + self.geta(p.r)

    def updateAll(self, p, pf, pn):
        if p == self.root:
            self.root = pn
        pn.f = pf
        if pf:
            if pf.l == p:
                pf.l = pn
            else:
                pf.r = pn
        self.updateh(p)
        self.updateh(pn)
        self.updatea(p)
        self.updatea(pn)

    def turnLeft(self, p: Node):
        pf = p.f
        pl, pr = p.l, p.r

        # 将右节点的左节点，放在根节点的右节点位置上。
        p.r = pr.l
        if p.r:
            p.r.f = p

        # 将根节点放在右节点的左节点位置上
        pr.l = p
        p.f = pr

        # 更新父节点
        self.updateAll(p, pf, pr)
        return pr

    def turnRight(self, p: Node):
        pf = p.f
        pl, pr = p.l, p.r

        # 将左节点的右节点，放在根节点的左节点位置上。
        p.l = pl.r
        if p.l:
            p.l.f = p

        # 将根节点放在左节点的右节点位置上
        pl.r = p
        p.f = pl

        # 更新父节点
        self.updateAll(p, pf, pl)

        return pl

    def add(self, v):
        p = self.root
        while p.v != v:
            p.a += 1
            if v < p.v:
                if not p.l:
                    p.l = Node(v, f=p)
                p = p.l
            else:
                if not p.r:
                    p.r = Node(v, f=p)
                p = p.r
        p.c += 1
        p.a += 1

        while p.f:
            pf = p.f
            # 没改变高度
            if p.h + 1 == pf.h:
                break
            # 改变了高度
            pflh, pfrh = self.geth(pf.l), self.geth(pf.r)

            d = (pflh - pfrh)
            # 还是平衡的
            if abs(d) <= 1:
                self.updateh(p.f)
                p = p.f
                continue
            plh, prh = self.geth(p.l), self.geth(p.r)
            # 左侧高
            if d > 0:
                if prh > plh:
                    self.turnLeft(p)
                p = self.turnRight(pf)
            # 右侧高
            else:
                if plh > prh:
                    self.turnRight(p)
                p = self.turnLeft(pf)

    # search  count where p.v bigger than or same to  v
    def search(self, v):
        p = self.root
        res = 0
        while p:
            if v <= p.v:
                res += p.c + self.geta(p.r)
                if v == p.v:
                    break
                p = p.l
            else:
                p = p.r
        return res

    def reversePairs(self, nums: List[int]) -> int:
        self.root = Node(0)
        res = 0
        for n in nums:
            t = n * 2 + 1
            res += self.search(t)
            self.add(n)
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,2,3,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().reversePairs([1, 3, 2, 3, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,4,3,5,1]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().reversePairs([2, 4, 3, 5, 1])))
    print()
    print('4')
    print(str(Solution().reversePairs([5, 4, 3, 2, 1])))

    pass
# @lc main=end