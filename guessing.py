#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Oct 2022
# This program is a guessing game

import random


def main():
    # this is a number guessing game

    # input
    print("Random Number Guessing Game.")
    while True:
        random_number = random.randint(1, 9)  # a number between 1 and 9
        user_number = input("Enter a number between 0-9: ")

        # process
        try:
            number_int = int(user_number)
            if number_int == random_number:
                print("YAY! You guessed the correct number!")
                break
            else:
                print("Random number was {0}. Try again.\n".format(random_number))
        except ValueError:
            print("Invalid integer")
    # output

    print("\nDone.")


if __name__ == "__main__":
    main()
