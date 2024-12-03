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


def check_with_single_removal(data):
	if check_data_validity(data):
		return True

	for i in range(len(data)):
		test_data = data[:i] + data[i + 1:]
		if check_data_validity(test_data):
			return True

	return False


def main():
	safe_count = 0

	with open("file.txt", "r") as file:
		for line in file:
			if line.strip():  # Skip empty lines
				numbers = list(map(int, line.strip().split()))
				if check_with_single_removal(numbers):
					print(f"Safe (possibly after removal): {numbers}")
					safe_count += 1

	print(f"Total safe sequences: {safe_count}")


if __name__ == "__main__":
	main()