# Motivation 

# Product Data
# 1. separate variables

#product_name = "Simple product"
#product_price = 100
#Product_avail = True

#if product_price < 500:
#    print("The product", product_name, "is cheap")

# 2. group it as a list 

#product = ["Simple product", True, 100]
#if product[2] < 500:
#    print("The product", product[0], "is cheap")

# 3. group it as a dict

#product = {"name": "Simple product", "avail": True,  "price": 100}

#if product["price"] < 500:
#    print("The product", product["name"], "is cheap")
# dict - best for Mixed
# list - best for homogeniuous

# What about scaling?  -> more products


products = [
    {"name": "Simple product", "avail": True,  "price": 100},  # index 0
    {"name": "Complex product", "avail": False,  "price": 50},  # index 1
    {"name": "Special product", "avail": True,  "price": 1000},   # index 2
    # ....
]

for i in range(len(products)):
    if products[i]["price"] < 500:
        print("The prouct", products[0]["name"], "is cheap")