
def decimal_to_binary(decimal_number):
    binary_list = []
    if decimal_number > 0:
        while decimal_number > 0:
            binary_number = decimal_number % 2
            binary_list.append(binary_number)
            decimal_number //= 2
        binary_list.reverse()
    elif decimal_number < 0:
        decimal_number = abs(decimal_number)
        while decimal_number > 0:
            binary_number = decimal_number % 2
            binary_list.append(binary_number)
            decimal_number //= 2
        binary_list.reverse()
        binary_list = "-" + str(binary_list)
    else:
        binary_list = [0]
    print(binary_list)


# decimal_to_binary(13)


def binary_to_decimal(binary_digits):
    times = 0
    decimal_number = 0
    for digit in reversed(binary_digits):
        if digit == 1:
            decimal_number += (digit * (2**times))
        else:
            pass
        times += 1
    print(decimal_number)


# binary_to_decimal([1, 1, 0, 0, 1])


def decimal_to_base(decimal_number, destination_base):
    base_list = []
    while decimal_number > 0:
        base_number = decimal_number % destination_base
        base_list.append(base_number)
        decimal_number //= destination_base
    base_list.reverse()
    print(base_list)


# decimal_to_base(13, 2)


def base_to_decimal(digits, original_base):
    times = 0
    decimal_number = 0
    for digit in reversed(digits):
        decimal_number += (digit * (original_base**times))
        times += 1
    print(decimal_number)


# base_to_decimal([2, 4], 8)

# Returns the string representation of an array of digits given in base
def digits_as_string(digits, base):
    for digit in digits:
        if digit > base:
            raise ValueError
    digits = ['A' if num == 10 else 'B' if num == 11 else 'C' if num == 12 else 'D' if num == 13 else 'E' if num == 14 else 'F' if num == 15 else num for num in digits]
    if base > 16:
        raise ValueError
    string_digits = ''.join(str(digit) for digit in digits)
    print(string_digits)


digits_as_string([2, 15, 9, 11], 16)


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass
