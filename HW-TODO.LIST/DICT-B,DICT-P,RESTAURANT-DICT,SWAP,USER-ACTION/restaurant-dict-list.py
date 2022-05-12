# Data Source - ordered items
# list > dict

data = [    # lavel 0
    {
        "title": "Salad",    # lavel 1
        "price": {
            "amount": 15.00,
            "currency": "MDL"            
            },
            "quantity": 2
    },
    {
        "title": "Soup",
        "price": { 
            "amount": 45.00,
            "currency": "MDL"
        },
        "quantity": 1
    },
    {
        "title": "Bread",
        "price": {
            "amount": 5.00,
            "currency": "MDL"
        },
        "quantity": 10
    },
]
 # Print / Iterate

for i in range(len(data)):
    item = data[i]
    item_cost = item["quantity"] * item["price"]["amount"]
    item_currency = item["price"]["currency"]
    
    out=f'{i+1:2}) {item["title"]:^15} x {item["quantity"]:3} = {item_cost:8.2f}{item_currency}'
    print(out)