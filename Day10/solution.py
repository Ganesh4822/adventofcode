from collections import deque

#For part one we need to find the paths through which we can reach to the distinct 9s
#for part 2 we need distinct paths through which we can reach 9

def part_one(grid,trailheads,rows,cols):
    score = 0
    for cr,cc in trailheads:
        dq = deque()
        seen = set()
        dq.append((cr,cc))
        print((cr,cc))
        while len(dq) > 0:
            (c1r, c1c) = dq.popleft()
            for nr,nc in [(c1r-1,c1c),(c1r + 1,c1c),(c1r,c1c + 1),(c1r,c1c - 1)]:
                
                if nr < 0 or nr >= rows or nc <0 or nc >= cols:
                    continue
                if grid[nr][nc] != grid[c1r][c1c] + 1:
                    continue
                # if (nr,nc) in seen:
                #     print((nr,nc) , "already visited")
                #     continue
                # seen.add((nr,nc))  commented for part 2
                   
                if grid[nr][nc] == 9:
                    score += 1
                    
                else:
                    dq.append((nr,nc))
                    
    return score






def main():
    
    grid = [[int(char) for char in line.strip()] for line in open("/Users/ganesh.ingale/adventofcode/Day10/example2.txt", "r", encoding="utf-8")]

    rows = len(grid)
    cols = len(grid[0])

    trailheads = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

    print(part_one(grid,trailheads,rows,cols))


if __name__ == "__main__":
    main()