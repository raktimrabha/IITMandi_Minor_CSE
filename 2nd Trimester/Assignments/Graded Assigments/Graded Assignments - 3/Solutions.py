'''____________________________________________________________________________________________'''
                                     GRADED ASSIGNMENT 3 
'''____________________________________________________________________________________________'''
#1 to 10

'''
1. d - O(2^n)
2. b - The algorithm can sometimes degrade to O(n^2) time
3. c - O(n^2)
4. b - [2, 3, 4, 5]
5. d - enqueue
6. b - Each node has only one pointer to the next node
7. b - Move one index forward, adding the new element and removing the trailing element
8. a - The array must be sorted
9. d - It leads to infinite recursion
10. c - Bubble Sort

'''



'''____________________________________________________________________________________________'''
#11 Solution



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





'''____________________________________________________________________________________________'''
#12 SOLUTION



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





'''____________________________________________________________________________________________'''
#13 SOLUTION



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





'''____________________________________________________________________________________________'''
#14 SOLUTION



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





'''____________________________________________________________________________________________'''
#15 SOLUTION



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





'''____________________________________________________________________________________________'''
#16 SOLUTION



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





'''____________________________________________________________________________________________'''
#17 SOLUTION



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





'''____________________________________________________________________________________________'''
#18 SOLUTION



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




'''____________________________________________________________________________________________'''
#19 SOLUTION



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





'''____________________________________________________________________________________________'''
#20 SOLUTION



def is_valid(x, y):
  return 1 <= x <= 10 and 1 <= y <= 10

def count_pos(x, y, n, visited):
  if n == 0:
    visited.add((x, y))
    return

  moves = [(-2, -1), (-2, 1), (-1,-2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

  for dx, dy in moves:
    nx, ny = x + dx, y + dy
    if is_valid(nx, ny):
      count_pos(nx, ny, n-1,visited)

def main():
  i, j, n = map(int, input().strip().split())
  visited = set()

  count_pos(i, j, n, visited)
  print(len(visited))

if __name__ == "__main__":
  main()





'''____________________________________________________________________________________________'''

