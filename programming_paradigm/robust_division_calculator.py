def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        
        return "Error: Please enter numeric values only."
def main():
    if len(sys.argv) != 3:
        print("Usage: python robust_division_main.py <numerator> <denominator>")
        return
    numerator = sys.argv[1]
    denominator = sys.argv[2]
    print(safe_divide(numerator, denominator))

if __name__ == "__main__":
    main()
