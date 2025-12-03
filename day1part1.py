def get_password(filepath):
    pos = 50
    counter = 0
    with open(filepath,'r') as file:
        for line in file:
            if line.rstrip():
                move = int(line.replace("L","-").replace("R",""))
                pos = (pos + move)%100
                counter += (pos==0)
    return counter

if __name__ == "__main__":
    filepath = 'inputs/day1.txt'
    print(get_password(filepath))