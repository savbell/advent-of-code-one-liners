'''
This program creates a rainbow line visualization from a list of percentages or numbers.
I'm using it to visualize the length of my one-line Python solutions for Advent of Code.
It can also be used to automatically count and visualize the length of your solutions if
you change the options below.
Created by Sav Bell (https://github.com/savbell).
'''

from matplotlib.colors import to_hex
import matplotlib.pyplot as plt
import re
import svgwrite
import os

################################## OPTIONS ##################################
svg_path = 'images/rainbow-line-visualization.svg' # Where to save the SVG
color_mapping = 'turbo'      # https://matplotlib.org/stable/users/explain/colors/colormaps.html
solutions_folder = '2023/'   # You may need your full path
first_day_file = 'day-01.py' # Used to automatically determine your naming convention


################################# FUNCTIONS #################################
# Creates and saves a rainbow line SVG from a list of numbers.
# Returns a list of [number, percentage, color] for each rectangle.
def create_rainbow_line(numbers, color_mapping=color_mapping, svg_path=svg_path):
    total = sum(numbers)
    normalized_percentages = [p / total for p in numbers]

    dwg = svgwrite.Drawing(svg_path, size=(1000, 200))

    start_x = 0
    layer = dwg.add(dwg.g(id=f'{color_mapping}-line'))
    colormap = plt.get_cmap(color_mapping)
    colors = []
    for i, p in enumerate(normalized_percentages):
        color = to_hex(colormap(i / len(numbers)))
        colors.append([numbers[i], p, color])

        # Calculate width of the rectangle proportionally
        width = p * 1000

        layer.add(dwg.rect(insert=(start_x, 0), size=(width, 200), fill=color, id=f'Color{i+1}'))

        # Update the start position for the next rectangle
        start_x += width

    dwg.save()
    print('SVG saved to', svg_path)


# Counts the number of characters in a file.
def count_file_chars(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        return len(file_content.strip())


# Creates a list [[day, None], file_path, num_chars] based on the name of the first day's solution.
# Assumes your files follow a naming convention like "day-01.py", "1.js", etc.
# Does not account for if you saved each part as a separate file (that's the None in [day, None]).
def count_aoc_solutions(folder_path, first_day_file):
    base_name, ext = os.path.splitext(first_day_file)
    match = re.search(r'(\D*)(\d+)(\D*)', base_name)
    prefix, day, postfix = match.groups()
    
    pattern = re.compile(rf'^{re.escape(prefix)}(\d+){re.escape(postfix)}{re.escape(ext)}$')

    solutions = []
    for file in os.listdir(folder_path):
        match = pattern.match(file)
        if match:
            day = int(match.group(1))
            file_path = os.path.join(folder_path, file)
            solutions.append([[day, None], file_path, count_file_chars(file_path)])

    # Sorting the list based on day
    return sorted(solutions, key=lambda x: x[0])


# Uses RegEx to calculate the number of characters in each part of each day's solution.
# Returns a list with each element in the format [[day, part], file_path, num_chars].
# Explicitly written to be used with my combined one-line solutions.
def count_oneliners(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        
    pattern = r'(Day \d{2} Part \d{1,2}:.*?)(?=Day \d{2} Part \d{1,2}:|$)'
    matches = re.findall(pattern, file_content, re.DOTALL)
    solutions = []

    for match in matches:
        title, content = match.split(':', 1)
        day, part = map(int, re.findall(r'\d+', title)[:2])
        num_chars = len(content.strip())
        print(str(title).rjust(2) + ' - ' + str(num_chars).rjust(3))
        solutions.append([[day, part], file_path, num_chars])

    return sorted(solutions, key=lambda x: x[0])

# Creates a rainbow line SVG from the number of characters in each part of each day's solution.
def create_oneliners_svg(file_path, color_mapping=color_mapping, svg_path=svg_path):
    solutions = count_oneliners(file_path)
    create_rainbow_line([s[2] for s in solutions], color_mapping, svg_path)

# Creates a rainbow line SVG from the number of characters in each day's solution.
def create_solutions_svg(folder_path, first_day_file, color_mapping=color_mapping, svg_path=svg_path):
    solutions = count_aoc_solutions(folder_path, first_day_file)
    create_rainbow_line([s[2] for s in solutions], color_mapping, svg_path)


################################# EXECUTION #################################
# Find the number of characters in my one-line solution and create a rainbow line SVG.
create_oneliners_svg('2023/the-basilisk.py', color_mapping, f'images/oneliners-{color_mapping}-line.svg')

# Find the number of characters for all solution files and create a rainbow line SVG.
create_solutions_svg(solutions_folder, first_day_file, color_mapping, f'images/aoc-solutions-{color_mapping}-line.svg')

# Another example: Make a rainbow line SVG from a list of numbers. Will be saved to path set in options.
# create_rainbow_line([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
