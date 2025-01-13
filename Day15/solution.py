from collections import defaultdict

# Part 1:-
# get starting position 
# We will get every move in to the moves array.
# For every move we will make   
# we will check in corresponding row/col if there are any boxes present we will add their coordinates in a list.
# if we directly encounter "#" we will continue to th next iteration.
# If we encounter "." we will move the boxes and the robot.



#part 2
#we will need to go through the all the coordinates which contains "[" and "]"
###########
##..@....##
##.[]....##
##[][]...##
# For above example we will add "]" and it corresponding "[" now this "[" is not in the line of robot
# but we will nned to iterate through its line to get all the boxes that are bot to move which we have done by UserWarning
# for cr,cc in moves:  for every "["  or  "]" added in our moves map we will add all the boxes in there line. 
#if # is encountered in any line no box will move as in below figure
##..@....##
##.[]....##
##[][]...##
##...#...##
#hence we will only break when we encounter # if we dont encounter # we can move these boxes.
#We will copy the values of coordinates present in moves as these values will be updated 

 


def part_one(grid,moves,ri,ci):
    rows = len(grid)
    cols = len(grid[0])
    move_mapping = {'^':(-1,0), '>': (0,1), '<': (0,-1), 'v':(1,0)}
    for i,move in enumerate(moves):
    
        steps = move_mapping[move]
        cr = ri
        cc = ci
        moves = [(cr,cc)]

        while True:
            go = True
            cr += steps[0]
            cc += steps[1]
            
            if grid[cr][cc] == "#":
                go = False
                break
            if grid[cr][cc] == "O":
                moves.append((cr,cc))
            if grid[cr][cc] == ".":
                break
        if not go:continue
        grid[ri][ci] = "."
        grid[ri + steps[0]][ci+ steps[1]] = "@"
        ri += steps[0]
        ci += steps[1]
        for r,c in moves[1 : ]:
            grid[r + steps[0]][c + steps[1]] = "O"
        
        
        result = "\n".join(" ".join(map(str, row)) for row in grid)
        # print(i, result,"after ",move)
        # print("--------------------------------------------------")

    score = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "O":
                score += 100 * r + c
    return score


def part_two(grid,moves,ri,ci):
    rows = len(grid)
    cols = len(grid[0])
    # print("\n".join(" ".join(map(str, row)) for row in grid))
    move_mapping = {'^':(-1,0), '>': (0,1), '<': (0,-1), 'v':(1,0)}
    for move in moves:
        cr = ri
        cc = ci
        moves = [(cr,cc)]
        steps = move_mapping[move]
        go = True
        for cr,cc in moves:
            cr = cr +  steps[0]
            cc = cc +  steps[1]
            if (cr,cc) in moves:continue
            if grid[cr][cc] == "#":
                go = False
                break
            if grid[cr][cc] == "[":
                moves.append((cr,cc))
                moves.append((cr,cc + 1))
            if grid[cr][cc] == "]":
                moves.append((cr,cc))
                moves.append((cr,cc - 1))
        if not go: continue
        # copy = [list(row) for row in grid] #deep copy 
        copy_val = defaultdict()
        for mr,mc in moves:
            copy_val[(mr,mc)] = grid[mr][mc]

            
        grid[ri][ci] = "."
        #original = grid[ri + steps[0]][ci +steps[1]] #(5,8) 
        grid[ri + steps[0]][ci +steps[1]] = "@"
        
        ri += steps[0]
        ci += steps[1]

        for nr,nc in moves[1:]: 
            grid[nr][nc] =  "."
        # print("before moves",moves)
        # print("\n".join(" ".join(map(str, row)) for row in grid))
        # print("------------------------------------------------------------")    
        for nr,nc in moves[1 :]:
            grid[nr+steps[0]][nc + steps[1]] = copy_val[(nr,nc)]

            
        
        # print("after move",move)
        # print("after moves",moves)
        # print("\n".join(" ".join(map(str, row)) for row in grid))
        # print("------------------------------------------------------------")

    score = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "[":
                score += (100 *r + c)
    return score

def main():
    path = "/Users/ganesh.ingale/adventofcode/Day15/input.txt"
    grid = [[]]
    moves = []
    blocks = open(path,"r",encoding="utf-8").read().split("\n\n")
    explode = {"#":"##", "O":"[]", ".":"..","@":"@." }
    grid = [list("".join(explode[c] for c in line))for line in blocks[0].split("\n")]
    print(grid)
    moves = [c for c in blocks[1] if c != "\n"]
    flag = 0
    r = 0
    c = 0
    for r in range(len(grid)):
        
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                flag = 1
                break
        if flag == 1:
            break
    
    # print(part_one(grid,moves,r,c))
    print(part_two(grid,moves,r,c))


    
    
if __name__ == "__main__":
    main()