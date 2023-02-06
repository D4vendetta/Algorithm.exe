from bisect import bisect_left, bisect_right
import sys

N = int(input())
arr_A = list(map(int,sys.stdin.readline().split()))
M = int(input())
arr_X = list(map(int,sys.stdin.readline().split()))

arr_A.sort()

for i in arr_X:
    print(bisect_right(arr_A, i) - bisect_left(arr_A, i), end = " ")