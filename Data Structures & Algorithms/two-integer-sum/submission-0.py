# We wish to return the indices of nums array at i and j, based on the target value
# we're told every inpit has one pair of index for i and j 

# Easy Way:
    # We can loop through the nums array in a 2D - for loop
    # We go through all the indices for i
    # we loop through all the indices for j
        # if i != j
        # set nums[i] and nums[j] to be given the value of target
        # return nums[i] and nums[j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                        return [i, j]
        