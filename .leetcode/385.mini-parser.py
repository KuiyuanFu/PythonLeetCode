# @lc app=leetcode id=385 lang=python3
#
# [385] Mini Parser
#
# https://leetcode.com/problems/mini-parser/description/
#
# algorithms
# Medium (34.97%)
# Likes:    308
# Dislikes: 1017
# Total Accepted:    44.3K
# Total Submissions: 126.3K
# Testcase Example:  '"324"'
#
# Given a string s represents the serialization of a nested list, implement a
# parser to deserialize it and return the deserialized NestedInteger.
#
# Each element is either an integer or a list whose elements may also be
# integers or other lists.
#
#
# Example 1:
#
#
# Input: s = "324"
# Output: 324
# Explanation: You should return a NestedInteger object which contains a single
# integer 324.
#
#
# Example 2:
#
#
# Input: s = "[123,[456,[789]]]"
# Output: [123,[456,[789]]]
# Explanation: Return a NestedInteger object containing a nested list with 2
# elements:
# 1. An integer containing value 123.
# 2. A nested list containing two elements:
# ⁠   i.  An integer containing value 456.
# ⁠   ii. A nested list with one element:
# ⁠        a. An integer containing value 789
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^4
# s consists of digits, square brackets "[]", negative sign '-', and commas
# ','.
# s is the serialization of valid NestedInteger.
#
#
#

# @lc tags=string;stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一个字符串表示的嵌套对象，反序列化出来。
# 直接递归。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        ss = s.split(',')
        stack = [NestedInteger()]
        for s in ss:
            i, l = 0, len(s)

            while i < l and s[i] == '[':
                stack.append(NestedInteger())
                i += 1
            n = 0
            f = None

            while i < l:
                c = s[i]
                if c == ']':
                    break
                elif c == '-':
                    f = False
                else:
                    n = n * 10 + int(c)
                    if f is None:
                        f = True
                i += 1
            if f is not None:
                if not f:
                    n = -n
                node = NestedInteger(n)
                stack[-1].add(node)

            while i < l and s[i] == ']':
                node = stack.pop()
                stack[-1].add(node)
                i += 1

        return stack[0].getList()[0]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "324"')
    print('Exception :')
    print('324')
    print('Output :')
    print(str(Solution().deserialize("324")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "[123,[456,[789]]]"')
    print('Exception :')
    print('[123,[456,[789]]]')
    print('Output :')
    print(str(Solution().deserialize("[123,[456,[789]]]")))
    print()

    pass
# @lc main=end