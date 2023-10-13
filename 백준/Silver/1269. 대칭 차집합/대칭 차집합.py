import sys

N, M = map(int, sys.stdin.readline().split())

A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

C = set(A&B)

result_A = set(A-C)
result_B = set(B-C)

print(len(result_A) + len(result_B))