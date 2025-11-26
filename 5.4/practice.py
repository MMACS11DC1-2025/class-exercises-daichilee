from PIL import Image
def isYellow(r, g, b):
    if r > 150 and g > 150 and b < 150:
        return True
    return False

image = Image.open("5.4/jelly_beans.jpg").load()
imageOutput = Image.open("5.4/jelly_beans.jpg")
width = imageOutput.width
height = imageOutput.height 

for i in range(width):
    for j in range(height):
        im_r = image[i, j][0]
        im_g = image[i, j][1]
        im_b = image[i, j][2]

        if isYellow(im_r, im_g, im_b):
            imageOutput.putpixel((i, j), (255, 255, 255))

imageOutput.save("5.4/jelly_beans_no_yellow.jpg")