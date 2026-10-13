from typing import List

class Sort:
    def merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])
        
        return self._merge(left_half, right_half)
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted_array = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
                
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
        
        return sorted_array

    def quick_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
            
        pivot = arr[len(arr) // 2]
        
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return self.quick_sort(left) + middle + self.quick_sort(right)


if __name__ == "__main__":
    sorter = Sort()
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    arr2 = [10, 7, 8, 9, 1, 5]
    
    print(f"Original array 1: {arr1}")
    print(f"Merge Sort: {sorter.merge_sort(arr1)}")
    print("-" * 30)
    
    print(f"Original array 2: {arr2}")
    print(f"Quick Sort: {sorter.quick_sort(arr2)}")