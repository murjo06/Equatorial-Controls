from PIL import Image
import numpy
import math
import warnings

STAR_SIZE = 20
selectedMagnitude = 255
magnitudeJumps = 5

warnings.filterwarnings("ignore")

image = Image.open("example.webp")
imageArray = numpy.array(image)

def getStars(magnitude):
    pixels = []
    rawPixels = []
    for x, row in enumerate(imageArray):
        for y, pixel in enumerate(row):
            if pixel[0] + pixel[1] + pixel[2] >= magnitude:
                rawPixels.append((y, x))
    for i in rawPixels:
        add = True
        for j in pixels:
            xDistance = i[0] - j[0]
            yDistance = i[1] - j[1]
            if math.sqrt(xDistance * xDistance + yDistance * yDistance) <= STAR_SIZE:
                add = False
        if add:
            pixels.append(i)
    return pixels

stars = getStars(selectedMagnitude)
while len(stars) < 3:
    stars = getStars(magnitude = selectedMagnitude - magnitudeJumps)
    selectedMagnitude -= magnitudeJumps
    print(f"Changed magnitude to {selectedMagnitude}")
print(stars)