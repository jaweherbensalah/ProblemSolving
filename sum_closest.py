import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """nums: List[int]
        target: int
        rtype : int"""
        if len(nums)in [0,1,2]:
            return 0
        else:
            min_diff=sys.maxsize
            sorted_nums=sorted(nums)
            for i in range(len(nums)):
                start=i+1
                end=len(nums)-1

                while start<end:
                    curr_sum=sorted_nums[i]+sorted_nums[start]+sorted_nums[end]
                    diff= abs(curr_sum-target)
                    if diff==0:
                        return curr_sum
                    if diff<min_diff:
                        min_diff=f=diff
                        result=curr_sum
                    if curr_sum<=target:
                        start+=1
                    else:
                        end-=1

            return result
        


if __name__ == "__main__":
    soln=Solution()
    nums = [-1, 2, 1, -4]
    print(soln.threeSumClosest(nums, 1))
    print(soln.threeSumClosest(nums, 3))
    print(soln.threeSumClosest(nums, 0))




"""Second approach"""
import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """ nums: List[int]
            target: int
            rtype : int"""
        if len(nums)in [0,1,2]:
            return 0
        else:
            nums.sort()
            result = nums[0] + nums[1] + nums[2]
            for i in range(len(nums) - 2):
                left, right = i + 1, len(nums) - 1
                while left < right:
                    current_sum = nums[i] + nums[left] + nums[right]
                    if current_sum == target:
                        return current_sum
                    if abs(current_sum - target) < abs(result - target):
                        result = current_sum
                    if current_sum < target:
                        left += 1
                    else:
                        right -= 1
            return result
            


if __name__ == "__main__":
    soln=Solution()
    nums = [-1, 2, 1, -4]
    print(soln.threeSumClosest(nums, 1))
    print(soln.threeSumClosest(nums, 3))
    print(soln.threeSumClosest(nums, 0))

