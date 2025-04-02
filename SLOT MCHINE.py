import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:  # Correct placement
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines
   
def slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
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

def print_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")
        
        print()


def deposit():
    while True: 
        amount = input("ENTER THE DEPOSIT:- $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("ENTER THE RIGHT AMOUNT")
        else:
            print("ENTER THE AMOUNT YOU WANT TO DEPOSIT")
    return amount

def number_of_lines():
    while True:
        lines = input("ENTER THE LINES TO BET ON BETWEEN (1-"+str(MAX_LINES)+"):- ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("ENTER THE RIGHT NUMBER OF LINES")
        else:
            print("ENTER THE LINES TO BET ON IN NUMBERS")
    return lines
 
def get_bet():
    while True:
        amount = input(f"ENTER THE AMOUNT FOR BET BETWEEN ${MIN_BET} - ${MAX_BET}:- $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("ENTER THE CORRECT AMOUNT AS PER DECIDED EARLIER")
        else:
            print("ENTER THE AMOUNT YOU WANT TO BET IN NUMBERS")
    return amount

def spin(balance):
 lines = number_of_lines()
 while True:
  bet = get_bet()
  total_bet = bet * lines
  
  if total_bet > balance:
    print(f"NOT ENOUGH AS BET IS MORE THAN BALANCE WHICH IS AT ${balance}")
  else:
    break   
 print(f"THE BET OF ${bet} on {lines} lines which make total anount of bet is ${total_bet}")
 
 slots = slot_machine(ROWS, COLS, symbol_count)
 print_machine(slots)
 winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
 print(f"YOU WON THE AMOUNT OF ${winnings}")
 print(f"YOU WON ON THE LINES:",*winning_lines)
 return winnings - total_bet

def main():
 balance = deposit()
 while True:
    print(f"CURRENT BALANCE IS:- ${balance}")
    answer = input("PRESS ENTER TO PLAY AND Q OR q TO QUIT. ")
    if answer == "Q" or answer == "q":
       break
    else:
       balance += spin(balance)
       
 print(f"YOU LEFT WITH BALANCE:- ${balance}")

main()