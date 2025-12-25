# ****************************************************
# Sanjay N Thacker
# sanjaythacker@hotmail.com
# ****************************************************
# The Fizz Buzz coding example:
# https://k3no.medium.com/fizz-buzz-in-python-2edea331d715

import sys

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
    """Run test cases for the fizzbuzz function and display detailed results"""
    test_cases = [
        (1, "1 is not a multiple of 3 or 5"),
        (3, "3 is a multiple of 3"),
        (5, "5 is a multiple of 5"),
        (15, "15 is a multiple of both 3 and 5"),
        (30, "30 is a multiple of both 3 and 5"),
        (7, "7 is not a multiple of 3 or 5"),
        (9, "9 is a multiple of 3"),
        (10, "10 is a multiple of 5"),
        (-3, "-3 is a multiple of 3"),
        (-5, "-5 is a multiple of 5"),
        (-15, "-15 is a multiple of both 3 and 5")
    ]
    
    print("\nRunning test cases...\n")
    print("Test # | Input | Expected Output | Status")
    print("-" * 50)
    
    passed = 0
    for i, (num, expected) in enumerate(test_cases, 1):
        try:
            result = fizzbuzz(num)
            status = "PASSED" if result == expected else "FAILED"
            if status == "PASSED":
                passed += 1
            print(f"{i:6d} | {num:5d} | {expected:30} | {status}")
            if status == "FAILED":
                print(f"       Expected: {expected}")
                print(f"       Got:      {result}")
        except Exception as e:
            print(f"{i:6d} | {num:5d} | {'Error!':30} | ERROR")
            print(f"       Error: {str(e)}")
    
    total = len(test_cases)
    print("\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
    if passed == total:
        print("All tests passed successfully!")
    else:
        print(f"{total - passed} tests failed")
    print("=" * 50)
    
    # Wait for user to press Enter
    input("\nPress Enter to continue...")

def get_user_input():
    """Get and validate user input in a loop until valid input or exit"""
    while True:
        user_input = input("\nEnter a number (or 'test' to run tests, 'exit' to quit): ").strip().lower()
        
        if user_input == "exit":
            print("Exiting program. Goodbye!")
            sys.exit(0)
        elif user_input == "test":
            test_fizzbuzz()
            continue
        elif user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            number = int(user_input)
            if number == 0:
                print("\nError: 0 is not a valid input.")
                print("Please enter a number less than or greater than 0.")
                print("Enter 'test' to run test cases or 'exit' to quit.")
                continue
            return number
        else:
            print(f"\nError: Invalid input '{user_input}'")
            print("Please enter a valid number, 'test', or 'exit'.")

def print_usage():
    """Print usage instructions"""
    print("\nFizzBuzz Program")
    print("-" * 40)
    print("Usage:")
    print("  python fizzBuzz.py               # Print FizzBuzz for numbers 1-100")
    print("  python fizzBuzz.py test          # Run test cases")
    print("  python fizzBuzz.py <number>      # Evaluate a specific number")
    print("  python fizzBuzz.py               # Start interactive mode")
    print("\nInteractive Mode Commands:")
    print("  <number>    Check if number is divisible by 3 or 5")
    print("  test        Run test cases")
    print("  exit        Exit the program")
    print("  help        Show this help message")
    print("\nExamples:")
    print("  python fizzBuzz.py 15            # Check if 15 is divisible by 3 or 5")
    print("  python fizzBuzz.py test          # Run test suite")
    print("  python fizzBuzz.py -9            # Check a negative number")

def interactive_mode():
    """Run the program in interactive mode"""
    print("\nFizzBuzz Interactive Mode")
    print("-" * 40)
    print("Enter a number to check, or type 'test', 'help', or 'exit'")
    print("Type 'exit' at any time to quit.\n")
    
    while True:
        try:
            number = get_user_input()
            print(fizzbuzz(number))
        except KeyboardInterrupt:
            print("\n\nExiting program. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            continue

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments: start interactive mode
        interactive_mode()
    elif len(sys.argv) == 2:
        # One argument provided
        arg = sys.argv[1].lower()
        if arg in ["help", "-h", "--help"]:
            print_usage()
        elif arg == "test":
            test_fizzbuzz()
        elif arg.isdigit() or (arg[0] == '-' and arg[1:].isdigit()):
            # Handle both positive and negative integers
            number = int(arg)
            if number == 0:
                print("\nError: 0 is not a valid input.")
                print("Starting interactive mode...\n")
                interactive_mode()
            else:
                print(fizzbuzz(number))
        else:
            print(f"\nError: Invalid argument '{arg}'")
            print_usage()
            sys.exit(1)
    else:
        print("\nError: Too many arguments")
        print_usage()
        sys.exit(1)
