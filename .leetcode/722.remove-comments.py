# @lc app=leetcode id=722 lang=python3
#
# [722] Remove Comments
#
# https://leetcode.com/problems/remove-comments/description/
#
# algorithms
# Medium (36.93%)
# Likes:    508
# Dislikes: 1389
# Total Accepted:    49K
# Total Submissions: 132.3K
# Testcase Example:  '["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]'
#
# Given a C++ program, remove comments from it. The program source is an array
# of strings source where source[i] is the i^th line of the source code. This
# represents the result of splitting the original source code string by the
# newline character '\n'.
#
# In C++, there are two types of comments, line comments, and block
# comments.
#
#
# The string "//" denotes a line comment, which represents that it and the rest
# of the characters to the right of it in the same line should be ignored.
# The string "/*" denotes a block comment, which represents that all characters
# until the next (non-overlapping) occurrence of "*/" should be ignored. (Here,
# occurrences happen in reading order: line by line from left to right.) To be
# clear, the string "/*/" does not yet end the block comment, as the ending
# would be overlapping the beginning.
#
#
# The first effective comment takes precedence over others.
#
#
# For example, if the string "//" occurs in a block comment, it is ignored.
# Similarly, if the string "/*" occurs in a line or block comment, it is also
# ignored.
#
#
# If a certain line of code is empty after removing comments, you must not
# output that line: each string in the answer list will be non-empty.
#
# There will be no control characters, single quote, or double quote
# characters.
#
#
# For example, source = "string s = "/* Not a comment. */";" will not be a test
# case.
#
#
# Also, nothing else such as defines or macros will interfere with the
# comments.
#
# It is guaranteed that every open block comment will eventually be closed, so
# "/*" outside of a line or block comment always starts a new comment.
#
# Finally, implicit newline characters can be deleted by block comments. Please
# see the examples below for details.
#
# After removing the comments from the source code, return the source code in
# the same format.
#
#
# Example 1:
#
#
# Input: source = ["/*Test program */", "int main()", "{ ", "  // variable
# declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "
# comment for ", "   testing */", "a = b + c;", "}"]
# Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
# Explanation: The line by line code is visualized as below:
# /*Test program */
# int main()
# {
# ⁠ // variable declaration
# int a, b, c;
# /* This is a test
# ⁠  multiline
# ⁠  comment for
# ⁠  testing */
# a = b + c;
# }
# The string /* denotes a block comment, including line 1 and lines 6-9. The
# string // denotes line 4 as comments.
# The line by line output code is visualized as below:
# int main()
# {
# ⁠
# int a, b, c;
# a = b + c;
# }
#
#
# Example 2:
#
#
# Input: source = ["a/*comment", "line", "more_comment*/b"]
# Output: ["ab"]
# Explanation: The original source string is
# "a/*comment\nline\nmore_comment*/b", where we have bolded the newline
# characters.  After deletion, the implicit newline characters are deleted,
# leaving the string "ab", which when delimited by newline characters becomes
# ["ab"].
#
#
#
# Constraints:
#
#
# 1 <= source.length <= 100
# 0 <= source[i].length <= 80
# source[i] consists of printable ASCII characters.
# Every open block comment is eventually closed.
# There are no single-quote or double-quote in the input.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 去除注释。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        dfa = [
            # // /* */ \n other

            # normal
            [1, 2, 0, 4, 0],
            # //
            [5, 5, 5, 4, 5],
            # /*
            [6, 6, 3, 6, 6],
            # */
            [1, 2, 0, 4, 0],
            # \n
            [1, 2, 0, 4, 0],
            # //  ...
            [5, 5, 5, 4, 5],
            # /* ...
            [6, 6, 3, 6, 6],
        ]

        def getSymbol(s):
            if s == '//':
                return 0
            elif s == '/*':
                return 1
            elif s == '*/':
                return 2
            elif s == '\n':
                return 3
            else:
                return 4

        state = 0
        res = []
        l = []
        for line in source:
            i = 0
            line += '\n'
            while i < len(line):
                symbol = getSymbol(line[i:i + 2])
                state = dfa[state][symbol]
                # normal
                if state == 0:
                    l.append(line[i])
                # \n
                elif state == 4:
                    nl = ''.join(l)
                    if len(nl) > 0:
                        res.append(nl)
                    l.clear()
                if 0 < state < 4:
                    i += 1
                i += 1

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'source = ["/*Test program */", "int main()", "{ ", "  // variabledeclaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "comment for ", "   testing */", "a = b + c;", "}"]'
    )
    print('Exception :')
    print('["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]')
    print('Output :')
    print(
        str(Solution().removeComments([
            "/*Test program */", "int main()", "{ ",
            "  // variabledeclaration ", "int a, b, c;", "/* This is a test",
            "   multiline  ", "comment for ", "   testing */", "a = b + c;",
            "}"
        ])))
    print()

    print('Example 2:')
    print('Input : ')
    print('source = ["a/*comment", "line", "more_comment*/b"]')
    print('Exception :')
    print('["ab"]')
    print('Output :')
    print(
        str(Solution().removeComments(
            ["a/*comment", "line", "more_comment*/b"])))
    print()

    pass
# @lc main=end