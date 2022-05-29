import numpy as np
from itertools import permutations, chain


def main(n, unique=False):
    """
    Main function

    :param n: the magic sum
    """

    print(f'sum: {n}')

    count = 0
    for arr1, arr2 in generate_arrays(n):

        grid = build_grid(n, arr1, arr2)

        if unique:
            solutions = []
            if not check_if_permutation(grid, solutions):
                solutions.append(grid)
                count = len(solutions)
        else:
            count += 1

    print(f'Solutions: {count}')
    return


def generate_arrays(n):
    """Generate the arrays"""
    # generate arr1
    for a1 in range(1, n - 1):
        for a2 in range(1, n - 1):
            # check if arr1 is valid
            if a1 + a2 >= n - 1:  # this ensures that a0 > 0
                break
            if a1 != a2:
                # get the missing number in the array
                a0 = n - a1 - a2
                # check if a0 is valid
                if a0 not in (a1, a2):
                    arr1 = (a0, a1, a2)
                    # generate arr2
                    for b1 in range(1, n - 1):
                        # get the missing number in the array
                        b2 = n - a0 - b1
                        if b1 + a0 >= n - 1:  # this ensures that b2 > 0
                            break
                        # check if arr2 is valid
                        if b1 != b2 and all(b not in arr1 for b in (b1, b2)):
                            arr2 = (a0, b1, b2)
                            # compare arr1 and arr2 and check if they are valid together
                            if compare(arr1, arr2, n) and compare(arr2, arr1, n):
                                yield arr1, arr2
    return None, None


def compare(a, b, n):
    """Compare two arrays"""
    expr1 = a[2] + b[2] - b[1]
    expr2 = n - 2 * a[2] + a[0] - b[2]
    return expr1 == expr2 and expr1 > 0


def check_if_permutation(grid, solutions):
    """Check if the grid is a permutation of a previous solution"""
    for perm in get_permutations(grid):
        for sol in solutions:
            if np.array_equal(sol, perm):
                return True
    return False


def get_permutations(grid):
    """Get the permutations of the grid"""
    # get the permutations of the grid
    perms = [grid, np.rot90(grid), np.rot90(grid, 2), np.rot90(grid, 3), np.flipud(grid), np.fliplr(grid),
             np.rot90(np.fliplr(grid)), np.rot90(np.flipud(grid))]
    return perms

def check_permutaions(grid):
    """Check if the grid is a permutation of a previous solution"""


def build_grid(n, arr1, arr2):
    """Build the magic square"""
    # initialize the grid
    grid = np.zeros((3, 3), dtype=int)
    # row 0
    grid[0] = arr1
    # col 0
    grid[:, 0] = arr2
    # middle
    grid[1, 1] = n - arr1[2] - arr2[2]
    # bottom right corner
    grid[2, 2] = n - arr1[0] - grid[1, 1]
    # middle right
    grid[1, 2] = n - grid[2, 2] - arr1[2]
    # bottom middle
    grid[2, 1] = n - grid[2, 2] - arr2[2]
    return grid


if __name__ == "__main__":
    main(15, unique=True)






