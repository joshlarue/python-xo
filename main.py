from xo import Token

def board(tokens):
    print(f'''
    ___________________
    |     |     |     |
    |  {tokens[0]}  |  {tokens[1]}  |  {tokens[2]}  |
    |_____|_____|_____|
    |     |     |     |
    |  {tokens[3]}  |  {tokens[4]}  |  {tokens[5]}  |
    |_____|_____|_____|
    |     |     |     |
    |  {tokens[6]}  |  {tokens[7]}  |  {tokens[8]}  |
    |_____|_____|_____|
    ''')

def playGame(positions):
    p1Turn = True
    while p1Turn:
        position = tuple(input("Player 1, enter your coordinates in the format 'x, y': ").split(', '))
        for val in position:
            val = int(val)
        positions['x'] = position
        print(position)
        print(positions)


def main():
    tokens = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']
    positions = {}
    board(tokens)
    playGame(positions)


if __name__ == '__main__':
    main()