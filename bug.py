def function_with_uncommon_error(x, y):
    if x == 0:
        return 1 / x  # ZeroDivisionError
    elif y < 0:
        return x ** y # Raises exception if y is a negative float
    else:
        return x + y

# Example usage (uncomment to test)
# print(function_with_uncommon_error(0, 5))
# print(function_with_uncommon_error(5, -2.5))