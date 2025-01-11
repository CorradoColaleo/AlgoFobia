def solution(nums, operations):
    dp1 = [0] * len(nums)
    dp2 = [0] * len(nums)

    # Gestione dei casi base
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        if operations[0] == "*":
            return nums[0] * nums[1]
        else:
            return nums[0] + nums[1]

    # Inizializzazione
    dp1[-1] = nums[-1]
    dp2[-1] = nums[-1]
    if operations[-1] == "*":
        dp1[-2] = nums[-2] * nums[-1]
        dp2[-2] = nums[-2] * nums[-1]
    else:
        dp1[-2] = nums[-2] + nums[-1]
        dp2[-2] = nums[-2] + nums[-1]


    # Ciclo per ottenere il massimo valore
    for i in range(len(nums) - 3, -1, -1):
        if operations[i] == "*":
            dp1[i] = nums[i] * dp1[i + 1]
        else:
            dp1[i] = nums[i] + dp1[i + 1]
        temp = nums[i]
        for j in range(i + 1, len(nums)):
            if operations[j - 1] == "*":
                temp *= nums[j]
            else:
                temp += nums[j]
            if j + 1 < len(nums):
                dp1[i] = max(dp1[i], temp * dp1[j + 1] if operations[j] == "*" else temp + dp1[j + 1])
            else:
                dp1[i] = max(dp1[i], temp)
    
    # Ciclo per ottenere il minimo valore
    for i in range(len(nums) - 3, -1, -1):
        if operations[i] == "*":
            dp2[i] = nums[i] * dp2[i + 1]
        else:
            dp2[i] = nums[i] + dp2[i + 1]
        temp = nums[i]
        for j in range(i + 1, len(nums)):
            if operations[j - 1] == "*":
                temp *= nums[j]
            else:
                temp += nums[j]
            if j + 1 < len(nums):
                dp2[i] = min(dp2[i], temp * dp2[j + 1] if operations[j] == "*" else temp + dp2[j + 1])
            else:
                dp2[i] = min(dp2[i], temp)

    return dp1[0],dp2[0]


if __name__ == "__main__":
    nums = [2,4,2,3,7]
    operations = ["+","*","*","+"]
    print(solution(nums,operations))

    nums = [3,14,19,3,10]
    operations = ["*","+","+","*"]
    print(solution(nums,operations))
