#!/usr/bin/env python3
# Created by: Angelo Garcia
# Created on: September 30th, 2025
# This program asks the user for the radius of a circle. It then calculates and displays the area and perimeter.
import math


def main():
    # input
    radius = float(input("Enter the radius of the circle (cm): "))

    # process
    area = math.pi * radius * radius
    perimeter = 2 * math.pi * radius

    # output
    print("")
    print("For a circle with a radius of {0} cm:".format(radius))
    print("The area is = {0:.2f} cm²".format(area))
    print("The perimeter is = {0:.2f} cm".format(perimeter))


if __name__ == "__main__":
    main()
