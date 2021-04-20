# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (34.98%)
# Likes:    343
# Dislikes: 99
# Total Accepted:    274.9K
# Total Submissions: 785.8K
# Testcase Example:  '"/home/"'
#
# Given a string path, which is an absolute path (starting with a slash '/') to
# a file or directory in a Unix-style file system, convert it to the simplified
# canonical path.
#
# In a Unix-style file system, a period '.' refers to the current directory, a
# double period '..' refers to the directory up a level, and any multiple
# consecutive slashes (i.e. '//') are treated as a single slash '/'. For this
# problem, any other format of periods such as '...' are treated as
# file/directory names.
#
# The canonical path should have the following format:
#
#
# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.
# The path only contains the directories on the path from the root directory to
# the target file or directory (i.e., no period '.' or double period '..')
#
#
# Return the simplified canonical path.
#
#
# Example 1:
#
#
# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory
# name.
#
#
# Example 2:
#
#
# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the
# root level is the highest level you can go.
#
#
# Example 3:
#
#
# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced
# by a single one.
#
#
# Example 4:
#
#
# Input: path = "/a/./b/../../c/"
# Output: "/c"
#
#
#
# Constraints:
#
#
# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.
#
#
#


# @lc tags=string;stack

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定一个字符串，内容是一个路径，求其最简化形式。
# 有限状态自动机，结合栈。
# 因为有返回上一级目录的操作，使用栈更方便一点。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def simplifyPath(self, path: str) -> str:
        fsa = [
            # . c

            # 0 init
            [1, 2],
            # 1 .
            [3, 2],
            # 2 c
            [2, 2],
            # 3 ..
            [2, 2],

        ]

        path += '/'
        stack = []
        t = ''
        i = 0
        for c in path:
            if c == '/':
                if i == 2:
                    stack.append(t)
                elif i == 3:
                    if len(stack) > 0:
                        stack.pop()
                i = 0
                t = ''
            else:
                t += c
                if c == '.':
                    i = fsa[i][0]
                else:
                    i = fsa[i][1]

        return '/' + '/'.join(stack)

# @lc code=end


# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('path = "/home/"')
    print('Output :')
    print(str(Solution().simplifyPath("/home/")))
    print('Exception :')
    print('"/home"')
    print()

    print('Example 2:')
    print('Input : ')
    print('path = "/../"')
    print('Output :')
    print(str(Solution().simplifyPath("/../")))
    print('Exception :')
    print('"/"')
    print()

    print('Example 3:')
    print('Input : ')
    print('path = "/home//foo/"')
    print('Output :')
    print(str(Solution().simplifyPath("/home//foo/")))
    print('Exception :')
    print('"/home/foo"')
    print()

    print('Example 4:')
    print('Input : ')
    print('path = "/a/./b/../../c/"')
    print('Output :')
    print(str(Solution().simplifyPath("/a/./b/../../c/")))
    print('Exception :')
    print('"/c"')
    print()

    pass
# @lc main=end
