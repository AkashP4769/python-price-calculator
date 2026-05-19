def calculate_total(price, quantity, discount=0):
    total = price * quantity
    total -= total * (discount / 100)
    return total


def main():
    price = 100
    quantity = 2

    total = calculate_total(price, quantity, discount=10)
    print(f"Total amount: {total}")


main()