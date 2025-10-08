def divide(a: int, b: int):
    try:
        result: int = a / b
    except ZeroDivisionError as error:
        return f"Error : {error}"
    else:
        return result
    finally:
        print("Division attempted")
