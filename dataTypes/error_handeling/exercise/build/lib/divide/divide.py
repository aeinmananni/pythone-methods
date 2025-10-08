def divide(a: int, b: int):
    try:
        result: int = a / b
    except ZeroDivisionError as error:
        return error
    else:
        return result
    finally:
        return result
