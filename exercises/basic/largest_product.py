import functools

def findMaxProduct(arr, n, m):
    max_product = 0
    for i in range(0, n - m + 1):
        sub_arr = arr[i:m + i]
        # print("Checking arr[{i}, {j}]: {ar}".format(i=i,j=(m+i),ar=sub_arr))
        curr_product = functools.reduce(lambda x, y: x * y, sub_arr)
        max_product = curr_product if curr_product > max_product else max_product

    return max_product


if __name__ == "__main__":
    n = 7
    m = 4
    arr = [7, 3, 7, 2, 9, 8, 10]

    ans = findMaxProduct(arr, n, m)

    print(ans)
