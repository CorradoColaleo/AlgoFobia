def solution(arr):
    if not arr:
        return 0
    arr.sort(key=lambda x: x[0])
    n = len(arr)
    dp = [1] * n 
    for i in range(n):
        for j in range(i):
            if arr[i][1] > arr[j][1]:  
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) 

print(solution([(2, 6), (3, 7), (5, 4), (8, 3)]))  
print(solution([(2,1),(3,2),(4,10),(5,7),(9,4),(12,3)]))
