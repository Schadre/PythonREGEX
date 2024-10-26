import re

def extract_product_info(data):
    
    product_pattern = r"Product ID: (\d+), Name: (.*?), Category: (.*?), Price: \$(\d+\.\d+)"

    try:
        products = re.findall(product_pattern, data)
        product_list = []
        for product in products:
            product_dict = {
                "ID" : product[0],
                "Name": product[1],
                "Category": product[2],
                "Price": product[3]
            }
            product_list.append(product_dict)
        return product_list

    except Exception as e:
        print("An error occurred:", e)
        return []

data = """ Product ID: 1001, Name: Alpha Widget, Category: Widgets, Price: $19.99
            Product ID: 1002, Name: Beta Widget, Category: Widgets, Price: $29.99 
            Product ID: 1003, Name: Gamma Gadget, Category: Gadgets, Price: $9.99"""

product_info = extract_product_info(data)
for product in product_info:
    print(f'Product ID: {product["ID"]}, Name: {product["Name"]}, Category: {product["Category"]}, Price: ${product["Price"]}')
