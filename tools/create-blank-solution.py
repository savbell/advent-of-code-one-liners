'''
This program creates a blank template for my one-line Advent of Code solutions.
It doesn't have much use beyond that.
Created by Sav Bell (https://github.com/savbell).
'''


################################# FUNCTIONS #################################
def create_aoc_template(day, file_path, file_name=None):
    if file_name is None:
        file_name = f"day-{str(day).zfill(2)}.py"
    template = f"""'''
2023 Advent of Code - Day {day:02} (https://adventofcode.com/2023/day/{day})
Solution by Sav Bell (https://github.com/savbell)
Challenge: Solve every day in a single line of Python code.
           See full progress at https://github.com/savbell/advent-of-code-one-liners
'''

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '2023/day-{day:02}.txt'

# To match the format of input files for the Basilisk.
q = {{ {day}: open(input_file).read().strip() }}


######################### PART 1: MULTI-LINE SOLUTION #########################
# Haven't started yet...

########################## PART 1: ONE-LINE SOLUTION ##########################
# Haven't started yet...


######################## PART 2: MULTI-LINE SOLUTION ##########################
# Haven't started yet...

########################## PART 2: ONE-LINE SOLUTION ##########################
# Haven't started yet...
"""
    with open(file_path + file_name, 'w') as file:
        file.write(template)


################################# EXECUTION #################################
create_aoc_template(14, '2023/')
