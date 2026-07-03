# 13. Roman to Integer

## Problem
Convert a Roman numeral into its corresponding integer.

---

## Approach

1. Create a dictionary containing Roman symbols and their values.
2. Traverse the string from left to right.
3. Compare the current Roman numeral with the next one.
4. If the current value is smaller than the next value:
   - Subtract the current value.
5. Otherwise:
   - Add the current value.
6. Return the final answer.

---

## Time Complexity
O(n)

## Space Complexity
O(1)

---

## Python Solution

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        number = 0

        for i in range(len(s)):
            if i < len(s)-1 and roman[s[i]] < roman[s[i+1]]:
                number -= roman[s[i]]
            else:
                number += roman[s[i]]

        return number
```
