

def part_one(grid,rows,cols):
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "X": continue
            for nr,nc in [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,1),(-1,-1),(1,-1)]:
                if  not  (0 <= r + 3 * nr < rows and 0 <= c +  3 * nc < cols ): continue
                if grid [r + nr][c + nc ] == "M" and grid [r + 2* nr][c + 2 * nc ] == "A" and grid [r + 3 * nr][c + 3 * nc ] == "S":
                    count += 1 
    return count
            
                
def part_two(grid,rows,cols):
    count = 0
    for r in range(1,rows-1):
        for c in range(1,cols - 1):
            if grid[r][c] != "A": continue
            # for nr,nc in [(-1,1),(1,1),(-1,-1),(1,-1)]:
            edge1 = [grid[r-1][c-1],grid[r+1][c+1]]
            edge2 = [grid[r+1][c-1],grid[r-1][c+1]]
            
            if ("".join(edge1) == "MS" or "".join(edge1) == "SM") and ("".join(edge2) == "MS" or "".join(edge2) == "SM"):
                count += 1
            else:
                continue
    return count




def main():

    grid = [[c for c in line.strip()] for line in open("/Users/ganesh.ingale/adventofcode/Day4/input.txt", "r", encoding="utf-8")]
    print(grid)
    rows = len(grid)
    cols = len(grid[0])

    print(part_two(grid,rows,cols))



if __name__ == "__main__":
    main()