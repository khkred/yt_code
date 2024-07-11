def cansum(targetSum, numbers):
    if targetSum == 0:
        return True
    
    if targetSum < 0:
        return False
    
    for num in numbers:
        remainder = targetSum - num
        if cansum(remainder, numbers):
            return True
           
    return False

print(cansum(7, [2, 4]))
