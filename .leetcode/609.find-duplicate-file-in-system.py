# @lc app=leetcode id=609 lang=python3
#
# [609] Find Duplicate File in System
#
# https://leetcode.com/problems/find-duplicate-file-in-system/description/
#
# algorithms
# Medium (63.23%)
# Likes:    734
# Dislikes: 862
# Total Accepted:    87.5K
# Total Submissions: 138.2K
# Testcase Example:  '["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]'
#
# Given a list paths of directory info, including the directory path, and all
# the files with contents in this directory, return all the duplicate files in
# the file system in terms of their paths. You may return the answer in any
# order.
#
# A group of duplicate files consists of at least two files that have the same
# content.
#
# A single directory info string in the input list has the following
# format:
#
#
# "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ...
# fn.txt(fn_content)"
#
#
# It means there are n files (f1.txt, f2.txt ... fn.txt) with content
# (f1_content, f2_content ... fn_content) respectively in the directory
# "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the
# directory is just the root directory.
#
# The output is a list of groups of duplicate file paths. For each group, it
# contains all the file paths of the files that have the same content. A file
# path is a string that has the following format:
#
#
# "directory_path/file_name.txt"
#
#
#
# Example 1:
# Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c
# 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
# Output:
# [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
# Example 2:
# Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c
# 3.txt(abcd)","root/c/d 4.txt(efgh)"]
# Output:
# [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
#
#
# Constraints:
#
#
# 1 <= paths.length <= 2 * 10^4
# 1 <= paths[i].length <= 3000
# 1 <= sum(paths[i].length) <= 5 * 10^5
# paths[i] consist of English letters, digits, '/', '.', '(', ')', and ' '.
# You may assume no files or directories share the same name in the same
# directory.
# You may assume each given directory info represents a unique directory. A
# single blank space separates the directory path and file info.
#
#
#
# Follow up:
#
#
# Imagine you are given a real file system, how will you search files? DFS or
# BFS?
# If the file content is very large (GB level), how will you modify your
# solution?
# If you can only read the file by 1kb each time, how will you modify your
# solution?
# What is the time complexity of your modified solution? What is the most
# time-consuming part and memory-consuming part of it? How to optimize?
# How to make sure the duplicated files you find are not false positive?
#
#
#

# @lc tags=hash-table;string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 相同文件。
# 字典。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}
        for p in paths:
            ps = p.split()
            dir = ps[0]
            for idx in range(1, len(ps)):
                pss = ps[idx]
                idxL = pss.index('(')
                name = pss[:idxL]
                content = pss[idxL + 1:len(pss) - 1]
                filePath = dir + '/' + name
                if content not in d:
                    d[content] = []
                d[content].append(filePath)
        res = []
        for k in d.keys():
            l = d[k]
            if len(l) > 1:
                res.append(l)

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]'
    )
    print('Exception :')
    print(
        '[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]'
    )
    print('Output :')
    print(
        str(Solution().findDuplicate([
            "root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)",
            "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"
        ])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c3.txt(abcd)","root/c/d 4.txt(efgh)"]'
    )
    print('Exception :')
    print(
        '[["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]')
    print('Output :')
    print(
        str(Solution().findDuplicate([
            "root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)",
            "root/c/d 4.txt(efgh)"
        ])))
    print()

    pass
# @lc main=end