# Selection Sort Implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


salaries = [
    45000.00, 56000.50, 32000.75, 89000.90,
    71000.40, 51000.30, 47000.00, 92000.00,
    83000.00, 61000.00
]

print("Selection Sort:")
print(selection_sort(salaries.copy()))
print("Top 5 highest salaries:")
print(selection_sort(salaries.copy())[-5:][::-1])

print("\nBubble Sort:")
print(bubble_sort(salaries.copy()))
print("Top 5 highest salaries:")
print(bubble_sort(salaries.copy())[-5:][::-1])
