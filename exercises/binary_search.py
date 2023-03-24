# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def binarysearch(arr, n, k):
    if arr == []:
        return -1

    print(f"Running for arr={arr}, n={n}, k={k}")
    indx = n // 2
    el = arr[indx]
    print(f"Checking el {el} at index {indx}")

    if k == el:
        return indx
    elif n == 1:
        return -1
    elif k < el:
        return binarysearch(arr[:indx], len(arr[:indx]), k)
    else:
        res = binarysearch(arr[indx + 1:], len(arr[indx + 1:]), k)
        if res == -1:
            return res
        else:
            return indx + 1 + res


n = 72
arr_str = "1 2 3 4 5 6 9 10 14 15 16 17 19 20 22 24 25 26 27 28 29 31 32 33 34 35 36 39 41 42 43 45 46 47 48 49 50 51 52 53 56 57 58 60 61 62 63 65 66 67 68 69 70 73 74 75 76 78 81 82 83 84 85 86 88 90 91 93 94 97 99 100"
arr = list(map(int, arr_str.split(" ")))

k = 4

print(f"arr is {arr}")
print(binarysearch(arr, n, k))