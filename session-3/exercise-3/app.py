def add_multiple_products(products_list: list, number_of_new_products: int):
    for _ in range(number_of_new_products):
        new_product_name = input("please enter your product's name: ")
        if new_product_name not in products_list:
            products_list.append(new_product_name)
    return products_list
