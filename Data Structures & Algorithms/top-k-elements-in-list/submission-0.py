class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         # UPI Method:

    # Understand - we are to return the elements that show up the most from our original array
    # [1, 1, 1, 2, 2, 3]
    # 1 is shown up three times (so we return 1)
    # 2 is shown up twice, (sp we return 2)

    # since k = 2, we return the two most frequent elements

    # Plan:
    # Store the number of occurences of each element into a table
        dict_table = {}
    # initialize a has table
    # initialize a variable called count
    # create a for loop that goes through each element in my list 
        for i in range(len(nums)):
        # check to see if element is in my hash table,
            dict_table[nums[i]] = 1 + dict_table.get(nums[i], 0)
        # if not, we add it to our table, and increase its value by 1
       
        
        arr = []
    # Create another loop to look at the values in my list:
        for num, freq in dict_table.items():  
            arr.append([freq, num])
        arr.sort()
        # sort the values from smallest to biggest
    # return said list

        results = []
    # Based on the length of k:
        while len(results) < k:
        # add the keys of the values
            results.append(arr.pop()[1]) 
        return results