def total_joltage(filepath):
    counter = 0
    with open(filepath,'r') as file:
        for line in file:
            line = line.rstrip()
            if line:
                bank = [int(s) for s in line]
                inds = sorted(range(len(line)-1),key=bank.__getitem__,reverse=True)
                bat1 = bank[inds[0]]
                bat2 = max(bank[inds[0]+1:])
                bank_joltage = int(str(bat1) + str(bat2)) 
                counter += bank_joltage
    return counter

if __name__ == "__main__":
    filepath = 'inputs/day3.txt'
    print(total_joltage(filepath))