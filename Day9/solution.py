

# def part_two(explode,input_data,input_spaces):
#     value_dict = dict()
#     for i in range(len(explode)):
#         if(explode[i] in value_dict):
#             value_dict[explode[i]] += 1
#         else:
#             value_dict[explode[i]] = 1
    
#     for idx,num in enumerate(zip(input_data,input_spaces)):
#         for i in range(int(num[0])):
#             explode.append(idx)
            
#         # for i in range(int(num[1])):
#         #     explode.append('.')
        
#     for j in range(int(input_data[-1])):
#         explode.append(len(input_data) - 1)
    

def part_one(input_data,input_spaces):
    explode = []

    for idx,num in enumerate(zip(input_data,input_spaces)):
        for i in range(int(num[0])):
            explode.append(idx)
            
        for i in range(int(num[1])):
            explode.append('.')
            
    
    
    for j in range(int(input_data[-1])):
        explode.append(len(input_data) - 1)
    sum1 = 0
    #sum1 = part_two(explode)
    sum = 0
    i = 0
    while i < len(explode):
        
        try:
            if explode[-1] == '.':
                explode.pop()
            elif explode[i] == '.':
                explode[i] = explode.pop()
                sum += ( i * explode[i])
                i = i + 1
            else:
                sum += ( i * explode[i]) 
                i = i + 1
                continue
        except IndexError:
            break

    print(sum)

def main():
    input_data = []
    input_space = []
    with open("/Users/ganesh.ingale/adventofcode/Day9/example.txt", "r", encoding="utf-8") as f:
        for line in f:
            id = 0
            for idx,c in enumerate(line):
                if c == '\n':
                    break
                if idx % 2 == 0:
                    input_data.append(c)
                else:
                    input_space.append(c)    
    part_one(input_data,input_space)


if __name__ == "__main__":
    main()
