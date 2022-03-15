# -*- coding: utf-8 -*-


"""

Given a 3x3 dot grid on an Android lock screen:

. . .
. . .
. . .

1 2 3
4 5 6
7 8 9

Possible patterns:
1-2-5-8 = yes
1-2-3 = no
1-2-5-2 = no
8-5-2-1 = yes
1-2-3-9 = no
1-2-3-5 = yes
1-2-3-6-5-4 = yes

A password pattern is valid if (must satisfy all 4 conditions):
    1. The pattern passes through at least 4 dots on the grid
2. The next dot to connect to must be adjacent or diagonal to the current dot
    (no jumping to farther dots or out of bounds)
3. A valid pattern cannot have two of the same dot
4. A pattern is directional: back and forth on the same path are two distinct patterns

Compute the number of valid patterns and print the number.
"""

valid_dot_for1 = [2, 4, 5]
valid_dot_for2 = [1, 3, 4, 5, 6]
valid_dot_for3 = [2, 5, 6]
valid_dot_for4 = [1, 2, 5, 7, 8]
valid_dot_for5 = [1, 2, 3, 4, 6, 7, 8, 9]
valid_dot_for6 = [2, 3, 5, 8, 9]
valid_dot_for7 = [4, 5, 8]
valid_dot_for8 = [4, 5, 6, 7, 9]
valid_dot_for9 = [5, 6, 8]

valid_dot_grid = [valid_dot_for1, valid_dot_for2, valid_dot_for3, valid_dot_for4, valid_dot_for5, valid_dot_for6,
                  valid_dot_for7, valid_dot_for8, valid_dot_for9]

MIN_DOTS_IN_PATTERN = 4

possible_patterns = []


def append_pattern(start_pattern):
    dots = valid_dot_grid[start_pattern[-1] - 1]
    result = []

    for next_dot in dots:
        if next_dot not in start_pattern:
            pattern = start_pattern.copy()
            pattern.append(next_dot)
            patterns = append_pattern(pattern)

            if patterns:
                for p in patterns:
                    if p:
                        result.append(p)
            else:
                result.append(pattern)

    return result


if "__main__" == __name__:
    for i in range(len(valid_dot_grid)):
        current_dot = i + 1
        possible_dots = valid_dot_grid[i]

        top_pattern = [current_dot]
        for item in append_pattern(top_pattern):
            print("possible_patterns", item)
            possible_patterns.append(item)

            sub_pattern = item[:-1]
            while len(sub_pattern) >= MIN_DOTS_IN_PATTERN:
                if sub_pattern not in possible_patterns:
                    print("possible_patterns", sub_pattern)
                    possible_patterns.append(sub_pattern)

                sub_pattern = sub_pattern[:-1]

    print("possible_patterns count", len(possible_patterns))
