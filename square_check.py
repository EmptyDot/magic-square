import numpy as np


def main(n=0):
    """
    Main function

    :param n: the target sum
    """

    try:
        arr1, arr2, a0 = generate_arrays(n)
        grid = build_grid(n, arr1, arr2, a0)
        print(n)
        print(grid)
        return grid
    except TypeError:
        return False


def generate_arrays(n):
    """Generate the arrays"""
    # generate arr1
    for a1 in range(1, n - 1):
        for a2 in range(1, n - 1):
            # check if arr1 is valid
            if a1 + a2 < n and a1 != a2:
                arr1 = [a1, a2]
                # get the missing number in the array
                a0 = n - sum(arr1)
                # check if a0 is valid
                if a0 > 0 and a0 not in arr1:
                    # generate arr2
                    for b1 in range(1, n - 1):
                        b2 = n - a0 - b1
                        # check if arr2 is valid
                        if b1 not in arr1 and b2 not in arr1 and b1 != b2 and b2 > 0:
                            arr2 = [b1, b2]
                            # check if a0 is valid
                            if a0 not in arr2:
                                # compare arr1 and arr2 and check if they are valid together
                                if 3 * arr1[1] + 2 * arr2[1] - arr2[0] - a0 == n:
                                    if 3 * arr2[1] + 2 * arr1[1] - arr1[0] - a0 == n:
                                        return arr1, arr2, a0
    return False


def build_grid(n, arr1, arr2, a0):
    """Build the magic square"""
    # initialize the grid
    grid = np.zeros((3, 3), dtype=int)
    # row 0
    grid[0] = [a0] + arr1
    # col 0
    grid[:, 0] = [a0] + arr2
    # middle
    grid[1, 1] = n - arr1[1] - arr2[1]
    # bottom right corner
    grid[2, 2] = n - a0 - grid[1, 1]
    # middle right
    grid[1, 2] = n - grid[2, 2] - arr1[1]
    # bottom middle
    grid[2, 1] = n - grid[1, 1] - arr1[0]
    return grid


if __name__ == "__main__":
    for i in range(1, 100):
        main(i)

