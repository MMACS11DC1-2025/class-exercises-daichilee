PROJECT OVERVIEW:
Name: Daichi
Image Names: "green1.jpg, green2.jpg, green3.jpg, red1.jpg, red2.jpeg, red3.jpg, red4.jpeg, red5.jpg, yellow1.jpg, yellow.jpg"
Goal: To detect red traffic lights from other traffic lights to assist AI-driven cars in stopping.
"Choose a specific theme for which you will be scanning multiple images (3 pts)"
Traffic Light color -> useful for real world, can detect if you have to stop immeditately or you have some time.
Detects only for red lights- more practical and can save from crashes.   
"Clearly define the visual feature your program will detect and count (2 pts)"
It will detect every pixel and then count for red ones. If red pixels reaches the threshold of 2.5%, the light will be counted as red and you will be alerted to stop.
"Justify your feature detection with an explanation of how your chosen feature can be accurately identified (3 pts)"
The program identifies red pixels by requiring a high red value (>150) alongside low green and blue values (< 100) to isolate red from colors like white or yellow, which are other traffic light colors


Other info:
"Testing and robustness: include a section in your README describing testing done to ensure each of the tasks works as intended (1 pt)"
I tested the program by using not just images of red lights, but green and yellow. This is to make sure the alert is mainly only triggered on red lights, with yellow1 being the only exception. I also checked the binary search by entering names with and without the file extension to confirm it handles both correctly.
"Performance analysis: include a section in your README describing your code profiling: give an example of the report and discuss what parts of the program take the longest"
The photo checking loops are the slowest part of the program, taking around 0.820 seconds when I run the code. This is because every single pixel in all 10 images must be checked individually. The sorting and searching algorithms are much faster as they only handle 10 scores.
"Challenges faced: include a section in your README describing at least one challenge faced and how you overcame it (2 pts)"
The greatest challenge I faced was the first part of the program: finding a theme to use for this assignment. It was hard for me to find a theme that my friends haven't already taken which can be efficiently checked mostly by color. The way I overcame this problem was to think of what would be a useful way to check color in this society. My initial thought was on something about animals and what color they were, but then I thought about the ai driven cars which is where I got the idea of the traffic light color detection. Once I found the idea, the rest was much simpler.



"Source code is committed to repository on Github with at least 5 meaningful commits on different days prior to deadline (10 pts)"
The commit from school to when I wrote this README may be quite different because I was on a 9 day vacation during winter break and had to finish everything on the last 3 days. Sorry
Also from "code" to "as" commits, it may seem like a big difference but it was because the prior day, the workspaces wasn't working right and was all glitchy. So I copy and pasted my code on the prior day and sent it to myself on outlook and pasted in the next day to commit.
open "screenshot.png"