# Given an integer array nums, return true if any value appears at least twice in the array, and
# return false if every element is distinct.


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # Set way
    """ numset = set(nums)

        if len(numset) == len(nums):
            return False
        return True """

    # Hashmap way
    dict = {}
    for num in nums:
        if num in dict:
            return True
        dict[num] = 0
    return False
