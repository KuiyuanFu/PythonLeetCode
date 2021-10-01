# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
#
# algorithms
# Easy (52.67%)
# Likes:    946
# Dislikes: 273
# Total Accepted:    128.1K
# Total Submissions: 242.9K
# Testcase Example:  '["Shogun","Tapioca Express","Burger King","KFC"]\n' +
# '["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]'
#
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both
# have a list of favorite restaurants represented by strings.
#
# You need to help them find out their common interest with the least list
# index sum. If there is a choice tie between answers, output all of them with
# no order requirement. You could assume there always exists an answer.
#
#
# Example 1:
#
#
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =
# ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
#
#
# Example 2:
#
#
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =
# ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is
# "Shogun" with index sum 1 (0+1).
#
#
# Example 3:
#
#
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =
# ["KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
#
#
# Example 4:
#
#
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =
# ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
#
#
# Example 5:
#
#
# Input: list1 = ["KFC"], list2 = ["KFC"]
# Output: ["KFC"]
#
#
#
# Constraints:
#
#
# 1 <= list1.length, list2.length <= 1000
# 1 <= list1[i].length, list2[i].length <= 30
# list1[i] and list2[i] consist of spaces ' ' and English letters.
# All the stings of list1 are unique.
# All the stings of list2 are unique.
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最小索引和。
# 字典存索引。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        l = len(list1) + len(list2)
        res = []
        for i, s in enumerate(list1):
            d[s] = i
        for i, s in enumerate(list2):
            if s in d:
                lt = i + d[s]
                if lt == l:
                    res.append(s)
                elif lt < l:
                    l = lt
                    res.clear()
                    res.append(s)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]'
    )
    print('Exception :')
    print('["Shogun"]')
    print('Output :')
    print(
        str(Solution().findRestaurant(
            ["Shogun", "Tapioca Express", "Burger King", "KFC"], [
                "Piatti", "The Grill at Torrey Pines",
                "Hungry Hunter Steakhouse", "Shogun"
            ])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =["KFC","Shogun","Burger King"]'
    )
    print('Exception :')
    print('["Shogun"]')
    print('Output :')
    print(
        str(Solution().findRestaurant(
            ["Shogun", "Tapioca Express", "Burger King", "KFC"],
            ["KFC", "Shogun", "Burger King"])))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =["KFC","Burger King","Tapioca Express","Shogun"]'
    )
    print('Exception :')
    print('["KFC","Burger King","Tapioca Express","Shogun"]')
    print('Output :')
    print(
        str(Solution().findRestaurant(
            ["Shogun", "Tapioca Express", "Burger King", "KFC"],
            ["KFC", "Burger King", "Tapioca Express", "Shogun"])))
    print()

    print('Example 4:')
    print('Input : ')
    print(
        'list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 =["KNN","KFC","Burger King","Tapioca Express","Shogun"]'
    )
    print('Exception :')
    print('["KFC","Burger King","Tapioca Express","Shogun"]')
    print('Output :')
    print(
        str(Solution().findRestaurant(
            ["Shogun", "Tapioca Express", "Burger King", "KFC"],
            ["KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"])))
    print()

    print('Example 5:')
    print('Input : ')
    print('list1 = ["KFC"], list2 = ["KFC"]')
    print('Exception :')
    print('["KFC"]')
    print('Output :')
    print(str(Solution().findRestaurant(["KFC"], ["KFC"])))
    print()

    pass
# @lc main=end