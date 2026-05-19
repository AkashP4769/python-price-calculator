def calculate_total(price, quantity, tax_percent=5):
    total = price * quantity
    total += total * tax_percent / 100
    return total

def main():
    price = 100
    quantity = 2

    total = calculate_total(price, quantity, tax_percent=10)
    
    print(f"Total amount: {total}")


main()