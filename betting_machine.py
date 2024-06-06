import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8,
}


def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)
    random.shuffle(all_symbols)

    columns = []
    for _ in range(cols):
        column = all_symbols[:rows]
        all_symbols = all_symbols[rows:]
        columns.append(column)

    return columns


def print_machine(columns):
    for row in range(ROWS):
        for col in range(COLS):
            if col != COLS - 1:
                print(columns[col][row], end='|')
            else:
                print(columns[col][row], end='')
        print()


def deposit():
    while True:
        amount = input('What would you like to deposit? £  ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be grater then 0 !')
        else:
            print('Please enter a number!')
    return amount


def line_numbers():
    while True:
        lines = input('Enter the number of lines to bet on! (1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter valid number of lines!')
        else:
            print('Please enter a number!')
    return lines


def get_bet():
    while True:
        amount = input('What would you like to bet on each line? £  ')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between £{MIN_BET} - £{MAX_BET}.')
        else:
            print('Please enter a number!')
    return amount


def main():
    balance = deposit()
    lines = line_numbers()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You do not have enough credit. Your current balance is £{balance}')
        else:
            break
    print(f'You are betting £{bet} on {lines} lines. Your total bet is equal to £{total_bet}')

    slots = get_spin(ROWS, COLS, symbol_count)
    print_machine(slots)


main()
