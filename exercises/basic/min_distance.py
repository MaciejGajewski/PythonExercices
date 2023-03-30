class Solution:
    def minDist(self, arr, n, x, y):
        x_y_direction = None
        found_y = False

        idx_x = 0
        idx_y = 0

        min_distance = n + 1

        for idx, el in enumerate(arr):
            if el == x and x_y_direction is None:
                idx_x = idx
                x_y_direction = "xy"
            elif el == y and x_y_direction is None:
                idx_y = idx
                x_y_direction = "yx"
            elif el == x and x_y_direction == "yx":
                min_distance = (idx - idx_y) if (idx - idx_y) < min_distance else min_distance
                idx_x = idx
                x_y_direction = "xy"
            elif el == y and x_y_direction == "xy":
                min_distance = (idx - idx_x) if (idx - idx_x) < min_distance else min_distance
                idx_y = idx
                x_y_direction = "yx"
            elif el == x and x_y_direction == "xy":
                idx_x = idx
            elif el == y and x_y_direction == "yx":
                idx_y = idx

            # print("Curr idx={idx}, el={el}, x_y_direction={x_y_direction}, idx_x={x}, idx_y={y}"
            #    .format(idx=idx,el=el, x_y_direction=x_y_direction, x=idx_x, y=idx_y))

        return min_distance if min_distance != n + 1 else -1


if __name__ == "__main__":
    arr = [1, 1, 5, 2, 3, 2]
    n = 6
    x = 2
    y = 1

    ob = Solution()
    ans = ob.minDist(arr, n, x, y)

    print(ans)
