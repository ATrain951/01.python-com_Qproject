"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from bisect import bisect_right

n, k = map(int, input().strip().split())
stones = list(map(int, input().strip().split()))
stones.sort()
total = 0
for i in range(n):
    for j in range(i + 1, n):
        x = k / (stones[i] * stones[j])
        if x >= stones[j]:
            index = bisect_right(stones, x)
            if index == n or stones[index] > x:
                index -= 1
            total += index - j
        else:
            break
print(total)
