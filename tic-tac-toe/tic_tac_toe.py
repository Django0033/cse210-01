def main():
    grid = create_grid()
    player_mark = 'O'

    while True:
        print_grid(grid)
        set_mark(grid, player_mark)
        check_win(grid, player_mark)
        player_mark = change_mark(player_mark)


def check_win(grid, player_mark):
    '''
    Checks if there are 3 of the same mark in a row, column or diagonal, and prints the winner.

    Parameters:
        grid (list): A list of lists representing the grid
        player_mark (str): The mark of the player who just played

    Returns:
        None
    '''
    if grid[0][0] == grid[0][1] == grid[0][2] or \
       grid[1][0] == grid[1][1] == grid[1][2] or \
       grid[2][0] == grid[2][1] == grid[2][2] or \
       grid[0][0] == grid[1][0] == grid[2][0] or \
       grid[0][1] == grid[1][1] == grid[2][1] or \
       grid[0][2] == grid[1][2] == grid[2][2] or \
       grid[0][0] == grid[1][1] == grid[2][2] or \
       grid[0][2] == grid[1][1] == grid[2][0]:
        print_grid(grid)
        print('\n{} wins!'.format(player_mark))
        exit()


def change_mark(player_mark):
    '''
    Checks what is the current player_mark and changes it to the other

    Parameters:
        player_mark (str): The current player_mark

    Returns:
        player_mark (str): The new player_mark
    '''
    if player_mark == 'O':
        player_mark = 'X'
    else:
        player_mark = 'O'
    return player_mark


def set_mark(grid, player_mark):
    '''
    Set players mark in a chosen spot

    Parameters:
        grid (list): A list of lists representing the grid
        player_mark (str): The mark to be set

    Returns:
        None
    '''
    spot = int(input('\n{}\' turn to choose a square (1-9): '.format(player_mark)))
    for row in grid:
        for number in row:
            if number == spot:
                indx = row.index(number)
                row[indx] = player_mark


def print_grid(grid):
    '''
    Prints a compound list as a grid

    Parameters:
        grid (list): A list of lists representing the grid

    Returns:
        None
    '''
    print()
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
