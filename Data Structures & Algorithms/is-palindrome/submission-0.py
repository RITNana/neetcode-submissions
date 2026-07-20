class Solution:
    def isPalindrome(self, s: str) -> bool:

        # UPI Method:

        # Understand

        # A string is a palindrome if it is the same going forward and going backward
        # raceacar is NOT one as going forward (race-) is different from going backward (raca-)
        # if a string is empty, it will automatically be a palindrome

        # Plan

        # convert any letters in my string to lower case 
        # remove whitespace in string
        # check to see if string is alphanumeric 

        # initialize a left and right pointer
        # while left_p is less than right_p
            # check to see if the values at each pointer are the same
            # if so we incrememt left pointer and decrement right pointer
            # return True
        # if not, we will return False 

        # Implement:
        # convert any letters in my string to lower case 
        lower_s = s.lower()
        # remove whitespace in string
        new_s = ''.join(char for char in lower_s if char.isalnum())

        # check to see if string is alphanumeric 
        
        left_pointer = 0
        right_pointer = len(new_s) - 1

        while(left_pointer < right_pointer):
                
                if new_s[left_pointer] == new_s[right_pointer]:
                    left_pointer += 1
                    right_pointer -= 1
                else:
                    return False
        return True

        # initialize a left and right pointer
        # while left_p is less than right_p
            # check to see if the values at each pointer are the same
            # if so we incrememt left pointer and decrement right pointer
            # return True
        # if not, we will return False 

        # Time Complexity: O(n) n = length of my strign and im comparing every single character from one pointer to the other
        # Space Complexity: O(n)

        