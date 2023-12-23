# Функция для добавления нового товара

def add_product(name, price, quantity):
    with open('products.txt', 'a', encoding="utf-8") as file:
        file.write(f"{name}, {price}, {quantity}\n")
        print("Товар успешно добавлен в файл.")

# Функция для поиска товара
def search_product(product_name):
     found = False
     with open('products.txt', 'r') as file:
        for line in file:
            name, price, quantity = line.strip().split(', ')
            if name == product_name:
                print(f"Информация о товаре {name}: цена - {price}, количество - {quantity}")
                found = True
                break
            if not found:
                print("Товар не найден.")

# Функция для добавления товара в чек
def add_to_cart(product_name, quantity, cart):
    cart[product_name] = quantity

# Функция для расчета итоговой суммы
def calculate_total(cart, products):
    total = 0
    for product_name, quantity in cart.items():
        if product_name in products:
            total += products[product_name]['price'] * quantity
            return total

# Функция для применения скидки
def apply_discount(total, discount):
    return total * (1 - discount / 100)

# Функция для обработки платежа
def process_payment(total, payment_amount):
    if payment_amount < total:
        return "Недостаточно средств для оплаты"
    change = payment_amount - total
    return f"Спасибо за покупку! Ваша сдача: {change}"