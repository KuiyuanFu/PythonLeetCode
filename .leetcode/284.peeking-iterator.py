# @lc app=leetcode id=284 lang=python3
#
# [284] Peeking Iterator
#
# https://leetcode.com/problems/peeking-iterator/description/
#
# algorithms
# Medium (51.23%)
# Likes:    821
# Dislikes: 570
# Total Accepted:    138.4K
# Total Submissions: 268.9K
# Testcase Example:  '["PeekingIterator","next","peek","next","next","hasNext"]\n' +
#   '[[[1,2,3]],[],[],[],[],[]]'
#
# Design an iterator that supports the peek operation on a list in addition to
# the hasNext and the next operations.
#
# Implement the PeekingIterator class:
#
#
# PeekingIterator(int[] nums) Initializes the object with the given integer
# array nums.
# int next() Returns the next element in the array and moves the pointer to the
# next element.
# bool hasNext() Returns true if there are still elements in the array.
# int peek() Returns the next element in the array without moving the
# pointer.
#
#
#
# Example 1:
#
#
# Input
# ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
# [[[1, 2, 3]], [], [], [], [], []]
# Output
# [null, 1, 2, 2, 3, false]
#
# Explanation
# PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
# peekingIterator.next();    // return 1, the pointer moves to the next element
# [1,2,3].
# peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
# peekingIterator.next();    // return 2, the pointer moves to the next element
# [1,2,3]
# peekingIterator.next();    // return 3, the pointer moves to the next element
# [1,2,3]
# peekingIterator.hasNext(); // return False
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# All the calls to next and peek are valid.
# At most 1000 calls will be made to next, hasNext, and peek.
#
#
#
# Follow up: How would you extend your design to be generic and work with all
# types, not just integer?
#

# @lc tags=design

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定一个迭代器，扩展，实现peek函数，返回下一个值，但不移动指针。
# 用一个变量保存值，之后根据函数决定是否移动指针。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class PeekingIterator:
    def __init__(self, iterator: Iterator):

        self.iterator = iterator

        self._next()

    def _next(self):
        if self.iterator.hasNext():
            self.value = self.iterator.next()
        else:
            self.value = None

    def peek(self):
        return self.value

    def next(self):
        v = self.value
        self._next()
        return v

    def hasNext(self):
        return self.value != None


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    pass
# @lc main=end