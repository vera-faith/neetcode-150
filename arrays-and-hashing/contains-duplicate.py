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
# Status: learned from example solution on 2026-10-20; re-solve from memory next time.
# Java equivalent: HashSet<Integer>, return true on !seen.add(n) style logic.
