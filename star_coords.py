#!/usr/bin/env python
#
# star_coords.py
#
# By Steve Mulanax 3/28/2019
#
# This Python program prints a list of [x,y,z] coordinates that form
# the shape of a star in the SimPixel driver for BiblioPixel. The list
# can be added to the pixel_positions parameter of the SimPixel driver.

from math import sin, cos, radians

iangle = 36               # Inside angle of the star point
tangle = 180 - iangle     # Turn angle (outside)
heading = -90 + iangle/2  # Down and toward the positive X by half the iangle
divs = 10                 # #divisions in the chords. 1st of next strip at end
spacing = 10              # Spacing between the centers of the pixels
x = 0.0                   # Start at the top point, center will be 0,0
y = spacing * divs * 0.525731  # Chord length * outer radius on unit star

points = []
for chord in range(5):
    x_incr = spacing * cos(radians(heading))
    y_incr = spacing * sin(radians(heading))
    for l in range(divs-1):
        points.append([int(x), int(-y), 0])  # -y is up, so flip here
        x = x + x_incr
        y = y + y_incr
    heading = (heading - tangle) % 360  # Turn right by tangle

print(points)
