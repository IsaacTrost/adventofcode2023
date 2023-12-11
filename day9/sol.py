with open('input.txt', 'r') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        line = line.strip().replace("  ", "")
        nums = [[int(x) for x in line.split(' ')]]
        while True:
            nums.append([])
            for i in range(len(nums[-2])-1):
                nums[-1].append(nums[-2][i+1] - nums[-2][i])
            flag = True
            for num in nums[-1]:
                if num != 0:
                    flag = False
            if flag:
                break
        nums[-1].insert(0, 0)
        for row in range(len(nums)-1)[::-1]:
            nums[row].insert(0, nums[row][0] - nums[row+1][0])
        print(nums)
        total += nums[0][0]
    print(total)
