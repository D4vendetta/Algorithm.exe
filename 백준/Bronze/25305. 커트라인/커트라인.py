N, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
result = data[k-1]
print(result)