# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


customer_ids = [101, 203, 305, 408, 512, 614]
target = int(input("Enter customer ID: "))

result = linear_search(customer_ids, target)
if result != -1:
    print("Linear Search: Found at index", result)
else:
    print("Linear Search: Not found")

result = binary_search(customer_ids, target)
if result != -1:
    print("Binary Search: Found at index", result)
else:
    print("Binary Search: Not found")
