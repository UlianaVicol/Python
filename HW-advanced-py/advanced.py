# advanced errors

product_name  = "\"Toilet Paper\""
product_price = 5.00
delivery_cost = 50

print("##############################")
print(product_name, ":" , product_price)

answer = input(" Do you want to buy? ").lower().strip()

# HW1: upgrade the condition - > "yes", "y" ; "Yes", "Y"
if answer.lower() in ["y","yes"]:
    order_quantity = input(" How many do you want to buy? ")
    order_cost = int(order_quantity) * product_price

    print("------------------------------")
    print(" Order Info ")
    print(product_name, "x", order_quantity, "=", order_cost)

    answer = input(" Do you want delivery? ").lower().strip()
    if answer.lower() in ["y","yes"]:
        order_cost += delivery_cost
        print(" Order cost (including delivery) ", order_cost)
    else:
        print(" Total cost ", order_cost)
else:
    print(" To bad :( ")        
