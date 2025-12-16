import time
from PIL import Image
t0 = time.time()
file = Image.open("5.4/jelly_beans.jpg")
jbimg = file.load()
width = file.width
height = file.height

yellow_pixles = 0
for x in range(width):
    for y in range(height):
        r = jbimg[x, y][0]
        g = jbimg[x, y][1]
        b = jbimg[x, y][2]
        if r > 150 and g > 150 and b < 150:
            yellow_pixles += 1
    
print("Number of yellow pixles:", yellow_pixles)
print(width * height)

percent_yellow = (yellow_pixles / (width * height)) * 100
report = "Percentage of yellow pixles: {:.2f}%".format(percent_yellow)
t1 = time.time()
print(report)
entire_time = t1 - t0
print("Time to process image: {:.2f} seconds".format(entire_time))

