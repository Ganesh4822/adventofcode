





def part_one(input_keys,input_locks):
    res = 0
    for key in input_keys:
        for lock in input_locks:
            flag = True
            for i in range(5):
                if key[i] + lock[i] <= 5:
                    continue
                else:
                    flag = False 
                    break
            if flag:
                res += 1
    return res
            
             



def get_column_sum(input_arr):
    input_col_sum = []
    for i in range(0,len(input_arr),5):
        group = input_arr[i:i + 5]
        group_sum = [0] * len(group[0])
        for row in group:
            for j,c in enumerate(row):
                if c == '#':
                    group_sum[j] += 1
        input_col_sum.append(group_sum)    
    return input_col_sum



def main():
    input_locks = []
    input_keys = []
    with open("/Users/ganesh.ingale/adventofcode/Day25/input.txt", "r", encoding="utf-8") as f:
        flag = 1
        key_flag = 0
        lock_flag = 0
        count = 0
        for line in f:
            
            if line.startswith('\n'):
                flag = 1
                key_flag = 0
                lock_flag = 0
                count = 0
                continue
            elif flag == 1 and line.startswith('.'):
                print("key")
                key_flag = 1
                flag = 0
                continue
            elif flag == 1 and line.startswith('#'):
                print("lock")
                lock_flag = 1
                flag = 0
                continue
            
            if key_flag == 1:
                count = count + 1
                if count < 6:
                    input_keys.append(line.strip())
            else:
                count = count + 1
                if count < 6:
                    input_locks.append(line.strip())
    


    input_keys_sum = []
    input_locks_sum = []

    input_keys_sum = get_column_sum(input_keys)
    input_locks_sum = get_column_sum(input_locks)

    print(part_one(input_keys_sum,input_locks_sum))

    





if __name__ == "__main__":
    main()