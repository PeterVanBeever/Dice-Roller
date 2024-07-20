# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#
# Starting
import random

# list comprehension 
# [expression for item in iterable if condition]
def dice_roller(diceQuantity):
    #create a list to keep dice roll
    die_value = [random.randint(1,6) for _ in range(diceQuantity)]
    formatted_dice_values = ' '.join(str(value) for value in die_value)
    print(f"You rolled a {formatted_dice_values}")
def main():
    # start dice roller
        print("Type q to quit.\n")
        # keep open
        while True:
            # ask user
            user_input =  input("How many dice do you want to roll?")
            # if quit
            if user_input == 'q': 
                 print("Bye")
                 break
            # try method
            try:
                diceQuantity = int(user_input)
                dice_roller(diceQuantity)
            except ValueError:
                 print("Enter a number only.")
        


if __name__ == "__main__":
    main()
    
