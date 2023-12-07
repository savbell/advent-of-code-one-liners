'''
This program automatically downloads the input file for a given day of Advent of Code.
Be sure to replace the session token with your own.
NOTE: Try not to overload the servers. Your input file will never change, so no need to download it more than once.
Also do not send more than one request every 15 minutes. Try to only download the input on the day you need it.
More info: https://www.reddit.com/r/adventofcode/wiki/faqs/automation/
Created by Sav Bell (https://github.com/savbell).
'''

import requests


################################## OPTIONS ##################################
# How to get your session token: https://github.com/wimglenn/advent-of-code-wim/issues/1
session_token = 'your_session_token'


################################# FUNCTIONS #################################
def import_aoc_input(year, day, file_path, file_name=None):
    if file_name is None:
        file_name = f'day-{str(day).zfill(2)}.txt'
    
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    headers = {
        'User-Agent': 'github.com/savbell/advent-of-code-one-liners by sav@savbell.com',
        'Cookie': f'session={session_token}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(file_path + file_name, 'w') as file:
            file.write(response.text)
    else:
        print(f'Failed to fetch input: HTTP {response.status_code}')


################################# EXECUTION #################################
import_aoc_input(2023, 6, '2023/')
