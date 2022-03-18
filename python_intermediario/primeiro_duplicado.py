def find_unique_numbers(numbers: list):
    for number in numbers:
        if number in numbers:
            numbers.remove(number)

    return numbers


if __name__ == "__main__":
    print(find_unique_numbers([1, 2, 1, 3]))
