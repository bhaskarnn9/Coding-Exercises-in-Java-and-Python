items = [44, 71, 91, 77, 10, 88, 36, 63, 22]


def quick_sort(arr):
    even_index = -1
    for i in range(len(arr)):
        print(arr[i])
        if arr[i] % 2 == 0:
            even_index += 1
            temp = arr[i]
            arr[i] = arr[even_index]
            arr[even_index] = temp
    print(arr)


selection_sort(items)






