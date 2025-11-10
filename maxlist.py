import random

list_numbers = [random.randint(1,10000) for _ in range(10000)]

maxvalue = max(list_numbers)
index_of_max = list_numbers.index(maxvalue)

print("The highest number is:", maxvalue)
print("It is located at this index:", index_of_max)
import time
import random
def timed_func(func_to_time):
    def timed(*args, **kwargs):
        start = time.perf_counter()
        res = func_to_time(*args, **kwargs)
        print(time.perf_counter() - start)
        return res
    return timed

@   timed_func
def merge_sort(list_numbers):
    if len(list_numbers) <= 1:
        return list_numbers
    mid = len(list_numbers) // 2
    left = merge_sort(list_numbers[:mid])
    right = merge_sort(list_numbers[:mid])

    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
            sorted_list.extend(left[i:])
            sorted_list.extend(right[i:])
            return sorted_list

sorted_list = merge_sort(list_numbers)
maxvalue = sorted_list[-1]
index_of_max = list_numbers.index(maxvalue)


