# ****************************************************
# Sanjay N Thacker
# sanjaythacker@hotmail.com
# ****************************************************
# The Fizz Buzz coding example:
# https://k3no.medium.com/fizz-buzz-in-python-2edea331d715

def fizzbuzz(n):
    """
    Determines the FizzBuzz value for a given number.
    
    Args:
        n (int): The number to evaluate
        
    Returns:
        str: A string describing the number's FizzBuzz status
             - "n is a multiple of both 3 and 5" if divisible by both 3 and 5
             - "n is a multiple of 3" if divisible by 3 only
             - "n is a multiple of 5" if divisible by 5 only
             - "n is not a multiple of 3 or 5" otherwise
    """
    if n % 3 == 0 and n % 5 == 0:
        return f"{n} is a multiple of both 3 and 5"
    elif n % 3 == 0:
        return f"{n} is a multiple of 3"
    elif n % 5 == 0:
        return f"{n} is a multiple of 5"
    else:
        return f"{n} is not a multiple of 3 or 5"

def test_fizzbuzz():
    """Test cases for the fizzbuzz function"""
    test_cases = [
        (1, "1 is not a multiple of 3 or 5"),
        (3, "3 is a multiple of 3"),
        (5, "5 is a multiple of 5"),
        (15, "15 is a multiple of both 3 and 5"),
        (30, "30 is a multiple of both 3 and 5"),
        (7, "7 is not a multiple of 3 or 5"),
        (9, "9 is a multiple of 3"),
        (10, "10 is a multiple of 5")
    ]
    
    for num, expected in test_cases:
        result = fizzbuzz(num)
        assert result == expected, f"Test failed for {num}. Expected: {expected}, Got: {result}"
    print("All tests passed!")

if __name__ == "__main__":
    # Run the test cases
    test_fizzbuzz()
    
    # Original functionality: print FizzBuzz for numbers 1-100
    for i in range(1, 101):
        print(fizzbuzz(i))
