# 🐍📅 Advent of Code One-Line Solutions
As a personal challenge, I'm trying to solve every [Advent of Code](https://adventofcode.com/) problem in a single line of Python code. No, my solutions are not optimal. Nor readable. Nor useful in any other way. But it's fun, so here we go!

I originally attempted this in 2022 and made it through about a dozen days. I'm now working on 2023 in real time! You can follow along on this repository or through [my Reddit posts](https://www.reddit.com/u/ImpossibleSav).

Note that per copyright and [Eric Wastl's request](https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/), input files are not included in this repository, so you must replace the file paths if you would like to run this code.

## Progress Tracking
| Status | Description |
| ------ | ----------- |
| ❌     | Problem not attempted yet |
| ✍     | Working on original solution |
| ⭐     | Original (OG) solution finished, working on one-line solution |
| ✅     | Completed both OG and one-line solutions |

### 2023 Solutions
| Day | Part 1 | Part 2 | Commentary |
|-----|--------|--------|------------|
| [01](2023/day-01.py) | ✅ | ✅ | This year, I'm removing my "no imports" restriction 😅 |
| [02](2023/day-02.py) | ✅ | ✅ | Getting in a lot of RegEx practice this year! |
| [03](2023/day-03.py) | ✅ | ✅ | Oh boy, the amount of RegEx I'm using is slowing down my computer... and [the Walrus](https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions) is back! |

### 2022 Solutions
Currently I am not working on 2022 problems, but this is where I left off:

| Day | Part 1 | Part 2 | Commentary |
|-----|--------|--------|------------|
| [01](2022/day-01.py)  | ✅     | ✅     |  |
| [02](2022/day-02.py)  | ✅     | ✅     |  |
| [03](2022/day-03.py)  | ✅     | ✅     |  |
| [04](2022/day-04.py)  | ✅     | ✅     |  |
| [05](2022/day-05.py)  | ✅     | ✅     | This one is a bit cheese but I'm doing my best. Requires Python 3.8 (https://peps.python.org/pep-0572/). |
| [06](2022/day-06.py)  | ✅     | ✅     |  |
| [07](2022/day-07.py)  | ✅     | ✅     | Even more cheese. But we got it! |
| [08](2022/day-08.py)  | ✅     | ✅     | Oh boy, I've started cheesing in my OG solutions now too. |
| [09](2022/day-09.py)  | ✅     | ✅     | Today's solution is brought to you by `x.insert(0, x.pop(0)+1)`. |
| [10](2022/day-10.py)  | ✅     | ✅     |  |
| [11](2022/day-11.py)  | ✅     | ✅     |  |
| [12](2022/day-12.py)  | ⭐     | ⭐     |  |
| [13](2022/day-13.py)  | ✍     | ❌     |  |
| [14](2022/day-14.py)  | ✅     | ✅     |  |


## Repo Organization
Within each year's folder:
- All the one-line solutions are combined into a single disgusting line of code that solves all the Advent of Code problems at once, nicknamed based on the year:
  - **2023:** [`the-basilisk`](2023/the-basilisk.py)
  - **2022:** [`the-beast`](2022/the-beast.py)
- The `day-xx.py` files have my first solution attempts and the resulting one-liners. See them to better understand what the blasphemous code does.


## Fun Stuff
I've also created a visualization to show how many characters in 2022's The Beast are used to solve each day/part as of Day 10!

<img src="./images/2022-day-10-beast-length.png" alt="A snake with rainbow bands where each colour corresponds to how many characters were used to solve each Advent of Code problem" width="750" height="600">

Other memes can be found in the [images](https://github.com/savbell/advent-of-code-one-liners/blob/master/images/) folder.


## Concluding Notes
Potential employers: I promise my production code is much, much better than this. Please don't blacklist me :(

... but if you're looking to reduce the lines of code in your codebase, I've got some ideas! ;)
