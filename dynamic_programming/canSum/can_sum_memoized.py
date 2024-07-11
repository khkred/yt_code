def canSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    
    # Check if targetSum is already in memo
    if targetSum in memo:
        return memo[targetSum]
    
    # Base cases
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    
    for num in numbers:
        remainder = targetSum - num
        
        # Check if the remainder can sum to the target
        if canSum(remainder, numbers, memo):
            memo[targetSum] = True
            return True
    
    # If no combination found, store the result as False
    memo[targetSum] = False
    return False


print(canSum(7,[3,4]))
print(canSum(7,[2,4]))