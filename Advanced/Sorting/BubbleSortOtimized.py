import time

startTime = time.time()
items = [21, 6, 9, 33, 3]


def bubble_sort_basic(arr):
    swap_flag = False
    n = len(arr)
    print('len', n)
    for i in range(n - 1):
        print('outer:', i, 'arr:', arr)

        for j in range(n - 1):
            print('inner:', j)
            swap_flag = False

            if arr[j] > arr[j + 1]:
                print(arr[j], '>', arr[j + 1])
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swap_flag = True
                print('after swap', arr)

        if swap_flag is False:
            print('braking inner', j)
            break

    print(arr)


bubble_sort_basic(items)
print(f'{time.time() - startTime:f}')
