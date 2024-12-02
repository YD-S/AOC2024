data_list = []


def check_data_validity(data):
    if len(data) < 2:
        return True

    is_increasing = data[1] > data[0]

    for i in range(1, len(data)):
        diff = abs(data[i] - data[i - 1])

        if diff < 1 or diff > 3:
            return False

        if is_increasing and data[i] <= data[i - 1]:
            return False
        if not is_increasing and data[i] >= data[i - 1]:
            return False

    return True

def check_data():
    safe_reports = 0
    for data in data_list:
        data = list(data)
        if check_data_validity(data):
            print(f"Safe report: {data}")
            safe_reports += 1
    return safe_reports


def main():
    with open("file.txt", "r") as file:
        for line in file:
            data_list.append(map(int, line.split()))

    safe = check_data()
    print(f"Total number of safe reports: {safe}")


if __name__ == "__main__":
    main()