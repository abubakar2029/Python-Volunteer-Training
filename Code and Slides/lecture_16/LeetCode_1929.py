class Solution(object):
    def getConcatenation(self, nums):
    
        # ans = []

        # n = len(nums)
        # ans = [0]*(2*n)
        # for i in range(2*n):
        #     print(i)
        #     if(i>= n):
        #         ans[i]=nums[i-n]
        #     else:
        #         ans[i]=nums[i]
        # return ans

        # return nums+nums


        # nums = 1 2 1
        # 1 2 1 1  2  1    
        # for i in range(len(nums)):
        #     nums.append(nums[i])

        return nums*2
        