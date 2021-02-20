
def decimal_to_binary(decimal_number):
    binary_list = []
    while decimal_number > 0:
        binary_number = decimal_number % 2
        binary_list.append(binary_number)
        decimal_number //= 2
    binary_list.reverse()
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


binary_to_decimal([1, 1, 0, 0, 1])


def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    pass


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    pass


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    pass


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass
