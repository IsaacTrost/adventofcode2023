from curses.ascii import isdigit

total = 0
valid = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        for num in valid:
            if num in line:
                line = line.replace(num, num[:-1] + str(valid.index(num) + 1) + num[-1])
        print(line)
        for char in line:
            if char.isdigit():
                total += int(char) * 10
                break
        for char in line[::-1]:
            if char.isdigit():
                total += int(char)
                break
print(total)