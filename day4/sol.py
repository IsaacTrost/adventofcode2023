sol1 = 0
with open("input.txt") as f:
    copies = []
    lines = f.readlines()
    for line in lines:
        copies.append(1)
    place = 0
    for line in lines:
        nums = line.split(': ')[1].strip().split('\n')[0].replace('  ', ' ')
        win = nums.split(' | ')[0].split(' ')
        have = nums.split(' | ')[1].split(' ')
        this = 0
        other = 0
        for num in have:
            if num in win:
                if this == 0:
                    this = 1
                else:
                    this*=2
        for num in have:
            if num in win:
                other += 1
        sol1 += this
        for i in range(1, other + 1):
            copies[place + i] += copies[place]
        place += 1
sol2 = sum(copies)
print("sol 1", sol1)
print("sol 2", sol2)
        