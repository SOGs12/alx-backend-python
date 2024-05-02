#!/usr/bin/env python3

def add(a: float, b: float) -> float:
    """
    Add two float numbers and return the sum.

    Args:
        a: First float number.
        b: Second float number.

    Returns:
        The sum of the two input numbers.
    """
    # Calculate the sum of a and b
    return a + b

# For testing the function
if __name__ == "__main__":
    # Test the add function
    result = add(1.11, 2.22)
    print(result == 1.11 + 2.22)
    print(add.__annotations__)
