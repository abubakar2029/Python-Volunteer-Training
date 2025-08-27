class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # array ko dictionary
        dic = {}
        for i in range(len(nums)): # O(N)
            dic[nums[i]] = i 

        # aak or scan ma second element find kr lo 
        for i in range(len(nums)): # O(N)
            y = target - nums[i]

            if y in dic and dic[y]!=i:
                return [dic[y],i]

        # O(N) + O(N)
        # 2 O(N)
        # O(N)
        return []