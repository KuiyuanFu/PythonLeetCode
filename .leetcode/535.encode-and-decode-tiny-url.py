# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#
# https://leetcode.com/problems/encode-and-decode-tinyurl/description/
#
# algorithms
# Medium (82.91%)
# Likes:    1004
# Dislikes: 1999
# Total Accepted:    154K
# Total Submissions: 185.6K
# Testcase Example:  '"https://leetcode.com/problems/design-tinyurl"'
#
# Note: This is a companion problem to the System Design problem: Design
# TinyURL.
#
# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such
# as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a
# tiny URL.
#
# There is no restriction on how your encode/decode algorithm should work. You
# just need to ensure that a URL can be encoded to a tiny URL and the tiny URL
# can be decoded to the original URL.
#
# Implement the Solution class:
#
#
# Solution() Initializes the object of the system.
# String encode(String longUrl) Returns a tiny URL for the given longUrl.
# String decode(String shortUrl) Returns the original long URL for the given
# shortUrl. It is guaranteed that the given shortUrl was encoded by the same
# object.
#
#
#
# Example 1:
#
#
# Input: url = "https://leetcode.com/problems/design-tinyurl"
# Output: "https://leetcode.com/problems/design-tinyurl"
#
# Explanation:
# Solution obj = new Solution();
# string tiny = obj.encode(url); // returns the encoded tiny url.
# string ans = obj.decode(tiny); // returns the original url after deconding
# it.
#
#
#
# Constraints:
#
#
# 1 <= url.length <= 10^4
# url is guranteed to be a valid URL.
#
#
#

# @lc tags=hash-table;math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 改成短地址，就是双向映射。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Codec:
    def __init__(self) -> None:
        self.toL = {}
        self.host = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        while True:
            r = random.randrange(0, 1000000)
            r = str(r).zfill(6)
            if r in self.toL:
                continue
            self.toL[r] = longUrl
            return self.host + r

    def decode(self, shortUrl: str) -> str:
        r = shortUrl[len(self.host):]
        return self.toL[r]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('url = "https://leetcode.com/problems/design-tinyurl"')
    print('Exception :')
    print('"https://leetcode.com/problems/design-tinyurl"')
    print('Output :')
    print(str(Solution().encode(error)))
    print()

    pass
# @lc main=end