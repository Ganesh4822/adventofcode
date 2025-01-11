

# Part 1:-
# get starting position 
# We will get every move in to the moves array.
# For every move we will make   
# we will check in corresponding row/col if there are any boxes present we will add their coordinates in a list.
# if we directly encounter "#" we will continue to th next iteration.
# If we encounter "." we will move the boxes and the robot.







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
        
        
        # result = "\n".join(" ".join(map(str, row)) for row in grid)
        # print(i, result,"after ",move)
        # print("--------------------------------------------------")

    score = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "O":
                score += 100 * r + c
    return score



def main():
    path = "/Users/ganesh.ingale/adventofcode/Day15/input.txt"
    grid = [[]]
    moves = []
    blocks = open(path,"r",encoding="utf-8").read().split("\n\n")
    
    grid = [[c for c in line]for line in blocks[0].split("\n")]
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
    
    print(part_one(grid,moves,r,c))
    
    
if __name__ == "__main__":
    main()