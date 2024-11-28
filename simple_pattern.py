def print_sr():
    s_pattern = [
        " ***** ",
        "*      ",
        "*      ",
        " ***** ",
        "      *",
        "      *",
        " ***** "
    ]

    r_pattern = [
        " *****  ",
        "*     * ",
        "*     * ",
        " *****  ",
        "*   *   ",
        "*    *  ",
        "*     * "
    ]

    # Print the two letters side by side
    for s_line, r_line in zip(s_pattern, r_pattern):
        print(s_line + "   " + r_line)

print_sr()
