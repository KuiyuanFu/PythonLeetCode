# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#
# https://leetcode.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (56.66%)
# Likes:    2496
# Dislikes: 899
# Total Accepted:    240.8K
# Total Submissions: 424.8K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# You are given a nested list of integers nestedList. Each element is either an
# integer or a list whose elements may also be integers or other lists.
# Implement an iterator to flatten it.
#
# Implement the NestedIterator class:
#
#
# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with
# the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested
# list and false otherwise.
#
#
# Your code will be tested with the following pseudocode:
#
#
# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
# ⁠   append iterator.next() to the end of res
# return res
#
#
# If res matches the expected flattened list, then your code will be judged as
# correct.
#
#
# Example 1:
#
#
# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false, the
# order of elements returned by next should be: [1,1,2,1,1].
#
#
# Example 2:
#
#
# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, the
# order of elements returned by next should be: [1,4,6].
#
#
#
# Constraints:
#
#
# 1 <= nestedList.length <= 500
# The values of the integers in the nested list is in the range [-10^6, 10^6].
#
#
#

# @lc tags=stack;design

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 将一个元素和数组混合的数组，展平成一个只含有元素的数组。
# 直接栈。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList):
        self.s = nestedList[::-1]
        self.n = None
        self._next()

    def _next(self):
        while self.s:
            n = self.s.pop()
            if n.isInteger():
                self.n = n.getInteger()
                return
            else:
                self.s += n.getList()[::-1]

        self.n = None

    def next(self) -> int:
        r = self.n
        self._next()
        return r

    def hasNext(self) -> bool:
        return self.n is not None

        # Your NestedIterator object will be instantiated and called as such:
        # i, v = NestedIterator(nestedList), []
        # while i.hasNext(): v.append(i.next())
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    pass
# @lc main=end
