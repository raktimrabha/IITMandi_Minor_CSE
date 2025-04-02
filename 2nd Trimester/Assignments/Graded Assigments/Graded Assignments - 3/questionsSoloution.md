### GRADED ASSIGNMENT 3

Solutions from Q:1 to Q:10

---

#### Q: 1

Which time complexity describes an algorithm whose running time doubles with each additional input element?

- O(1)
- O(log n)
- O(n)
- O(2^n)

**Answer:** d - O(2^n)

---

#### Q: 2

If an algorithm’s average-case time complexity is O(n), but the worst-case time complexity is O(n^2), which statement is generally true?

- The algorithm always runs in O(n) time.
- The algorithm can sometimes degrade to O(n^2) time.
- The algorithm never exceeds O(n) time.
- The average-case complexity is unimportant in practical use.

**Answer:** b - The algorithm can sometimes degrade to O(n^2) time

---

#### Q: 3

What is the time complexity of the Selection Sort algorithm in the worst case?

- O(n)
- O(n log n)
- O(n^2)
- O(log n)

**Answer:** c - O(n^2)

---

#### Q: 4

Consider the following Python code snippet:

```python
arr = [5, 2, 4, 3]
for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
```

What will be the output after the code executes?

- `[5, 2, 4, 3]`
- `[2, 3, 4, 5]`
- `[4, 3, 2, 5]`
- `[2, 4, 3, 5]`

**Answer:** b - `[2, 3, 4, 5]`

---

#### Q: 5

Which operation is typically not associated with a stack?

- push
- pop
- top (or peek)
- enqueue

**Answer:** d - enqueue

---

#### Q: 6

Which statement best describes a singly linked list?

- Each node has two pointers: one to the next node and one to the previous node.
- Each node has only one pointer to the next node.
- Each node contains a pointer that references the node before it.
- Nodes are stored contiguously in memory.

**Answer:** b - Each node has only one pointer to the next node

---

#### Q: 7

When using the sliding window technique to find the maximum sum of any subarray of length k in an array, how do you typically move the window?

- Increase the window size by 1 each time.
- Move one index forward, adding the new element and removing the trailing element.
- Jump k elements forward each time.
- Re-compute the sum from scratch for each new window.

**Answer:** b - Move one index forward, adding the new element and removing the trailing element

---

### Q: 8

**What is the main requirement for using a standard binary search on an array?**

- The array must be sorted.
- The array must be of even length.
- The array must contain unique elements.
- The array must contain integer values only.

**Answer:** a - The array must be sorted

---

### Q: 9

**What happens in a recursive function when it does not have a valid base case?**

- It returns zero.
- It returns None.
- It will run in constant time.
- It leads to infinite recursion.

**Answer:** d - It leads to infinite recursion

---

### Q: 10

**Which of the following sorting algorithms is not considered a “divide-and-conquer” algorithm?**

- Merge Sort
- Quick Sort
- Bubble Sort
- All of the above are divide-and-conquer

**Answer:** c - Bubble Sort

---

### Q: 11

**Merge Sorted Arrays**

#### Description

You are given two sorted arrays, `A` and `B`. Your task is to merge these arrays into one sorted array and print the resulting array.

#### Input Description

- The first line contains a single integer `n`, the size of array `A`.
- The second line contains `n` integers, the elements of array `A` (sorted in non-decreasing order).
- The third line contains a single integer `m`, the size of array `B`.
- The fourth line contains `m` integers, the elements of array `B` (sorted in non-decreasing order).

#### Output Description

Print the merged array of size `n + m` in non-decreasing order.

#### Constraints

- \(1 \leq n, m \leq 10^5\)
- \(-10^9 \leq A[i], B[j] \leq 10^9\)
- Both arrays are sorted in non-decreasing order.

#### Sample Input 1:

```
4  
1 3 5 7  
5  
2 4 6 8 9  
```

#### Sample Output 1:

```
1 2 3 4 5 6 7 8 9
```

#### Solution:

```python
def merged_sorted(A, B):
    i, j, merged = 0, 0, []

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1

    while i < len(A):
        merged.append(A[i])
        i += 1

    while j < len(B):
        merged.append(B[j])
        j += 1

    print(*merged)

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

merged_sorted(A, B)
```

---

### Q: 12

**Opp Merge Sort**

#### Description

Given a list of `n` integers, write a program for the merge sort algorithm such that it reverses the list in descending order. You must not write any other sorting algorithm.

#### Input Description

- The first line contains `n`, which is the number of elements present in the array.
- The second line contains `n` space-separated integers.

#### Output Description

Output the elements present in the array sorted in descending order.

#### Sample Input 1:

```
5
2 3 1 4 5
```

#### Sample Output 1:

```
5 4 3 2 1
```

#### Solution:

```python
def m_sort_d(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = m_sort_d(arr[:mid])
    right = m_sort_d(arr[mid:])

    return m_desc(left, right)

def m_desc(left, right):
    i, j = 0, 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

n = int(input())
arr = list(map(int, input().split()))

sorted_arr = m_sort_d(arr)
print(*sorted_arr)
```

### Q:13 - Mr Robot - Elliot

#### Description
Mr. Robot needs an encryption method, so Elliott was there to help him. At the same time, Richard wrote a paper on encryption. Elliott then started writing his algorithms with the help of Richard's paper but needs your help in implementing it. The algorithm is as follows:

Given an input string, the encrypted string will start with the middle character of the string and will be formed henceforth with the middle characters of the left and right substrings (of the middle character of the word) and so on. Refer to the explanation of the sample test case for better understanding.

#### Input Description
- **Input Format**:
    - The first line contains an integer `T` denoting the number of test cases.
    - Each test case consists of 2 lines:
        - The first line contains an integer `N` denoting the length of the word that needs to be encrypted.
        - The second line contains the word that needs to be encrypted.

#### Constraints
- \(1 \leq T \leq 10\)
- \(1 \leq \text{Length of the string} \leq 10000\)

#### Output Description
- Print `N` lines where each line will contain the encrypted words.

#### Sample Input 1
```
3
3
abc
4
abcd
11
abcdefghijk
```

#### Sample Output 1
```
bac
bacd
fcabdeighjk
```

#### Hint
For `abc`, initially, `ans` is `""`:
1. Middle character for `abc` is `b`, so the answer becomes `"b"`, and strings are `a` and `c`.
2. Now the middle character of the string `"a"` is `a`, so the answer becomes `"ba"`.
3. Now the middle character of the string `"c"` is `c`, so the answer becomes `"bac"`.

#### Solution
```python
def encrypt(s):
        if not s:
                return ""
        mid = len(s) // 2
        if len(s) % 2 == 0:
                mid -= 1
        return s[mid] + encrypt(s[:mid]) + encrypt(s[mid + 1:])

T = int(input())
for _ in range(T):
        N = int(input())
        word = input().strip()
        en_word = encrypt(word)
        print(en_word)
```

---

### Q:14 - Average Chocolates

#### Description
Vishal asked his mother to buy a pack of chocolates for him. She agreed but on one condition: Vishal has to solve one question. If he answers correctly, he will be given all the chocolates.

Vishal has `N` friends. Each friend has some chocolates with them, given in an array `A`. There are `Q` queries. Each query contains an integer `K`. He has to choose a subset `S` from the given array `A` such that the average of `S` is less than `K`.

He has to print the maximum possible length of `S`.

#### Input Description
- **Input Format**:
    - The first line contains `N`, the length of array `A`.
    - The next line contains `N` space-separated elements of array `A`.
    - The next line contains an integer `Q`, the number of queries.
    - Each of the following `Q` lines contains a single integer `K`.

#### Constraints
- \(1 \leq N \leq 10^5\)
- \(1 \leq Q \leq 5 \times 10^5\)
- \(1 \leq A[i], K \leq 10^9\)

#### Output Description
- For each query, print a single integer denoting the maximum possible length of the subset.

#### Sample Input 1
```
5
1 2 3 4 5
5
1
2
3
4
5
```

#### Sample Output 1
```
0
2
4
5
5
```

#### Hint
**Output Explanation**:
- In the first query, there is no possible subset such that its average is less than `1`.
- In the second query, you can select the subset `{1, 2}`.
- In the third query, you can select the subset `{1, 2, 3, 4}`.
- In the fourth and fifth queries, you can select the complete array `{1, 2, 3, 4, 5}`.

#### Solution
```python
import sys

def solve():
        input = sys.stdin.read().split()
        ptr = 0
        N = int(input[ptr]); ptr += 1
        A = list(map(int, input[ptr:ptr+N])); ptr += N
        Q = int(input[ptr]); ptr += 1
        queries = list(map(int, input[ptr:ptr+Q]))

        A.sort()
        prefix = [0] * (N + 1)
        for i in range(N):
                prefix[i+1] = prefix[i] + A[i]

        for K in queries:
                low, high, best = 0, N, 0
                while low <= high:
                        mid = (low + high) // 2
                        if mid == 0:
                                avg = 0
                        else:
                                avg = prefix[mid] / mid
                        if avg < K:
                                best = mid
                                low = mid + 1
                        else:
                                high = mid - 1
                print(best)

solve()
```

```markdown
## Q:15 - Signal's Capacity

### Description

There are many signal towers present in Bangalore. Towers are aligned in a straight horizontal line (from left to right), and each tower transmits a signal in the right-to-left direction.

Tower X shall block the signal of Tower Y if Tower X is present to the left of Tower Y and Tower X is taller than Tower Y. So, the power of a signal of a given tower can be defined as:

> **(The number of contiguous towers just to the left of the given tower whose height is less than or equal to the height of the given tower) + 1.**

You need to write a program that finds the power of each tower.

---

### Input Description

- **Input Format**:
    - Each test case has multiple test cases in it:
        - First line contains an integer specifying the number of test cases.
        - Second line contains an integer `n` specifying the number of towers.
        - Third line contains `n` space-separated integers `H[i]` denoting the height of each tower.

- **Constraints**:
    - \(1 \leq T \leq 10\)
    - \(2 \leq n \leq 10^6\)
    - \(1 \leq H[i] \leq 10^8\)

---

### Output Description

- **Output Format**:
    - Print the range of each tower (separated by a space).

---

### Sample Input 1:
```
2
7
100 80 60 70 60 75 85
5
3 5 0 9 8
``

### Sample Output 1:
```
1 1 1 2 1 4 6
1 2 1 4 1
```

---

### Hint

**Sample 1 Explanation**:
- There are 2 test cases:
    - In the first test case:
        - 7 towers are present, and the signal range of each tower separated by space is: `1 1 1 2 1 4 6`.
    - In the second test case:
        - 5 towers are present, and the signal range of each tower separated by space is: `1 2 1 4 1`.

---

### Solution:
```python
def signal_capacity(n, heights):
        stack = []
        result = [0] * n

        for i in range(n):
                while stack and stack[-1][1] <= heights[i]:
                        stack.pop()
                result[i] = (i - stack[-1][0]) if stack else (i + 1)
                stack.append((i, heights[i]))

        return result

t = int(input())
for _ in range(t):
        n = int(input())
        heights = list(map(int, input().split()))
        print(*signal_capacity(n, heights))
```

---

## Q:16 - Sort Colors

### Description

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

---

### Input Description

- **Input Format**:
    - First line has an integer `N` (size of array).
    - Next line has `N` integers.

- **Constraints**:
    - \(1 \leq N \leq 10^5\)
    - \( \text{Arr}[i] \) is `0`, `1`, or `2`.

---

### Output Description

- Print the final array after sorting.

---

### Sample Input 1:
```
6
2 0 2 1 1 0
```

### Sample Output 1:
```
0 0 1 1 2 2
```

---

### Solution:
```python
def sort_colors(nums):
        n = len(nums)

        index = 0
        for i in range(n):
                if nums[i] == 0:
                        nums[i], nums[index] = nums[index], nums[i]
                        index += 1

        index = n - 1
        for i in range(n - 1, -1, -1):
                if nums[i] == 2:
                        nums[i], nums[index] = nums[index], nums[i]
                        index -= 1

N = int(input())
nums = list(map(int, input().split()))

sort_colors(nums)
print(*nums)
```

---

## Q:17 - Fill Gaps

### Description

You are given a sorted linked list containing unique values. You have to manipulate the linked list such that the difference between every two adjacent node values should be exactly equal to `1`. You can only insert some extra nodes between existing nodes in the linked list.

---

### Input Description

- **Input Format**:
    - The first line of input contains the integer `N` denoting the number of elements of the linked list.
    - The second line contains the elements of the linked list.

- **Function Description**:
    - `fillGaps(head)`:
        - Arguments:
            - `head`: Head node of the LinkedList.

- **Constraints**:
    - \(1 \leq N \leq 10^4\)
    - \(1 \leq \text{node.val} \leq 10^6\)

---

### Output Description

- Return the head of the modified linked list.

---

### Sample Input 1:
```
3
4 7 8
```

### Sample Output 1:
```
4 5 6 7 8
```

### Sample Input 2:
```
5
2 5 8 9 11
```

### Sample Output 2:
```
2 3 4 5 6 7 8 9 10 11
```

---

### Hint

**Explanation of Sample 1**:
- The given linked list has elements `4` and `7`. We can insert nodes `5` and `6` between `4` and `7` to make a new LinkedList having a difference between every pair of adjacent nodes equal to `1`. So, the linked list becomes `4 -> 5 -> 6 -> 7`.

---

### Solution:
```python
class ListNode:
        def __init__(self, data):
                self.data = data
                self.next = None

def fillGaps(head):
        current = head
        while current and current.next:
                while current.next.data > current.data + 1:
                        new_node = ListNode(current.data + 1)
                        new_node.next = current.next
                        current.next = new_node
                current = current.next

        return head
```

```markdown
## Q:18 - Voco Sort

### Description

Given `N` strings each consisting of lowercase alphabets, sort the array using the following rule:

1. A string having a lesser sum of consonants and vowels should come first.
2. If two strings `X` and `Y` have an equal sum of consonants and vowels, then `X` and `Y` should be sorted in the same order as that of input.

---

### Input Description

- **Input Format**:
    - The first line contains a single integer `T` denoting the number of test cases.
    - For each test case:
        - The first line contains a single integer `N`.
        - The next `N` lines each consist of a string `S`.

- **Constraints**:
    - \(1 \leq T \leq 100\)
    - \(1 \leq N \leq 100\)

---

### Output Description

For each test case, print `N` strings, each in a new line, denoting the final sorted array.

---

### Sample Input 1:
``
1
4
aeaed
fha
cdf
ba
``

### Sample Output 1:
``
ba
fha
cdf
aeaed
``

---

### Hint

Given the test case:

- \(N = 4\)
- Given array `A`:
    - Let `C` denote the number of consonants while `V` denotes the number of vowels.

| String | Consonants (C) | Vowels (V) | C + V |
|--------|----------------|------------|-------|
| aeaed  | 1              | 4          | 5     |
| fha    | 2              | 1          | 3     |
| cdf    | 3              | 0          | 3     |
| ba     | 1              | 1          | 2     |

- Since the value of `C + V` is least for `"ba"`, it occurs at the beginning in the sorted array.
- Both `"cdf"` and `"fha"` have the same `C + V` values. Since `"fha"` occurs ahead of `"cdf"` in the original array `A`, `"fha"` comes ahead of `"cdf"` in the sorted array.
- `"aeaed"` has the largest `C + V` value, so it occurs at the last of array `A`.

---

### Solution:
```python
def main():
        import sys
        lines = sys.stdin.read().splitlines()
        ptr = 0
        T = int(lines[ptr])
        ptr += 1
        for _ in range(T):
                N = int(lines[ptr])
                ptr += 1
                strings = []
                for _ in range(N):
                        strings.append(lines[ptr].strip())
                        ptr += 1

                def compute(s):
                        vowels = {'a', 'e', 'i', 'o', 'u'}
                        v = 0
                        c = 0
                        for char in s:
                                if char in vowels:
                                        v += 1
                                else:
                                        c += 1
                        return c + v

                idx_str = [(compute(s), i, s) for i, s in enumerate(strings)]
                idx_str.sort(key=lambda x: (x[0], x[1]))

                s_str = [item[2] for item in idx_str]
                for s in s_str:
                        print(s)

if __name__ == "__main__":
        main()
```

---

## Q:19 - Generate Permutations

### Description

Given a collection of numbers, return all possible permutations.

- **NOTE**:
    - No two entries in the permutation sequence should be the same.
    - For the purpose of this problem, assume that all the numbers in the collection are unique.
    - **Using built-in library functions to permute will lead to disqualification.**

---

### Input Description

- **Input Format**:
    - The first line contains an integer `n` denoting the size of the array.
    - The next line contains `n` distinct integers \(A[1], A[2], \dots, A[N]\).

- **Constraints**:
    - \(1 \leq n \leq 6\)

---

### Output Description

Print the permutations of numbers in a new line separated by space. Ensure the permutations are printed in sorted order, i.e., `"1 2 3"` must come before `"2 3 1"`. Print without quotes.

---

### Sample Input 1:
```
3
1 2 3
```

### Sample Output 1:
```
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```

---

### Solution:
```python
def heap_permute(nums, size, result):
        if size == 1:
                result.append(" ".join(map(str, nums)))
                return

        for i in range(size):
                heap_permute(nums, size - 1, result)
                if size % 2 == 1:
                        nums[0], nums[size - 1] = nums[size - 1], nums[0]
                else:
                        nums[i], nums[size - 1] = nums[size - 1], nums[i]

def generate_permutations():
        N = int(input())
        nums = list(map(int, input().split()))
        nums.sort()
        result = []
        heap_permute(nums, N, result)
        print("\n".join(sorted(result)))

generate_permutations()
```

---

## Q:20 - Follow The Knight

### Description

You are very good at playing chess since childhood and know the rules very well. You have a `10 x 10` chessboard and want to explore all the possible squares on the board that the knight can be at in exactly `N` moves. It is placed at `(i, j)` coordinate initially. 

For a `10 x 10` chessboard:
- `(1, 1)` will be the top-left corner.
- `(10, 10)` will be the bottom-right corner.

The knight can move to any of the squares marked as `X` in 1 move.

---

### Input Description

- **Input Format**:
    - Input consists of three space-separated integers `i`, `j`, and `N`.

- **Constraints**:
    - \(N < 10\)

---

### Output Description

Print a single integer denoting the number of blocks on the chessboard that the knight can be at in exactly `N` moves.

---

### Sample Input 1:
```
3 3 1
```

### Sample Output 1:
```
8
```

---

### Solution:
```python
def is_valid(x, y):
        return 1 <= x <= 10 and 1 <= y <= 10

def count_pos(x, y, n, visited):
        if n == 0:
                visited.add((x, y))
                return

        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                        count_pos(nx, ny, n - 1, visited)

def main():
        i, j, n = map(int, input().strip().split())
        visited = set()

        count_pos(i, j, n, visited)
        print(len(visited))

if __name__ == "__main__":
        main()
```
```
