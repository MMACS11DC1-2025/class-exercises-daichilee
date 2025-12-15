from PIL import Image
import time


def isRed(r, g, b):
    if r > 150 and g < 100 and b < 100:
        return True
    else:
        return False

imgList = (
"red1.jpg", "red2.jpeg", "red3.jpg", "red4.jpeg", "red5.jpg", "yellow1.jpg", "yellow2.jpg", "green1.jpg", "green2.jpg", "green3.jpg"
)

startTimer = time.time()

for image in imgList:
    file = image.open("6.7/images/" + image)
    img = file.load()
    width = file.width
    height = file.height

    redPixelCount = []