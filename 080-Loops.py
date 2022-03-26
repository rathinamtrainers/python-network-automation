shopping_list = [
    { "name": "Rice", "qty": "2 kgs", "purchased": "NO" },
    { "name": "Wheat", "qty": "10 kgs", "purchased": "NO" },
    {"name": "Apple", "qty": "1 kgs", "purchased": "NO"},
    {"name": "Carrots", "qty": "1.5 kgs", "purchased": "NO"},
    {"name": "Biscuits", "qty": "1 pack", "purchased": "NO"}
]

# for loop
for shopping_item in shopping_list:
    if (shopping_item["purchased"] == "NO"):
        print(f"Purchasing {shopping_item['name']} ")
        shopping_item["purchased"] = "YES"
    else:
        print(f"{shopping_item['name']} is already purchased")
print("=============================")


shopping_list[2]["purchased"] = "NO"

# while loop
count = len(shopping_list)
n = 0
while n < count:
    shopping_item = shopping_list[n]
    if (shopping_item["purchased"] == "NO"):
        print(f"Purchasing {shopping_item['name']} ")
        shopping_item["purchased"] = "YES"
    else:
        print(f"{shopping_item['name']} is already purchased")
    n = n + 1
print("=============================")



