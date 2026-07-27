class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
    # UPI Method
    # Understand 
    # Given a 1-index array, we must return the indices of the two numbers that add up to the target 

    # regular arrays are 0-index, so we must increment the indices of the elements by 1, and return it as a list

      

        # for i in range(len(numbers)):
        #     if nums[i] not in my_dict:
        #         my_dict[i] = i
    # Brute Force:
        # 2D arrary:
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             indices.append(i + 1)
        #             indices.append(j + 1)
        # return indices
            # loop through it once starting at the first element
            # loop througbh it again, starting at the second number
        # check to see if the values at both indices equal the target
        # if so, we increment both indices by 1, and return it as a list

    # Plan:
    # Two Pointer Technique:
        # set my pointers of L and R at 0 and numbers - 1:
        # while left < right:
            # set a result for my answer at left + right
            # if my result is less than the target,:
                # increment my left pointer by 1
            # if my result is greater than target:
                # decrement right by 1:
            # else
                # return both pointers in a list [left + 1, right + 1]

        # Implement:
        left = 0
        right = len(numbers) - 1
        while left < right:
            curResult = numbers[left] + numbers[right]
            if curResult < target:
                left += 1    
            elif curResult > target:
                right -= 1
            else:
                return [left + 1, right + 1]
          
