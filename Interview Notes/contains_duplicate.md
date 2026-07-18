## Interview Notes

- Used a **HashSet (`set`)** to store visited elements.
- Checked if the current element already exists in the set before adding it.
- Returned `True` immediately upon finding a duplicate (early exit).
- If the loop completes, all elements are unique, so return `False`.
- Best choice when only **existence/uniqueness** needs to be checked.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

### Key Learning
- Use a **set** for fast membership checks.
- Use a **dictionary** only when frequency counting or key-value mapping is required.
