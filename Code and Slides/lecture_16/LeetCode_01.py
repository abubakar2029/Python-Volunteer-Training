class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            print("Value of i :",i)
            for j in range(i+1,len(nums)):
                print("Value of j : ",j)
                if(nums[i]+nums[j]==target):
                    return [i,j]
            # print("Wapis outer loop ma jae ga---")
        