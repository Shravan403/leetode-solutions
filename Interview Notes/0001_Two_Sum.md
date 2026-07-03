- Compare every pair.
- Time Complexity: O(n²)
- Space Complexity: O(1)

Optimal:
- Use a dictionary to store:
  Number → Index

Algorithm:
1. Create an empty dictionary.
2. Loop through the array.
3. Calculate remaining = target - current number.
4. If remaining is already in the dictionary:
      return both indices.
5. Otherwise store current number and index.

Time Complexity:
O(n)

Space Complexity:
O(n)

Interview Learning:
Always ask:
"What number do I need?"

Instead of:
"Which pair should I search?"
