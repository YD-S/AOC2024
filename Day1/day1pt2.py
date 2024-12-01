
left_list = []
right_list = []

def count_occurrences():
    total = 0
    for num in left_list:
        count = right_list.count(num)
        total += count * num
    return total

def main():
    with open("file.txt", "r") as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    left_list.sort()
    right_list.sort()
    total = count_occurrences()
    print(total)

if __name__ == "__main__":
    main()