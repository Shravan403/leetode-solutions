# Problem 002 - Palindrome Number

Difficulty:
Easy

Pattern:
Digit Manipulation

Problem Statement:
Return True if the given integer reads the same forwards and backwards; otherwise return False.

--------------------------------------------------

Brute Force Idea:

1. Store the original number.
2. Reverse the number mathematically.
3. Compare the reversed number with the original number.
4. Return the result.

--------------------------------------------------

Algorithm:

1. original = x
2. reverse = 0
3. While x > 0
      digit = x % 10
      reverse = reverse * 10 + digit
      x = x // 10
4. return original == reverse

--------------------------------------------------

Important Concepts Learned:

1. % 10
   → Gives the last digit.

Example:
123 % 10 = 3

--------------------------------------------

2. // 10
   → Removes the last digit.

Example:
123 // 10 = 12

--------------------------------------------

3. reverse = reverse * 10 + digit

Purpose:
Shift all digits left by one place and append the new digit.

Example:

reverse = 47
digit = 8

47 × 10 = 470

470 + 8 = 478

--------------------------------------------

Time Complexity:

O(log₁₀ n)

Reason:
We process each digit exactly once.

--------------------------------------------

Space Complexity:

O(1)

No extra data structures are used.

--------------------------------------------------

Edge Cases:

Negative Numbers

Input:
-121

Output:
False

Reason:
Negative numbers cannot be palindromes.

--------------------------------------------

Zero

Input:
0

Output:
True

Reason:
0 reversed is still 0.

--------------------------------------------

Trailing Zero

Input:
10

Output:
False

Reason:
Reverse becomes 1.

--------------------------------------------------

Mistakes I Made:

1. Forgot to remove the last digit using // 10.

2. Tried returning x instead of comparing
   original and reverse.

3. Initially thought the while condition
   needed to change for negative numbers.

--------------------------------------------------

Interview Questions:

Q1.
Why do we use % 10?

Answer:
To extract the last digit.

--------------------------------------------

Q2.
Why do we use // 10?

Answer:
To remove the last digit.

--------------------------------------------

Q3.
Why multiply reverse by 10?

Answer:
To shift digits left before adding the new digit.

--------------------------------------------

Q4.
Why store original?

Answer:
Because x changes during the loop.

We need the original value for comparison.

--------------------------------------------

Q5.
Can this solution be optimized?

Answer:
Yes.

Instead of reversing the whole number,
we can reverse only half of it,
reducing unnecessary operations.

--------------------------------------------------

Interview Learning:

Whenever a problem involves digits,
immediately think:

Last Digit
→ % 10

Remove Last Digit
→ // 10

Build New Number
→ reverse = reverse * 10 + digit

--------------------------------------------------

Pattern Learned:

Digit Manipulation
