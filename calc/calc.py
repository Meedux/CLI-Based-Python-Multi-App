
def calculate():
    text = input("Type an expression: ")

    try:
        res = eval(text, {"__builtins__": None}, {})
        print(f"Result: {res}")
    except SyntaxError:
        print("Error: Invalid mathematical expression syntax.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except NameError:
        print("Error: Undefined variable or character used.")
    except TypeError:
        print("Error: Incompatible data types in calculation.")
    except OverflowError:
        print("Error: Result is too large to calculate.")
    except Exception as e:
        print(f"Calculation Error: {e}")