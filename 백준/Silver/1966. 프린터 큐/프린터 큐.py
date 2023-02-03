from collections import deque
Testcase = int(input())

#문서의 개수 = N, 찾는 문서의 현 순서 = key
for _ in range(Testcase):
    N, key = map(int, input().split())
    arr = deque(map(int, input().split()))
    count = 0

    if len(arr) == 1 :
            print(1)
            continue

    while True:
        if arr[0] != max(arr) :
            arr.append(arr.popleft())
            if key == 0:
                key = len(arr)-1
            else : key -= 1
        else :
            if key == 0:
                    print(f"{count+1}")
                    break
            arr.popleft()
            key-= 1
            count += 1