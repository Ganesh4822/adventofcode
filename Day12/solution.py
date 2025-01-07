from collections import deque

def get_regions(garden,rows,cols):
    regions = []
    seen = set()
    for r in range(rows):
        for c in range(cols):
            if (r,c) in seen: continue
            seen.add((r,c))
            field = garden[r][c]
            region = set()
            dq = deque()
            dq.append((r,c))
            while dq:
                cr,cc = dq.popleft()
                region.add((cr,cc))
                for nr,nc in [(cr + 1,cc),(cr - 1,cc),(cr,cc + 1),(cr,cc - 1)] :
                    if nr < 0 or nc  < 0 or nr >=rows or nc >= cols:continue
                    if garden[nr][nc] != field: continue
                    if (nr,nc) in region: continue
                    region.add((nr,nc))
                    seen.add((nr,nc))
                    dq.append((nr,nc))
                
            regions.append(region)
    return regions


def part_one(garden,rows,cols):

    regions = get_regions(garden,rows,cols)
    print(regions)
    total_cost = 0    
    for s in regions:
        area = sum(1 for num in s)
        perimeter = area * 4
        for region in s:
            cr,cc = region[0],region[1]
            for nr,nc in [(cr+1,cc),(cr-1,cc),(cr,cc+ 1),(cr,cc -  1)]:
                if (nr,nc) in s:
                    perimeter -= 1
        
        total_cost += area * perimeter
    return total_cost

def part_two(garden,rows,cols):
    regions = get_regions(garden,rows,cols)

    for s in regions:
        for region in s:
            edges = set()
            cr,cc = region[0],region[1]
            for nr,nc in [(cr+1,cc),(cr-1,cc),(cr,cc+1),(cr,cc-1)]:
                if (nr,nc) in region: continue
                



        

def main():

    garden = [[c for c in line.strip()]for line in open("/Users/ganesh.ingale/adventofcode/Day12/input.txt", "r", encoding="utf-8")]

    rows = len(garden)
    cols = len(garden[0])

    print(part_one(garden,rows,cols))

if __name__ == "__main__":
    main()