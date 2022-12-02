def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_map = {}

    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in num_map:
            return [i, num_map.get(comp)]

        num_map[nums[i]] = i

    # Brute Force O(n^2)
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[j] == (target - nums[i]):
    #             return [i, j]


print(twoSum([3, 3, 4], 6))
