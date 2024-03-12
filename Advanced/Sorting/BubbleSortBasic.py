import time

startTime = time.time()
items = [21, 6, 9, 33, 3]


def bubble_sort_basic(arr):
    n = len(arr)
    print('len', n)
    for i in range(n-1):
        print('outer:', i, 'arr:', arr)

        for j in range(n-1):
            print('inner:', j)

            if arr[j] > arr[j + 1]:
                print(arr[j], '>', arr[j+1])
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                print('after swap', arr)

    print(arr)


bubble_sort_basic(items)
print(f'{time.time() - startTime:f}')
