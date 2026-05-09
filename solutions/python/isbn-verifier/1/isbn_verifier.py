def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    if not isbn[:-1].isdigit():
        return False

    if not (isbn[-1].isdigit() or isbn[-1] == "X"):
        return False

    total = 0

    for i, c in enumerate(isbn):
        value = 10 if c == "X" else int(c)
        total += value * (10 - i)

    return total % 11 == 0