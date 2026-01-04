from PIL import Image
import time

picture_data = []

#code to determine if a pixel is considered "red"
def is_target_color(r, g, b):
    return r >= 150 and g <= 100 and b <= 100

#list of images ordered by color
image_list = (
    "green1.jpg", "green2.jpg", "green3.jpg",
    "red1.jpg", "red2.jpeg", "red3.jpg", "red4.jpeg", "red5.jpg",
    "yellow1.jpg", "yellow2.jpg"
)

#set time
start_time = time.time()

#Iterate through each image to calculate percentage of red
for image in image_list:
    file = Image.open("6.7/images/" + image)
    img = file.load()
    width, height = file.size
    red_count = 0
    #Nested for loops to check every pixel
    for x in range(width):
        for y in range(height):
            r, g, b = img[x, y]
            if is_target_color(r, g, b):
                red_count += 1
    #Calculate the percentage and store the filenames into picture_data
    red_percent = (red_count / (width * height)) * 100
    #Display the results for each image
    print(f"{image} has {red_percent:.2f}% red.")
    if red_percent > 2.5:
        print("STOP: Red traffic light detected")
    picture_data.append([image, red_percent])

#Calculate and display the total processing time to the 3rd decimal place
end_time = time.time()
print(f"Pixel analysis took {end_time - start_time:.3f} seconds.")

#Selection sort to order picture_data by redness percentage
for i in range(len(picture_data)):
    max_index = i
    for x in range(i + 1, len(picture_data)):
        if picture_data[x][1] > picture_data[max_index][1]:
            max_index = x
    picture_data[i], picture_data[max_index] = picture_data[max_index], picture_data[i]

#Display the top 5 reddest images using slicing
print("Top 5 results:")
print(picture_data[:5])

#New list sorted alphabetically for the binary search
name_sorted = sorted(picture_data)

#Binary Search to efficiently find an image by its name
def binary_search_name(data, target):
    low = 0
    high = len(data) - 1
    #Simplify name for search 
    target = target.split(".")[0]
    while low <= high:
        mid = (low + high) // 2
        #Simplify current name for comparison
        current_name = data[mid][0].split(".")[0]

        if current_name == target:
            return mid
        elif current_name < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#Prompt user for an image name and search for it
question = input("Enter an image name: ")
index = binary_search_name(name_sorted, question)

if index == -1:
    print("That image is not in the list.")
else:
    full_name, score = name_sorted[index]
    #Identify the rank by finding the image in the score-sorted list
    rank = 0
    for i in range(len(picture_data)):
        if picture_data[i][0] == full_name:
            rank = i + 1
            break
    print(f"{full_name} is ranked #{rank} in redness ({score:.2f}% red).")