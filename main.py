def calculate_total(price, quantity, tax=0):
    total = price * quantity
    total += total * tax / 100
    return total


def main():
    price = 100
    quantity = 2

    total = calculate_total(price, quantity, tax=10)
    print(f"Total amount: {total}")


main()