def subsets(arr):
    results = []
    rec(arr, 0, [], results)
    return results


def rec(arr, i, subset, results):

    # base case
    if i == len(arr):
        results.append(subset[:])
        return

    # case include
    subset.append(arr[i])
    rec(arr, i + 1, subset, results)
    subset.pop()

    # case : exclude
    rec(arr, i + 1, subset, results)


print(subsets([1, 2]))
