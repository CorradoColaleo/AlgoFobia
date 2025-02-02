import math 

class Solution:

    def wiggleSort(self, nums: list[int]) -> None:
        """
        This method takes an array 'nums' and reorders it in-place to a wiggle sort order.
        Where nums[0] < nums[1] > nums[2] < nums[3]...
        """
        # Sort the array to make it easier to find the median.
        sorted_nums = sorted(nums)
        length = len(sorted_nums)
        # Find the midpoints for the smaller and larger halves
        # If 'length' is odd, 'mid' is the exact middle, else it's just before the middle
        mid = (length - 1) // 2
        end = length - 1
      
        # Reorder the array by placing the largest element at the end and the next
        # largest at the beginning, then the second-largest at index 2, and so on.
        for index in range(length):
            if index % 2 == 0:
                # Even index gets the next element from the smaller half
                nums[index] = sorted_nums[mid]
                mid -= 1
            else:
                # Odd index gets the next element from the larger half
                nums[index] = sorted_nums[end]
                end -= 1
        # The array is now reordered in-place

        print(nums)

nums1 = [1,5,1,1,6,4]

nums2 = [1,3,2,2,3,1]

nums3 = [9, 4, 8, 6, 2, 7, 3, 5, 1, 10]

s = Solution()

s.wiggleSort(nums1)

s.wiggleSort(nums2)

s.wiggleSort(nums3)













        

