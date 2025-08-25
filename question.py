class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]
        
    
# a = Solution()
# a.twoSum([3,2,4],6)

# for i in range(2,4):
#     print (i)


from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return nums

s = Solution()

# print(s.buildArray([1,2,3]))   # ✅ works
# print(s.buildArray("abc"))     # ❌ logically wrong, but still runs!


with open("Code and Slides/lecture_16/a.txt", "w") as f:
    print(f.write("I changed the text at 8:54 am"))

