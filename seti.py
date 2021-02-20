
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


decimal_to_base(0, 2)


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    pass


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    pass


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass
