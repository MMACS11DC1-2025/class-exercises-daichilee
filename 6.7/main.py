from PIL import Image

img = (
"green1.jpg","green2.jpg","green3.jpg",
"red1.jpg","red2.jpg","red3.webp","red4.webp",
"yellow1.webp","yellow2.jpg","yellow3.jpg"
)

for n in img:
    f = Image.open("6.7/images/" + n)
    w, h = f.size

    tr = 0
    tg = 0
    tb = 0
    c = 0

    for y in range(1, h-1):
        for x in range(1, w-1):
            r, g, b = f.getpixel((x, y))

            if r < 40 and g < 40 and b < 40:
                r2, g2, b2 = f.getpixel((x, y+1))

                tr += r2
                tg += g2
                tb += b2
                c += 1

    if c > 0:
        r = tr // c
        g = tg // c
        b = tb // c

        if r > g and r > b:
            s = "red stop"
        elif g > r and g > b:
            s = "green go"
        else:
            s = "yellow slow"

        print(n, "=", s)
    else:
        print(n, "= no black frame found")
