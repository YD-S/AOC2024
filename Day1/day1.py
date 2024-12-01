
left_list = []
right_list = []

def add_lists():
    total = sum(abs(left - right) for left, right in zip(left_list, right_list))
    return total

def main():
    with open("file.txt", "r") as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    left_list.sort()
    right_list.sort()
    total = add_lists()
    print(total)

if __name__ == "__main__":
    main()