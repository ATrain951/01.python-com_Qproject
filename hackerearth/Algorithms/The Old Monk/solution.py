"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().strip().split()))
    b = list(map(int, sys.stdin.readline().strip().split()))
    if a[0] <= b[-1]:
        print(0)
        continue
    monkiness = 0
    i = 0
    for j in range(n):
        if j >= i and b[j] >= a[i]:
            monkiness = max(monkiness, j - i)
        else:
            i += 1
            if i == n:
                break
    print(monkiness)
