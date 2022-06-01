def add_product(products_list):
    new_product_name = input('please input your product name: ')
    if new_product_name in products_list:
        return products_list
    products_list.append(new_product_name)
    return products_list
