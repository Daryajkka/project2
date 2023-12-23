from user_func import add_product, search_product, add_to_cart, calculate_total, apply_discount, process_payment
products = []
# Основной код для работы с командами пользователя
cart = {}
while True:
    command = input("Введите команду: ")

    if command == "Добавить товар":
        name = input("Введите название товара: ")
        price = input("Введите цену товара: ")
        quantity = input("Введите количество товара: ")
        add_product(name, price, quantity)
    elif command == "Поиск":
        product_name = input("Введите название товара: ")
        search_product(product_name)
    elif command == "add_to_cart":
        product_name = input("Введите название товара: ")
        quantity = int(input("Введите количество: "))
        add_to_cart(product_name, quantity, cart)
    elif command == "calculate_total":
        total = calculate_total(cart, products)
        print(f"Итоговая сумма: {total}")
        discount = int(input("Введите скидку (если нет, введите 0): "))
        total_with_discount = apply_discount(total, discount)
        print(f"Итоговая сумма с учетом скидки: {total_with_discount}")
    elif command == "process_payment":
        payment_amount = float(input("Введите сумму оплаты: "))
        print(process_payment(total_with_discount, payment_amount))
        break # Завершение программы после обработки платежа
    else:
        print("Неизвестная команда.")


