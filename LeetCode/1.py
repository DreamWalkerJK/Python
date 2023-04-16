# 1.两数之和

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2) 3036ms
        # for a in range(0, len(nums)-1):
        #     for b in range(a+1, len(nums)):
        #         if target == nums[a] + nums[b]:
        #             result = [a,b]
        #             break
        # else:
        #     return result

        # O(n) 692ms
        # temp = nums[:]
        # result = []
        # for a in range(0,len(nums)):
        #     other = target - nums[a]
        #     temp[a] = 10**9 -1
        #     try:
        #         b = temp.index(other)
        #     except ValueError as err:
        #         continue
        #     else:
        #         result = [a,b]
        #         break
        #     finally:
        #         temp[a] = nums[a]
        # return result
        
        # O(n) 44ms
        dict = {}
        result = []
        for a in range(0, len(nums)):
            other = target - nums[a]
            if other in dict:
                result = [dict[other], a]
                break
            else:
                dict[nums[a]] = a
        return result

nums = [3,3]
target = 6

res = Solution().twoSum(nums, target)
print(res)
