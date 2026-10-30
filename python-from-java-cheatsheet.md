# Python from Java — NeetCode Cheatsheet

Faith's refresher: you already know the logic from Java. This is just syntax translation.

## The big mindset shifts
1. No types on variables, no semicolons, no braces — indentation IS the block.
2. No `public static void main` — NeetCode gives you `class Solution:` with one method.
3. Almost everything you used `HashMap / HashSet / ArrayList` for has a 1-line built-in.

## Data structures: Java -> Python
| Java | Python | Notes |
|---|---|---|
| `ArrayList<Integer>` | `list` = `[]` | `.append(x)`, `.pop()`, `len(a)` not `a.size()` |
| `int[]` array | `list` | Same thing in practice for NeetCode |
| `HashMap<K,V>` | `dict` = `{}` | `d[k] = v`, `d.get(k, 0)`, `k in d` |
| `HashSet<T>` | `set` = `set()` | `.add(x)`, `x in s`, no duplicates |
| `String` | `str` | Immutable in both. `s[i]`, `len(s)` |
| `StringBuilder` | `list` of chars + `"".join(chars)` | Or just build strings in a list |
| `Stack<T>` | `list` | `.append()` = push, `.pop()` = pop |
| `Queue<T>` (LinkedList) | `collections.deque` | `.append()`, `.popleft()` — list pop(0) is O(n) |
| `PriorityQueue` (min) | `heapq` | `heapq.heappush(h,x)`, `heapq.heappop(h)` — min-heap by default |
| `null` | `None` | Capital N |
| `true / false` | `True / False` | Capital first letter |

## Loops & control
```python
for n in nums:              # Java: for (int n : nums)
for i in range(len(nums)):  # Java: for (int i = 0; i < nums.length; i++)
for i, n in enumerate(nums):# index AND value together — use this a lot
while l < r:                # same idea, no parens needed
if x in seen:               # Java: seen.contains(x)
elif / else                 # elif = else if
and / or / not              # Java: && || !
```

## Operations that trip Java brains
- Integer division: `a // b` (Java `/` on ints). `a / b` in Python = float division.
- No `i++` — use `i += 1`.
- Swap: `a, b = b, a` (no temp variable).
- Slicing: `s[l:r]` = chars from l up to but NOT including r. `s[::-1]` = reversed string.
- Negative index: `nums[-1]` = last element (Java: `nums[nums.length-1]`).
- Length: `len(x)` for list/string/dict/set — one function for everything.
- Membership: `x in thing` works for list, set, dict (keys), and string.

## The NeetCode workhorses
- `Counter(nums)` — frequency map in one line (for anagrams, top-k).
- `defaultdict(int)` / `defaultdict(list)` — dict that auto-creates missing keys, no `getOrDefault` dance.
- Sorting: `nums.sort()` in place, `sorted(nums)` returns new. Sort by key: `sorted(words, key=lambda w: len(w))` (lambda = Java's `->`).
- List comprehension: `[x*2 for x in nums if x > 0]` = loop + filter + collect in one line.
- Unpacking: `a, b = pair`, `first, *rest = nums`.

## Method skeleton (every problem)
```python
class Solution:
    def methodName(self, nums: List[int]) -> bool:
        # your code, indented
        return True
```
- `self` = Java's implicit `this`, but you must write it as the first parameter.
- `-> bool` is just a type hint for readability — Python won't enforce it.

## Pattern map (Arrays & Hashing first)
- Seen / duplicate check -> `set`
- Count frequencies / find pair sums -> `dict` (Two Sum = dict of value -> index)
- Group by something -> `defaultdict(list)`
- Two pointers on sorted input -> `l, r = 0, len(nums)-1` + while loop
