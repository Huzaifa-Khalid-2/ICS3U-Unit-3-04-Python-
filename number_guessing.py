#!/usr/bin/env python3

# Created by: Huzaifa
# Created on: March 2022
# This function takes a random integer and checks if its
# >0/<0/==0

def main():
    # this function checks if the number is >0/<0/==0

    # input
    number = int(input("Enter any integer: "))
    print("")

    # process and output
    if number > 0:
        print("you have a positive number")
    elif number < 0:
        print("you have a negative number.")
    elif number == 0:
        print("Your number is 0.")
    else:
        print("I have no clue")
    print("\nDone.")


if __name__ == "__main__":
    main()
