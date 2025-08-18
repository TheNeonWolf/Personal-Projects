import random

print("*********************************************")
print("Welcome to the Lotus Slot Machine, have a go!")
print("*********************************************")



def spin_row():
    symbols = ['7️⃣', '🍒', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for symbol in range(3)]

def print_final_slots(row):
    row1 = " | ".join(row)
    print("***************")
    print("|" + row1 + "|")
    print("***************")


def get_earnings(row, bet, balance):
    if row[0] == row[1] == row[2]:
        print("Congrats! You have Won!")
        if row[0] == '⭐':
            return bet*20 + balance
        elif row[0] == '🔔':
            return bet*10 + balance
        elif row[0] == '7️⃣':
            return bet*7 + balance
        elif row[0] == '🍋':
            return bet*5 + balance
        elif row[0] == '🍒':
            return bet*5 + balance
    return 0

def main():

    b = input("Please enter how much money are you going to start with: $")
    if not b.isdigit():
        print("Please enter a valid number.")
        main()
    if int(b) <= 0:
        print("Starting money should be greater than 0.")
        main()

    balance = int(b)

    while balance > 0:
        print(f"Your balance: ${balance}")

        bet = int(input("Enter your bet amount: $"))
        if not str(bet).isdigit():
            print("Please enter a valid bet number.")
            continue

        if bet > balance:
            print(f"Your bet amount exceeds your balance(${balance}).")
            continue

        if bet <= 0:
            print(f"Bet must be greater than $0.")
            continue

        balance= balance - bet

        row = spin_row()
        print_final_slots(row)

        earnings = get_earnings(row, bet, balance)

        if earnings > 0:
            print(f'You won ${earnings}!')
        elif earnings == 0:
            print(f'You lost this round')

        balance += earnings

        i = input("Would you like to play again? (Y/N): ").upper()

        if i != 'Y':
            print(f"Thank you for playing! You have cashed out ${balance}, have a great day!")
            break

    if balance <= 0:
        print("Oops your balance is 0, thank you for playing!")


if __name__ == '__main__':
    main()