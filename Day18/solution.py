from collections import deque
from collections import defaultdict



def can_reach(grid,corrupt_coord,simulations,grid_size):

    for i in range(simulations):
        #print(i)
        r,c = corrupt_coord[i]
        grid[c][r] = "#"

    q = deque([(0,0,0)])
    seen = {(0,0)}
    # a = ['.','.','.']
    # st = "\n".join(",".join(c for c in a) for a in grid)
    # print(st)
     
    while q:
        r,c,count = q.popleft()
        for nr,nc in [(r + 1,c), (r-1,c),(r ,c + 1), (r, c - 1)]:
            if nr < 0  or nc < 0 or nr > (grid_size - 1) or nc  > (grid_size - 1): continue
            if grid[nr][nc] == "#":continue
            if (nr,nc) in seen:continue
            if nr ==  nc == (grid_size - 1):
                return count + 1
            seen.add((nr,nc))
            q.append((nr,nc,count + 1))
    return False

def part_two(grid,corrupt_coord,simulations,grid_size):
    #brut force 
    for i in range(simulations):
        ri,ci = corrupt_coord[i]
        grid[ci][ri] = "#"
        q = deque([(0,0)])
        seen = {(0,0)}
        while q:
            flag = 0
            r,c = q.popleft()
            for nr,nc in [(r + 1,c), (r-1,c),(r ,c + 1), (r, c - 1)]:
                if nr < 0  or nc < 0 or nr > (grid_size - 1) or nc  > (grid_size - 1): continue
                if grid[nr][nc] == "#":continue
                if (nr,nc) in seen: continue
                if nr ==  nc == (grid_size - 1):
                    flag = 1
                    break
                seen.add((nr,nc))
                q.append((nr,nc))
            if flag == 1:
                break 
        if flag == 0:
            return (ri,ci)

            
#smarter approach is to use binary search over the list of give range of coordinate to check the cut of faster
def part_two_optmized(grid,corrupt_coord,simulations,grid_size):
    low = 0
    high = simulations 

    while low < high:
        middle  = (low + high) // 2
        if can_reach(grid,corrupt_coord,middle + 1,grid_size):
            low = middle + 1
        else:
            high = middle
    print(corrupt_coord[low])






    

         
            
            
    

def main():
    path = "/Users/ganesh.ingale/adventofcode/Day18/input.txt"
    
    corrupt_coord = [[int(c) for c in line.strip().split(',')] for line in open(path,"r",encoding="utf-8")]
    grid_size = 71
    simulations = len(corrupt_coord)
    print(simulations)
    grid = [['.']* grid_size for _ in range(grid_size)]
    
    # print(part_one(grid,corrupt_coord,simulations,grid_size))
    #print(part_two(grid,corrupt_coord,simulations,grid_size))
    print(part_two_optmized(grid,corrupt_coord,simulations,grid_size))
    
    
if __name__ == "__main__":
    main()