


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

def part_one(input_arr):
    row = len(input_arr)
    col = len(input_arr[0])
    count = 0
    turns = [(0,-1),(1,0),(0,1),(-1,0)]


    




def main(): 
    input_arr = []
    count = 0
    with open("/Users/ganesh.ingale/adventofcode/Day6/example.txt", "r", encoding="utf-8") as f:
        row = 0
        initial_row = 0
        for line in f:
            arr = []
            row = row + 1
            for c in line:
                if c == '\n':
                    break
                if (c == '>' or c == '<' or c == '^' or c == 'V'):
                    initial_row = row - 1
                arr.append(c)

            input_arr.append(arr)

        
    #count,input_arr = calculate_steps(input_arr,initial_row)
    #print(count)
    #input_arr[initial_row][initial_col]
    #print(input_arr)

            
if __name__ == "__main__":
    main()

