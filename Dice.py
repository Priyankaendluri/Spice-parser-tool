import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("🎲 Welcome to the Dice Roller Simulator! 🎲\n")
    
    while True:
        input("Press Enter to roll the dice... ")
        result = roll_dice()
        print(f"You rolled a {result}!\n")

        again = input("Do you want to roll again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

