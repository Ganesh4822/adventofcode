import heapq

#to move clockwise or anticlockwise we can just swap the row, col and chnage the sign 
#exm suppose we are moving -1,0 (in the up direction) suppose we want to turn clockwise(right direction)
#swap row , col  = col , -row which is (0 , 1)
#for anticlockwise movement move row , col = -col , row 



#following code snippet follows djiktras algorithm to calculate the shortest path
#We store (cost to reach the point , coordimates , directions)
#we start from the starting point as it has cost = 0
#We explore all the vertices from this point and get the next point which has lowest cost using priority queue
#and we add this in a dictionary as we have already passed this point with minimum cost.
#Then we visit all the adjecent point from this vertex to update their cost and add it in the heap.
#Once we reach the end point with minimum cost we return 
#https://www.youtube.com/watch?v=EFg3u_E6eHU (djiktras explanation)

def part_one(grid,rows,cols,rs,cs):
    pq = [(0,rs,cs,0,1)] #(cost, row , col , next_r , next_col)

    seen = {(rs,cs,0,1)}
    tiles = set()
    while pq:
        cur_cost,r,c,dr,dc = heapq.heappop(pq)
        seen.add((r,c,dr,dc))
        tiles.add((r,c))
        if grid[r][c] == "E":
            return len(tiles)
        for next_cost, nr,nc,ndr,ndc in [(cur_cost + 1, r  + dr , c  + dc , dr , dc),
                                         (cur_cost + 1000, r  , c  , dc , -dr),
                                         (cur_cost + 1000, r  , c  , -dc , dr)]:
            if grid[nr][nc] == "#":continue
            if(nr,nc,ndr,ndc ) in seen:continue
            heapq.heappush(pq,(next_cost, nr,nc,ndr,ndc))
 
def main():
    path = "/Users/ganesh.ingale/adventofcode/Day16/example.txt"
    
    grid = [[c for c in line.strip()] for line in open(path,"r",encoding="utf-8")]
    
    rows  = len(grid)
    cols = len(grid[0])
    flag = True
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                flag = False
                break
        if not flag:
            break
    print(part_one(grid, rows , cols , r,c))
    
if __name__ == "__main__":
    main()