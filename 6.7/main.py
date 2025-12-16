from PIL import Image
import time

picture_data = []

def is_target_color(r, g, b):
    return r >= 150 and g <= 100 and b <= 100

image_list = (
    "green1.jpg", "green2.jpg", "green3.jpg",
    "red1.jpg", "red2.jpeg", "red3.jpg", "red4.jpeg", "red5.jpg",
    "yellow1.jpg", "yellow2.jpg"
)

start_time = time.time()

for image in image_list:
    file = Image.open("6.7/images/" + image)
    img = file.load()

    width = file.width
    height = file.height
    red_count = 0

    for x in range(width):
        for y in range(height):
            r, g, b = img[x, y]
            if is_target_color(r, g, b):
                red_count += 1

    red_percent = round((red_count / (width * height)) * 100)
    print("{} has {:.2f}% red.".format(image, red_percent))

    if red_percent > 2.5:
        print("STOP: Red traffic light detected")

    picture_data.append((image, red_percent))

end_time = time.time()
print("Pixel analysis took {:.3f} seconds.".format(end_time - start_time))

for i in range(len(picture_data)):
    max_index = i
    for x in range(i + 1, len(picture_data)):
        if picture_data[x][1] > picture_data[max_index][1]:
            max_index = x
    picture_data[i], picture_data[max_index] = picture_data[max_index], picture_data[i]

print("Sorted red percentages (high -> low):", picture_data)

def binary_search_name(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        name_only = data[mid][0].split(".")[0]

        if name_only == target:
            return mid
        elif name_only < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

name_sorted = picture_data[:]
for i in range(len(name_sorted)):
    min_index = i
    for x in range(i + 1, len(name_sorted)):
        if name_sorted[x][0] < name_sorted[min_index][0]:
            min_index = x
    name_sorted[i], name_sorted[min_index] = name_sorted[min_index], name_sorted[i]

question = input("Enter an image name to find its redness position: ")
index = binary_search_name(name_sorted, question)

if index == -1:
    print("That image is not in the list.")
else:
    image_name = name_sorted[index][0]
    for position in range(len(picture_data)):
        if picture_data[position][0] == image_name:
            
            print("{} is ranked #{} in redness ({}% red).".format(image_name, position + 1, picture_data[position][1]))
            break