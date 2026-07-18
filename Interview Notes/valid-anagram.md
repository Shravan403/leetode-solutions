# Interview Notes

## Pattern
- Hash Map (Dictionary)
- Frequency Counting

## Intuition
Anagrams contain the same characters with the same frequency, regardless of order.

## Approach
1. If the lengths are different, return `False`.
2. Store the frequency of each character from the first string in a dictionary.
3. Traverse the second string and decrease the corresponding frequency.
4. If any frequency becomes negative, return `False`.
5. If all checks pass, return `True`.

## Why Length Check?
Strings with different lengths can never be anagrams.

Example:
```
s = "ab"
t = "a"
```

Without the length check, leftover characters may never be detected.

## Complexity
- Time: **O(n)**
- Space: **O(n)**

## Alternative Solution
Sort both strings and compare.

```python
return sorted(s) == sorted(t)
```

- Time: **O(n log n)**
- Space: **O(n)**

## Interview Takeaways
- Frequency maps are a common interview pattern.
- Always handle edge cases before the main logic.
- `dict.get(key, 0)` simplifies frequency counting.
- Negative frequencies indicate the second string contains extra occurrences of a character.

## Related Problems
- 1. Two Sum
- 217. Contains Duplicate
- 383. Ransom Note
- 49. Group Anagrams
- 438. Find All Anagrams in a String
