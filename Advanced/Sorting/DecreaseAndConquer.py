# Failed to implement, please check

items = [77, 66, 55, 44, 10, 88, 36, 63, 22, 34]


# trying to sort in descending order


def decrease_conquer_insertion_sort(arr, n):
    n = len(arr) - 1
    print(n)
    if n <= 1:
        return
    j = n - 1
    print(j)
    while j >= 1 and arr[j] < arr[j + 1]:
        print(j)
        temp = arr[j + 1]
        arr[j + 1] = arr[j]
        arr[j] = temp
        j = j - 1
    print(arr)
    decrease_conquer_insertion_sort(arr, n - 1)
    n -= 1
    if n == 1:
        return


decrease_conquer_insertion_sort(items, len(items))
