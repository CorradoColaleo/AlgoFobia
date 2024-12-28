def max_channels(X, Y, N):
    if N == 0 or N == 1:
        return N

    memoX = {X[i]: i for i in range(N)}
    memoY = {Y[i]: i for i in range(N)}

    X.sort()
    Y.sort()

    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if memoX[X[i - 1]] == memoY[Y[j - 1]]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[N][N]


if __name__ == "__main__":
    
    X = [2,5,3,8]
    Y = [6,4,7,3]
    N = 4
    print(max_channels(X, Y, N))

    Z = [2,5,3,9,12,4]
    W = [1,7,2,4,3,10]
    M = 6
    print(max_channels(Z, W, M))