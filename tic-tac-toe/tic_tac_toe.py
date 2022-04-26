def main():
    grid = create_grid()
    print_grid(grid)


def print_grid(grid):
    '''
    Prints a compound list as a grid

    Parameters:
        grid (list): A list of lists representing the grid

    Returns:
        None
    '''
    for row in grid:
        print('{}'.format(' | '.join(str(number) for number in row)))
        if row != grid[-1]:
            print('-' * (len(row) * len(row)))


def create_grid(size=3):
    '''
    Create a numbered grid of size x size

    Parameters:
        size (int): The size of the grid

    Returns:
        grid (list): A list of lists representing the grid
    '''
    grid = []
    for row in range(size):
        grid.append([])
        for column in range(size):
            grid[row].append(row * size + column + 1)
    return grid


if __name__ == "__main__":
    main()
