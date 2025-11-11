def to_int_divide(a, b):
    try:
        x = int(a)          # may raise ValueError
        return x / b        # may raise ZeroDivisionError
    except ValueError:
        print("Not a valid integer.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print("Division succeeded.")
    finally:
        print("Done cleanup.")

# Example runs:
to_int_divide("12", 3)
to_int_divide("abc", 3)
to_int_divide("12", 0)
