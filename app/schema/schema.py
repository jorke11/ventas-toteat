def individual_serial(product) -> dict:
    print(product)
    return {
        # "id": str(product["id"]),
        "name": str(product["name"]),
        "age": product["age"],
    }


def list_serial(products) -> list:
    return [individual_serial(product) for product in products]
