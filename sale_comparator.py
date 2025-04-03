from notification import unwrap_product_string


def create_message(new_products, old_products, url):
    if new_products & old_products:
        new_products_string = unwrap_product_string(new_products)
        old_products_string = unwrap_product_string(old_products)
        print("Sending message about both new and expired products")
        return f"Subject: Update on sales\n\n New products: {new_products_string}\n\n Expired products:{old_products_string} \n\nURL: {url}"

    if new_products and not old_products:
        new_products_string = unwrap_product_string(new_products)
        print("Sending message about new product")
        return f"Subject: New Ibanez guitar at Evenstad Outlet\n\nThere is a new product on Evenstad's outlet page: {new_products_string}. \n There are currently {len(new_products)} guitars out: \n\n{products_string}\n\n URL: {url}"

    if old_products and not new_products:
        old_products_string = unwrap_product_string(new_products)
        print("Sending message about product no longer for sale")
        return f"Subject: Product no longer for sale at Evenstad's Outlet\n\n The product: {old_products_string} is no longer for sale. \n There are currently {len(new_products)} guitars out: \n\n{products_string}\n\n URL: {url}"

    else:
        return


def compare_sales(old_products, new_products):
    new_products = []
    old_products = []
    if old_products == new_products:
        print("No change in the sales.")
        return new_products
    else:
        for product in new_products:
            if product not in old_products:
                new_products.append(product)
        for product in old_products:
            if product not in new_products:
                old_products.append(product)

    return new_products, old_products
