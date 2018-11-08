"""
Program: CS 115 Lab 01b
Author: 
Description: This program will compute the area of a square,
    given the side length.
"""


def main():
    # Get the side length
    length = int(input('Enter a numeric value: '))

    # Compute the area of the square
    square_area = length * length

    print("The area of a square with side length ", length,
          " is ", square_area, ".", sep="")


main()
