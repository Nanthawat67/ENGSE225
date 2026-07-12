from inventory import Inventory


inventory = Inventory()

inventory.add_product("Keyboard", 500, 10)

print(inventory.products)
print("Total:", inventory.total_value())
