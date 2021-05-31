#!/usr/bin/env python3

# Created by: Jonathan Kene
# Created on: May 31, 2021
# The program will use one for loop and one if statement,
# outputting five integers per line with each separated by a space.

import constants


def main():
    # initilizations
    counter = 1000
    # do an if statement in a for loop to display the numbers in 5 per line
    for counter in range(constants.MIN_VALUE, constants.MAX_VALUE):
        if ((counter+1) % 5 == 0):
            print(counter)
        else:
            print(counter, end="")


if __name__ == "__main__":
    main()
