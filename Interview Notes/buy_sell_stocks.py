## 📝 Interview Notes

### Pattern
- Running Minimum + Greedy

### Key Idea
- Keep track of the minimum buying price seen so far.
- For every new price, calculate the profit if sold today.
- Update the maximum profit whenever a better profit is found.

### Algorithm
1. Initialize:
   - `buy = prices[0]`
   - `max_profit = 0`
2. Traverse the array once.
3. If the current price is lower than `buy`, update `buy`.
4. Otherwise, compute `current_profit = price - buy`.
5. Update `max_profit = max(max_profit, current_profit)`.
6. Return `max_profit`.

### Why It Works
- Buying at the lowest price seen before the current day always gives the best possible profit for selling on the current day.
- A single pass guarantees the optimal answer.

### Complexity
- **Time:** O(n)
- **Space:** O(1)

### Common Interview Follow-ups
- Why not use `max(prices) - min(prices)`?
  - Because the maximum price may occur **before** the minimum price, violating the rule that buying must happen before selling.
- Can this be solved in one pass?
  - Yes. Track the running minimum and update the maximum profit simultaneously.
- What if prices are always decreasing?
  - No profitable transaction exists, so return `0`.

### Takeaway
- Whenever a problem asks for the **maximum difference while preserving order**, think of maintaining a **running minimum** and updating the answer in one pass.
