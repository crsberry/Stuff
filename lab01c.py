"""
Program: CS 115 Lab 01b
Author: 
Description: This program will compute the area of a square, the perimeter of a square and the volume of a square,
    given the side length.
"""


def main():
    # Get the side length
    length = int(input('Enter a numeric value: '))

    # Compute the area of the square
    square_area = length * length

    print("The area of a square with side length ", length,
          " is ", square_area, ".", sep="")

    # Compute the perimeter of the square
    perimeter = 4 * length

    print('The perimeter of a square with side length ', length,
          ' is ', perimeter, '.', sep='')

    # Compute the volume of the square
    volume = length * length * length

    print('The volume of a square with side length ', length,
          ' is ', volume, '.', sep='')

main()
