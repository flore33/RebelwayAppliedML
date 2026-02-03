def reverse_string(s):
    return s[::-1]

s = "hello"
#print("reverse_string(s):", reverse_string(s))




def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

#print("secondreverse_string(s):", reverse_string(s))




def sum_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total

arr = [1, 2, 3, 4, 5]
#print("sum_elements(arr):", sum_elements(arr))






def find_missing_number(arr, N):
    expected_sum = N * (N + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

arr = [1, 2, 4, 5]
N = 5
#print(find_missing_number(arr, N))  # Output: 3


s = "racecar"
def is_palindrome(s):
    return s == s[::-1]

#print(is_palindrome("racecar"))  # True
#print(is_palindrome("hello"))    # False

def merge_sorted_arrays(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
#print(merge_sorted_arrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

s = "hello"
#print(count_vowels(s))  # Output: 2

def find_largest_number(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num
arr = [1, 3, 5, 7, 2, 4, 6, 8]
#print(arr[0])


#print(find_largest_number(arr))  # Output: 8

def find_second_largest(arr):
    if len(arr) < 2:
        return None
    max_num = arr[0]
    min_num = arr[0]
    second_max = None
    second_min = None
    for num in arr:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num < min_num and (second_max is None or num > second_max):
            second_min = min_num
            min_num = num
        elif num > min_num and (second_min is None or num < second_min):
            second_min = num
    return second_max, second_min

arr = [1, 3, 5, 7, 2, 4, 6, 8]



#print(find_second_largest(arr))  # Output: 7, 2

def find_second_smallest(arr):
    if len(arr)<2:
        return None
    min_num = arr[0] 
    second_min = arr[0]
    for num in arr:
        if num < min_num:
            second_min = min_num
            min_num = num
        elif num > min_num and (second_min is None or num < second_min):
            second_min = num
    return second_min
arr = [15, 3, 5, 7, 2, 4, 6, 8]
#print(find_second_smallest(arr))  # Output: 2


def move_zeros_to_end (arr):
    non_zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[non_zero_index] = arr[non_zero_index], arr[i]
            non_zero_index += 1
    return arr
arr = [23, 0, 1, 0, 3, 12]
#print(move_zeros_to_end(arr))  # Output: [23, 1, 3, 12, 0, 0]



def move_zeros_and_sort_nonzeros(arr):
    non_zeros = sorted([x for x in arr if x != 0])
    zeros = [0] * (len(arr) - len(non_zeros))
    return non_zeros + zeros

arr = [23, 0, 1, 0, 3, 12]
#print(move_zeros_and_sort_nonzeros(arr))  # Output: [1, 3, 12, 23, 0, 0]



def sort_array_by_ascending(arr):
    return sorted(arr)
arr = [23, 0, 1, 0, 3, 12]
#print(sort_array_by_ascending(arr))  # Output: [0, 0, 1, 3, 12, 23]    



def find_the_smallest(arr):
    min_number = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_number:
            min_number = arr[i]
    return min_number

arr = [1, 3, 5, 7, 2, 4, 6, 8]
#print(find_the_smallest(arr))  # Output: 1

##better solution
def find_the_smallest(arr):
    min_number = arr[0]
    for num in arr:
        if num < min_number:
            min_number = num
    return min_number

arr = [1, 3, 5, 7, 2, 4, 6, 8]
#print(find_the_smallest(arr))  # Output: 1
##even better solution
def find_the_smallest(arr):
    return min(arr)
arr = [1, 3, 5, 7, 2, 4, 6, 8]
#print(find_the_smallest(arr))  # Output: 1

def find_the_largest(arr):
    return max(arr)
arr = [1, 3, 5, 7, 2, 4, 6, 8]
#print(find_the_largest(arr))  # Output: 8

def find_the_largest(arr):
    max_number = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_number:
            max_number = arr[i]
    return max_number
arr = [1, 3, 5, 7, 2, 4, 6, 8]
#print(find_the_largest(arr))  # Output: 8

def find_the_index_largest_num(arr):
    max_num = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            index = i
    return max_num, index

arr = [1, 3, 5, 7, 2, 4, 6, 8]
#print(find_the_index_largest_num(arr))  # Output: (8, 7)




def find_second_largest(arr):
    if len(arr) < 2:
        return None

    max_num = arr[0]
    second_max = None

    for num in arr:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num != max_num:  # Important to avoid duplicates
            if second_max is None or num > second_max:
                second_max = num

    return second_max



arr = [130, 6, 190, 2, 550]
#print(find_second_largest(arr))

def find_second_largest(arr):
    if len(arr) < 2:
        return None

    max_num = second_max = float('-inf')

    for num in arr:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num

    return second_max if second_max != float('-inf') else None

def find_third_largest(arr):
    if len(arr) < 3:
        return None
    #float('-inf') ensures any real number will be larger initially
    max_num = second_num = third_num = float('-inf')
    for num in arr:
        if num > max_num:
            third_num = second_num
            second_num = max_num
            max_num = num
        if num > second_num and num != max_num:
            second_num = num
        elif num > third_num and num != max_num and num != second_num:
            third_num = num

    return third_num if third_num != float('-inf') else None

arr = [2, 3, 4, 5, 6, 7]
#print(find_third_largest(arr))

def find_nth_largest(arr, n):
    unique_nums = list(set(arr))          # Remove duplicates
    if len(unique_nums) < n:
        return None                       # Not enough unique numbers
    unique_nums.sort(reverse=True)        # Sort descending
    return unique_nums[n - 1]             # n-th largest is at index n-1

import heapq

def find_nth_largest_heap(arr, n):
    unique_nums = list(set(arr))
    if len(unique_nums) < n:
        return None
    return heapq.nlargest(n, unique_nums)[-1]


#arr = arr = [2, 333, 144, 5, 56, 7]
#print(find_nth_largest_heap(arr, 3))

def find_the_nth_smallest(arr,n):
    unique_nums = list(set(arr))
    if len(unique_nums) < n :
        return None
    unique_num_sorted = sorted(unique_nums)
    return unique_num_sorted[n - 1]

arr = [2, 3, 56, 345, 9, 2, 7,8,9]
#print(find_the_nth_smallest(arr,2))

arr = [1]
#print(find_the_nth_smallest(arr,2))

def find_the_nth_smallest(arr,n):
    unique_nums = list(set(arr))
    if len(unique_nums) < n :
        return None
    return heapq.nsmallest(n,unique_nums)[-1]

arr = [1]
#print(find_the_nth_smallest(arr,2))

arr = [2, 3, 56, 345, 9, 2, 7,8,9]
#print(find_the_nth_smallest(arr,2))


def find_nth_smallest_with_duplicate(arr, n):
    if len(arr) < n:
        return None, []

    sorted_arr = sorted(arr)  # Keep duplicates
    nth_smallest = sorted_arr[n - 1]

    # Find all occurrences of nth smallest in original array
    duplicates = [x for x in arr if x == nth_smallest]

    return nth_smallest, duplicates


arr = [2, 3, 2, 4, 2, 6, 2]
#print(find_nth_smallest_with_duplicate(arr, 1))


def find_nth_smallest_with_duplicate_index(arr, n):
    index = 0
    nth_smallest = arr[0]
    if len(arr) < n:
        return None, []

    sorted_arr = sorted(arr)  # Keep duplicates
    nth_smallest = sorted_arr[n - 1]

    # Find all occurrences of nth smallest in original array
    #duplicates = [x for x in arr if x == nth_smallest]
      # Collect all indexes where the value matches nth_smallest
    indexes = [i for i, val in enumerate(arr) if val == nth_smallest]
    values = [arr[i] for i in indexes]

        

    return nth_smallest, indexes, values


arr = [2, 3, 2, 4, 2, 6, 2]
print(find_nth_smallest_with_duplicate_index(arr, 1))


    












