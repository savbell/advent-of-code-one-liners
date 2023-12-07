'''
This program creates a rainbow line visualization from a list of percentages or numbers.
I'm using it to visualize the length of my one-line Python solutions for Advent of Code.
Created by Sav Bell (https://github.com/savbell).
'''

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import re


################################## OPTIONS ##################################
svg_path = 'images/rainbow_line_visualization.svg'
color_mapping = 'rainbow'    # https://matplotlib.org/stable/users/explain/colors/colormaps.html


################################# FUNCTIONS #################################
# Creates and saves a rainbow line to path from a list of numbers
def create_rainbow_line(numbers, path=svg_path):
    total = sum(numbers)
    normalized_percentages = [p / total for p in numbers]

    fig, ax = plt.subplots(figsize=(10, 2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    start = 0
    colormap = plt.get_cmap(color_mapping)
    for i, p in enumerate(normalized_percentages):
        color = colormap(i / len(numbers))
        rect = patches.Rectangle((start, 0), p, 1, edgecolor=color, facecolor=color)
        ax.add_patch(rect)
        start += p

    plt.savefig(path, format='svg', bbox_inches='tight')
    plt.close(fig)

# Uses RegEx to calculate the number of characters in each part of each day's solution
# Explicitly written to be used with my combined one-line solutions
def calculate_chars(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        
    pattern = r'(Day \d{2} Part \d{1,2}:.*?)(?=Day \d{2} Part \d{1,2}:|$)'
    matches = re.findall(pattern, file_content, re.DOTALL)
    num_chars = []
    for match in matches:
        part, content = match.split(':', 1)
        num_chars.append(len(content.strip()))
    return num_chars


################################# EXECUTION #################################
char_counts = calculate_chars('2023/the-basilisk.py')
print(char_counts)
create_rainbow_line(char_counts)