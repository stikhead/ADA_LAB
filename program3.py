import random
from typing import List, Tuple

def findKthLargest(nums: List[int], k: int) -> int:
    def partition(left: int, right: int, pivot_index: int) -> int:
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
                
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    def quickselect(left: int, right: int, k_smallest: int) -> int:
        if left == right:
            return nums[left]
            
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)
        
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        else:
            return quickselect(pivot_index + 1, right, k_smallest)

    return quickselect(0, len(nums) - 1, len(nums) - k)


def findMinMax(nums: List[int]) -> Tuple[int, int]:

    if not nums:
        raise ValueError("Array cannot be empty")

    def divide_and_conquer(left: int, right: int) -> Tuple[int, int]:
        if left == right:
            return nums[left], nums[left]
            
        if right == left + 1:
            if nums[left] < nums[right]:
                return nums[left], nums[right]
            else:
                return nums[right], nums[left]
                
        mid = (left + right) // 2
        left_min, left_max = divide_and_conquer(left, mid)
        right_min, right_max = divide_and_conquer(mid + 1, right)
        
        return min(left_min, right_min), max(left_max, right_max)

    return divide_and_conquer(0, len(nums) - 1)

if __name__ == "__main__":
    test_array = [3, 2, 1, 5, 6, 4]
    
    kth_largest = findKthLargest(test_array.copy(), 2) 
    print(f"2nd Largest: {kth_largest}")
    
    min_max = findMinMax(test_array)
    print(f"Min and Max: {min_max}")