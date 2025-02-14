from collections import deque
from collections import defaultdict
import time

def cal_cost_dict(grid,rs,rc):
    q = deque([(rs,rc,0)])
    seen = defaultdict()
    seen[(rs,rc)] = 0
    rows = len(grid)
    cols = len(grid[0])


    # print(grid[rs][rc])
    # print("\n".join(",".join(str(c) for c in rows)for rows in dist))
    # print("\n".join(",".join(c for c in rows)for rows in grid))
    while q:
        cr,cc,cur_cost  = q.popleft()
        for nr,nc in [(cr + 1, cc),(cr - 1, cc),(cr, cc +  1),(cr, cc - 1)]:
            if nr < 0 or nc < 0 or nr >= rows or nc  >= cols:continue
            if grid[nr][nc] == "#":continue
            if (nr,nc) in seen :continue
            seen[(nr,nc)] = cur_cost + 1
            q.append((nr,nc,cur_cost + 1))

    shortcuts = defaultdict()
    for k,v in seen.items():
        r,c = k
        for nr,nc in [(r + 2, c),(r - 2, c),(r, c +  2),(r, c - 2)]:
            if nr < 0 or nc < 0 or nr >= rows or nc  >= cols:continue
            cr = (nr+ r) // 2
            cc = (nc+c) // 2
            if (cr,cc) in shortcuts: continue
            if (nr,nc) in seen and (nr,nc) in seen and  grid[cr][cc] == '#' and (seen[(nr,nc)] - seen[(r,c)] - 2 >= 100 ):
                shortcuts[(cr,cc)] = seen[(nr,nc)] - seen[(r,c)] - 2
    print(len(shortcuts))
    

def cal_cost_grid(grid,rs,cs):
    q = deque([(rs,cs)])
    rows = len(grid)
    cols = len(grid[0])
    dist_grid = [[-1] * cols for _ in range(rows)]
    dist_grid[rs][cs] = 0
    while q:
        cr,cc = q.popleft()
        for nr,nc in [(cr + 1, cc),(cr - 1, cc),(cr, cc +  1),(cr, cc - 1)]: 
            if nr < 0 or nc < 0 or nr >= rows or nc  >= cols:continue
            if grid[nr][nc] == "#":continue
            if dist_grid[nr][nc] != -1 :continue
            dist_grid[nr][nc] = dist_grid[cr][cc]  + 1
            
            q.append((nr,nc))
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":continue
            for nr,nc in [(r + 2, c),(r + 1, c + 1),(r, c +  2),(r - 1, c + 1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc  >= cols:continue
                if grid[r][c] == "#":continue
                if dist_grid[nr][nc] == -1:continue
                if abs(dist_grid[r][c] - dist_grid[nr][nc]) >= 102: 
                    count += 1

    #part2
    count2 = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":continue
            for dist in range(2,21):
                for dr in range(dist + 1):
                    dc  = dist - dr
                    for nr,nc in {(r + dr,c + dc),(r - dr,c + dc),(r + dr,c - dc),(r - dr,c - dc)}:
                        if nr < 0 or nc < 0 or nr >= rows or nc  >= cols:continue
                        if dist_grid[nr][nc] == -1:continue
                        if grid[r][c] == "#":continue
                        if (dist_grid[r][c] - dist_grid[nr][nc]) >= 100 + dist: 
                            count2 += 1
    print(count2)
    #print("\n".join(" , ".join(str(c) for c in rows) for rows in dist_grid))



            


def main():
    path = "/Users/ganesh.ingale/adventofcode/Day20/input.txt"

    grid = [[c for c in line.strip()]for line in open(path,"r",encoding="utf-8")]
    flag = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                flag = 1 
                break
        if flag == 1:
            break
    #print(grid)
    #print("\n".join("".join(c for c in rows)for rows in grid))
    #print(r,c)    
    print(cal_cost_grid(grid,r,c))
        
    


if __name__ == "__main__":
    main()