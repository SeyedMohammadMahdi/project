import time
import random


def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + equal + quick_sort(right)


arrays = []

for _ in range(10):
    size = random.randint(10, 30)
    new_array = [random.randint(1, 100) for _ in range(size)] 
    arrays.append(new_array)

print("sampleNo        bubble sort        merge sort        quick sort")


for i, arr in enumerate(arrays):

    bubble_sort_start = time.time()
    bubble_sort(arr)
    bubble_sort_end = time.time()

    merge_sort_start = time.time()
    merge_sort(arr)
    merge_sort_end = time.time()

    quick_sort_start = time.time()
    quick_sort(arr)
    quick_sort_end = time.time()

    print(f"{i+1}        {bubble_sort_end - bubble_sort_start}        {merge_sort_end - merge_sort_start}        {quick_sort_end - quick_sort_start}")
