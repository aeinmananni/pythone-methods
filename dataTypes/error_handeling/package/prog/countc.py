def countc(s: str, c: str) -> int:
    found: int = 0
    for this_cahr in s:
        if this_cahr == c:
            found += 1
    return found


result: int = countc("ayin mannani", "n")
print("Result Found : ", result)
