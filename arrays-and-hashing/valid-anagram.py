from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        for n in s:
            countS[n] = countS.get(n, 0) + 1

        countT = {}
        for n in t:
            countT[n] = countT.get(n, 0) + 1

        return countS == countT


# Pattern: frequency dicts (counting)
# A set is not enough: it forgets HOW MANY times a character appears.
# Same length but different letters -> countS == countT evaluates to False,
# and that False is what gets returned. No extra if needed.
# Time: O(n). Space: O(n) (at most one entry per distinct character).
# Solved on NeetCode: 2026-10-29.
# Note: loop variable name (n / c / ch) is arbitrary - it holds each character
# itself, not an index. Faith prefers n for consistency across problems.
