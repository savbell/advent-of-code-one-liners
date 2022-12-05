with open('./day-04.txt') as file:
    assignments = file.read().split('\n')

sections = [[list(map(int, a.split('-'))), list(map(int, b.split('-')))] for a, b in [x.split(',') for x in assignments]]
subsets = [(x[0][0] >= x[1][0] and x[0][1] <= x[1][1]) or (x[0][0] <= x[1][0] and x[0][1] >= x[1][1]) for x in sections]
overlaps = [x[0][0] <= x[1][1] and x[0][1] >= x[1][0] for x in sections]
print(sum(subsets), sum(overlaps))