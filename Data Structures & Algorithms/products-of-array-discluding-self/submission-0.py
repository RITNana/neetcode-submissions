class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         # Implement:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        answer = [1] * n

        # build prefix: each element holds the product of everything to its LEFT 
        for i in range(1, n): # start at 2nd element, go to end of length of nums - 1
            prefix[i] = prefix[i - 1] * nums[i - 1] # start at 1, index 0 will be 1 on default 

        # build postfix: each eleement holds the product of everything to its RIGHT
        for i in range(n -2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        # build the answer - multiple out prefix and postfix at each index 
        for i in range(n):
            answer[i] = prefix[i] * postfix[i]
        return answer 

        # Time Complexity - O(n) because for each separate array that runs times (targeting the same nums array) we have n + n + n = O(n)

        # Space Complexity - O(n) because we initalize two arrays (output doesnt count for extra space) so n + n = O(2n) = O(n)