def searchInsert(nums, target):
    if target in nums: return nums.index(target)
    index = 0
    for num in nums:
        if num < target: index += 1
        else: break
    return index