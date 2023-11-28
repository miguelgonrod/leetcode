#!/usr/bin/env python3

class Solution:
    def __init__(self):
        self.left = 0
        self.right = 0

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        self.left = 0
        self.right = len(nums)-1
        result = [0,0]
        while self.left < self.right:
            current_sum = nums[self.left] + nums[self.right]
            result[0] = self.left
            result[1] = self.right

            if (current_sum == target):
                return result

            else:
                self.left += 1

        return self.twoSum(nums[:-1], target)

            
        

if __name__ == "__main__":
    solucion = Solution()
    print(solucion.twoSum([2,7,11,15], 9))
    print(solucion.twoSum([3,2,4], 6))
    print(solucion.twoSum([3,3], 6))
