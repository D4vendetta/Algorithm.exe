import sys
step, dp = [], []

N = int(sys.stdin.readline())
for _ in range(N):
  step.append(int(sys.stdin.readline()))

dp.append(step[0])
if N >= 2:
  dp.append(max(step[0], step[0]+step[1]))
if N >= 3:
  dp.append(max(step[0]+step[2], step[1]+step[2]))
if N >= 4:
  for i in range(3, N):
    dp.append(max(dp[i-2]+step[i], dp[i-3]+step[i-1]+step[i]))
  
print(dp[-1])