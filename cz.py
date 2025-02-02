import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("Kolik si přejete vložit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Částka musí být větší než 0.")
        else:
            print("Prosím, zadejte číslo.")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Zadejte počet řádků, na které chcete vsadit (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Zadejte platný počet řádků.")
        else:
            print("Prosím, zadejte číslo.")

    return lines


def get_bet():
    while True:
        amount = input("Kolik chcete vsadit na každý řádek? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Částka musí být mezi ${MIN_BET} a ${MAX_BET}.")
        else:
            print("Prosím, zadejte číslo.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Nemáte dostatek prostředků pro tuto sázku, váš aktuální zůstatek je: ${balance}")
        else:
            break

    print(f"Vsazujete ${bet} na {lines} řádků. Celková sázka je: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"Vyhráli jste ${winnings}.")
    print("Vyhráli jste na řádcích:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Aktuální zůstatek je ${balance}")
        answer = input("Stiskněte Enter pro hraní (q pro ukončení).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"Opustili jste hru s ${balance}")


main()
