def is_num_palindrome(num: int):
    return str(num) == str(num)[::-1]


def PalinArray(arr, n):
    for num in arr:
        if not is_num_palindrome(num):
            return 0

    return 1


if __name__ == "__main__":

    assert PalinArray([111, 222, 333, 444, 555], 5) == 1
    assert PalinArray([121, 131, 20], 3) == 0
