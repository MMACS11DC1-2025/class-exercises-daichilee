# Project: Image Explorer Checklist Rubric

TOTAL: ___ / 100

## Project Description

**Goal:** Create a Python program that analyzes a set of at least 10 images based around a theme of your choice (e.g., medical scans, satellite photos, historical archives, deep-sea research photos).
Using the new skills in units 5 and 6, you will implement a computer vision algorithm that detects a visual feature.

## "Gotta Have" Checklist

## **ESSENTIAL REQUIREMENTS**
### Project Overview - Must appear in a README.md file

> *These items belong at the very top of your `README.md`. They give the context for everything else you do.*

- [ ] Choose a specific theme for which you will be scanning multiple images (3 pts)
- [ ] Clearly define the visual feature your program will detect and count (2 pts)
- [ ] Justify your feature detection with an explanation of how your chosen feature can be accurately identified (3 pts)

### Image Processing and Feature Extraction (Unit 5)
#### Task 1: Pixels to Data Function
- [ ] Write a function, is_target_feature, that accepts pixel data (e.g. colour channels as RGB tuple inputs) and returns a specific, useful output (e.g., returns True if the pixel matches your custom feature definition else False, or a weight) (10 pts)
#### Task 2: Pixel Iteration and List Building
- [ ] Use nested loops to iterate over all pixels **in a set of at least 10 images** and calculate your "Feature Density Score" for each image (10 pts)
- [ ] Append the filename and score to a master list, demonstrating list manipulation and the use of the append() method (5 pts)
#### Task 3: Code Profiling
- [ ] Measure the precise time taken for the program to complete the pixel processing loops using the time module (3 pts)
- [ ] Output this time in a human-readable report, using string formatting to ensure the output displays accurately to three decimal places (2 pts)

### Algorithms and Efficiency (Unit 6)
#### Task 4: Selection Sort
- [ ] Implement the Selection Sort algorithm function yourself (not using built-in libraries for sorting) to sort the master list based on the calculated Feature Density Score (highest to lowest) (12 pts)
- [ ] Output the top 5 results using list slicing (3 pts)
#### Task 5: Binary Search
- [ ] Implement the Binary Search algorithm function yourself to search the sorted list for a specific target score (10 pts)

### Process
- [ ] Algorithm design in English: outline the logic using English comments (pseudocode) before each major Python code block (3 pts)
- [ ] Code clarity: use descriptive variable names unless they are standard loop indices (e.g. x, y) (2 pts)
- [ ] Use of functions: structure the program using functions to organize it and reduce code duplication (2 pts)
- [ ] Testing and robustness: include a section in your README describing testing done to ensure each of the tasks works as intended (1 pt)
- [ ] Performance analysis: include a section in your README describing your code profiling: give an example of the report and discuss what parts of the program take the longest
- [ ] Challenges faced: include a section in your README describing at least one challenge faced and how you overcame it (2 pts)

### Version Control
- [ ] Source code is committed to repository on Github with at least 5 meaningful commits on different days prior to deadline (10 pts)

## **QUALITY CRITERIA**
### Code Quality and Efficiency
- [ ] Code quality: Clean, readable structure (2 pts)
- [ ] Efficiency: Evidence of thinking about algorithmic complexity throughout the code (2 pts)
- [ ] The program handles potential errors and edge cases effectively (2 pts)
- [ ] Documentation polish: README is clear, concise, free of typos; also, code comments explain why decisions were made. (1 pt)

### Creativity and Originality
- [ ] The chosen theme and visual feature are unique, interesting, and insightful (2 pts)
- [ ] Feature detection uses a more advanced process, such as pre-processing the image, using multiple pixels, or using statistical approaches to detect features (4 points)
- [ ] Captured feature involves a real-world use-case. References a real paper, report, or dataset supporting decisions for detecting feature (4 points)

## **SUBMISSION REQUIREMENTS**

### **Files to Include:**
1. `main.py` - Your complete Python program
1. `README.md` - Documentation file with all required content.
1. Images - The set of at least 10 images that your program will analyze
1. (Optional): - Other Python modules you write that you import for use in `main.py`

### **Required Documentation Content Summary:**
- Project overview, including your chosen image theme
- Explanation of your visual feature and how it will be identified
- Discussion of the testing and validation done to verify your program works as intended
- Discussion of your code profiling
- Discussion of challenges faced while working on this project

## **GETTING STARTED TIPS**

1. Start simple - work on one sub-problem at a time
1. Test incrementally - "unit test" each function you write separately to make sure it works
1. Start with pseudocode - describe your algorithm in English before starting to code
1. Use the "gotta have" checklist - self-grade to make sure your submission fulfills all requirements