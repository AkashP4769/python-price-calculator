def calculate_total(price, quantity):
    total = price * quantity
    return total


def main():
    price = 100
    quantity = 2

    total = calculate_total(price, quantity)
    print(f"Total amount: {total}")


main()