def function_with_uncommon_error(x, y):
    try:
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        elif y < 0 and isinstance(y, float):
            raise ValueError("Cannot raise a float to a negative power.")
        else:
            return x + y
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None  # Or handle the error as needed
    except ValueError as e:
        print(f"Error: {e}")
        return None  # Or handle the error as needed

# Example usage
print(function_with_uncommon_error(0, 5))
print(function_with_uncommon_error(5, -2.5))
print(function_with_uncommon_error(5, -2))