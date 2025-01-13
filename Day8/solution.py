import itertools







def part_one(input_dict,limit):
    antinodes_cnt = set()

    for key,value in input_dict.items():
        print(value)
        line_combos = list(itertools.combinations(value,2))
        for ops in line_combos:
            node1 = ops[0]
            node2 = ops[1]
            differ = tuple(a-b for a,b in zip(node2,node1))
            # print(differ)
            antinode1 = tuple(a-b for a,b in zip(node1,differ))
            # print(antinode1)
            if antinode1[0] >= 0 and antinode1[1] >= 0 and antinode1[0] < limit and antinode1[1] < limit:
                antinodes_cnt.add(antinode1)
            antinode2 = tuple(a+b for a,b in zip(node2,differ))
            # print(antinode2)
            # print("heyyyy")
            if antinode2[0] >= 0 and antinode2[1] >= 0 and antinode2[0] < limit and antinode2[1] < limit:
                antinodes_cnt.add(antinode2)
    # set_anti = set(antinodes_cnt)
    return  len(antinodes_cnt)


def part_two(input_dict,limit):
    antinodes_cnt = set()

    for key,value in input_dict.items():
        # print(value)
        line_combos = list(itertools.combinations(value,2))
        # print(line_combos)
        for ops in line_combos:
            node1 = ops[0]
            node2 = ops[1]
            differ = tuple(a-b for a,b in zip(node2,node1))
            antinodes_cnt.add(node1)
            antinodes_cnt.add(node2)
            # print(differ)
            while True:
                antinode1 = tuple(a-b for a,b in zip(node1,differ))
                if antinode1[0] >= 0 and antinode1[1] >= 0 and antinode1[0] < limit and antinode1[1] < limit:
                    antinodes_cnt.add(antinode1)
                    node1 = antinode1
                else:
                    break

            while True:
                antinode2 = tuple(a+b for a,b in zip(node2,differ))
                if antinode2[0] >= 0 and antinode2[1] >= 0 and antinode2[0] < limit and antinode2[1] < limit:
                    antinodes_cnt.add(antinode2)
                    node2 = antinode2
                else:
                    break    
            
            # print(antinode2)
            # print("heyyyy")
            
    # set_anti = set(antinodes_cnt)
    return  len(antinodes_cnt)



def main():
    input_data = []
    input_dict = {}
    row = 0 
    col = 0
    with open("/Users/ganesh.ingale/adventofcode/Day8/example.txt", "r", encoding="utf-8") as f:
        for idx,line in enumerate(f):
            row  = len(line)
            for jdx,c in enumerate(line):
                if c == '\n':
                    break
                if c == '.':
                    continue
                else:
                    if c not in  input_dict:
                        input_dict[c] = []
                        input_dict[c].append((idx,jdx))
                    else:
                        input_dict[c].append((idx,jdx))
    print(row)  
    count = 0          
    count = part_two(input_dict,row)
    print(count)

    # for row in range(len(input_data)):
    #     for col in range(len(input_data[0])):
    #         if input_data[row][col] != '.' and input_data[row][col] != '#':
            
    #             if input_data[row][col] not in input_dict:
    #                 input_dict[input_data[row][col]] = []    
    #             input_dict[input_data[row][col]].append((row,col))

if __name__ == "__main__":
    main()