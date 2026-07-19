# 📝 Interview Notes

## Pattern
- Stack (LIFO)

## Key Idea
- Push every opening bracket onto the stack.
- When a closing bracket is encountered:
  - If the stack is empty → Invalid.
  - If the top of the stack doesn't match the corresponding opening bracket → Invalid.
  - Otherwise, pop the matching opening bracket.
- At the end, the stack must be empty for the string to be valid.

## Why Stack?
The most recently opened bracket must be closed first (Last-In, First-Out).

## Data Structures Used
- Stack (list)
- Hash Map (Dictionary) for bracket mapping

```python
pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}
```

## Complexity
- Time: O(n)
- Space: O(n)

## Common Mistakes
- Forgetting to check if the stack is empty before accessing `stack[-1]`.
- Forgetting to pop after finding a valid pair.
- Returning `True` without checking if the stack is empty at the end.
- Writing multiple `if-elif` statements instead of using a dictionary.

## Interview Follow-up
- Can this be solved without a stack?
  - No. Nested brackets require remembering the most recent unmatched opening bracket, making a stack the appropriate data structure.

## Pattern Recognition
Keywords that indicate a Stack problem:
- Matching pairs
- Nested structures
- Balanced brackets
- Most recent element
- Undo / Backtracking
- Expression evaluation
