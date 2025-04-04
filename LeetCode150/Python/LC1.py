def binary_search_boolean(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def two_sum_boolean(arr, target):
    arr.sort()
    for i in range(len(arr)):
        complement = target - arr[i]
        if binary_search_boolean(arr, i + 1, len(arr) - 1, complement):
            return True
    return False


def two_sum_pair(arr, target):
    arr.sort()
    for i in range(len(arr)):
        complement = target - arr[i]
        if binary_search_boolean(arr, i + 1, len(arr) - 1, complement):
            return [arr[i], complement]
    return []

print(two_sum_boolean([0, -1, 2, -3, 1], -2))
print(two_sum_pair([0, -1, 2, -3, 1], -2))

