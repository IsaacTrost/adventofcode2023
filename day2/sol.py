given = {"red": 12, "green": 13, "blue": 14}

games = []
total = 0
parttwo = 0
with open('input.txt', 'r') as f:
    count = 0
    for line in f.readlines():
        miny = {"red": 0, "green": 0, "blue": 0}
        count+=1    
        game = line.split(":")[1]
        flag = False
        for round in game.split(";"):
            for color in round.split(","):
                for key in given:
                    if(key in color):
                        if(int(color.split(" ")[1]) > miny[key]):
                            miny[key] = int(color.split(" ")[1])
                        if(int(color.split(" ")[1]) > given[key]):
                            flag = True
                            break
        if(not flag):  
            total+=count
        parttwo += miny["red"] * miny["green"] * miny["blue"]
         
            
print("part 1", total)
print("part 2", parttwo)


