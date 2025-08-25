class Solution(object):
    def containsDuplicate(self, nums):

        # print("Before sorting : ", nums)
        nums.sort()
        # print("After sorting : ", nums)

        # print(len(nums))
        # for i in range(len(nums)): # range(4) -> 0 1 2 3
        #     # print(i)
        #     if i==0:
        #         continue
            
        #     if nums[i]==nums[i-1]:
        #         return True
            
        # return False

        # for i in range(len(nums)):
        #     print("value of i :",i)
        #     for j in range(i+1,len(nums)):
        #         print("value of j : ",j)
        #         if nums[i]==nums[j]:
        #             return True
        

        for i in range(len(nums)): # range(4) -> 0 1 2 3            
            if i>0 and nums[i]==nums[i-1]:
                return True

        return False
