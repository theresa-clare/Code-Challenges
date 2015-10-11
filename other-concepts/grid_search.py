"""
Given a 2D array of digits and a 2D pattern, try to find the location of the
pattern of digits.

https://www.hackerrank.com/challenges/the-grid-search
"""

def grid_search(grid, pattern):
    found_pattern = "NO"
    for r in range(len(grid)-len(pattern)+1):
        for c in range(len(grid[0])-len(pattern[0])+1):
            if grid[r][c] == pattern[0][0]:
                start = r
                found_pattern = "YES"
                for row in pattern:
                    if grid[start][c:c+len(row)] != row:
                        found_pattern = "NO"
                    else:
                        start += 1
                if found_pattern == "YES":
                    return found_pattern
    return found_pattern   

test_cases = input()
for t in range(test_cases):
    grid_R_C = raw_input().split()
    grid_rows = int(grid_R_C[0])
    grid = []
    for r in range(grid_rows):
        line = raw_input()
        grid.append(line)
    pattern_r_c = raw_input().split()
    pattern_rows = int(pattern_r_c[0])
    pattern = []
    for r in range(pattern_rows):
        line = raw_input()
        pattern.append(line)
    print find_pattern(grid, pattern)