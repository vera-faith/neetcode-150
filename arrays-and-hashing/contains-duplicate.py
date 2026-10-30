from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False


# Pattern: seen set
# Time: O(n) — one pass. Space: O(n) — set can hold every element.
# Status: learned from example on 2026-10-20, then worked through and passed on NeetCode on 2026-10-29.
# Java equivalent: HashSet<Integer>, return true on !seen.add(n) style logic.
