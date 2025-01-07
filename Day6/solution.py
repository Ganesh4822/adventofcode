


# def calculate_steps(input_arr,initial_row):
#     row = len(input_arr)
#     col = len(input_arr[0])
#     initial_col = 0
#     flag = 'up'
#     for i in range(col):
#         if(input_arr[initial_row][i]) == '^':
#             initial_col = i
#             flag = 'up'

#     i = initial_row
#     j = initial_col
#     print(i,j)
#     count = 0
#     while(i in range(0,row) and (j in range(0,col))):
#         if(flag == 'up'):
#             if input_arr[i][j] == '#':
#                 flag = 'right'
#                 i = i + 1
#             else:
#                 if(input_arr[i][j] != 'x'):
#                     count = count + 1
#                     input_arr[i][j] = 'x'
#                 i = i - 1

#         elif(flag == 'right'):
            
#             if input_arr[i][j] == '#':
#                 flag = 'down'
#                 j = j - 1
#             else:
#                 if(input_arr[i][j] != 'x'):
#                     count = count + 1
#                     input_arr[i][j] = 'x'
#                 j = j + 1
#         elif(flag == 'down'):
#             if input_arr[i][j] == '#':
#                 flag = 'left'
#                 i = i - 1
#             else:
#                 if(input_arr[i][j] != 'x'):
#                     count = count + 1
#                     input_arr[i][j] = 'x'
#                 i = i + 1
#         else:
#             if input_arr[i][j] == '#':
#                 flag = 'up'
#                 j = j + 1
#             else:
#                 if(input_arr[i][j] != 'x'):
#                     count = count + 1
#                     input_arr[i][j] = 'x'
#                 j = j - 1            
                
#     return count,input_arr

def is_loop(input_arr,row,col):
    nr  = -1
    nc = 0
    rows = len(input_arr)
    cols = len(input_arr[0])
    seen  = set()
    while True:
        seen.add((row,col,nr,nc))
        if row + nr < 0 or row  + nr >= rows or col + nc < 0 or col+ nc >= cols: return False
        if input_arr[row + nr][col + nc] == "#":
            nc,nr = -nr,nc
        else:
            row += nr
            col += nc
        if (row,col,nr,nc) in seen:
            return True
        

def part_two(input_arr,r,c):
    rows = len(input_arr)
    cols = len(input_arr[0])
    count = 0
    for cr in range(rows):
        for cc in range(cols):
            if input_arr[cr][cc] != ".":continue
            input_arr[cr][cc] = "#"
            if(is_loop(input_arr,r,c)):
                count += 1
            input_arr[cr][cc] = "."
    return count
                
            


def part_one(input_arr,r,c):
    row = len(input_arr)
    cols = len(input_arr[0])

    nr = -1
    nc = 0

    seen = {(r,c)}
    while True:
        if r + nr < 0 or r  + nr >= row or c + nc < 0 or c + nc >= cols: break
        if input_arr[r + nr][c + nc] == "#":
            nc,nr = -nr,nc
        else:
            r += nr
            c += nc
        
        seen.add((r,c))
    return len(seen)
        
          

    


    




def main(): 
    input_arr = []
    count = 0
    grid  = [[c for c in line.strip()] for line in open("/Users/ganesh.ingale/adventofcode/Day6/input.txt", "r", encoding="utf-8")]

    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "^":
                break
        else:
            continue
        break
    
    print(part_two(grid,r,c))


        
    #count,input_arr = calculate_steps(input_arr,initial_row)
    #print(count)
    #input_arr[initial_row][initial_col]
    #print(input_arr)

            
if __name__ == "__main__":
    main()

