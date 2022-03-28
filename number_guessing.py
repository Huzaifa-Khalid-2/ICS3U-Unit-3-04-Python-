#!/usr/bin/env python3

# Created by: Huzaifa
# Created on: March 2022
# This function takes a random integer between 0-9
# and tells the user if they guessed corretly

def main():
    # this function takes a random integer between 0-9
    # and tells the user if they guessed corretly

    # input
    number = int(input("Insert any integer: "))

    # process and output
    print("")
    if number > 0:
        print("You have a positive number")
    elif number < 0:
        print("You have a negative number")
    elif number == 0 :
      print("Your number is 0")
    else:
        print("I have no clue")
    print("\nDone.")

if __name__ == "__main__":
    main()
