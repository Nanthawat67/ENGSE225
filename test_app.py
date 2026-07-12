from inventory import Inventory


def test_add_product():
    inv = Inventory()

    inv.add_product("Mouse", 200, 5)

    assert "Mouse" in inv.products


def test_update_product():
    inv = Inventory()

    inv.add_product("Keyboard", 500, 10)
    inv.update_product("Keyboard", 20)

    assert inv.products["Keyboard"]["stock"] == 20


def test_remove_stock():
    inv = Inventory()

    inv.add_product("Monitor", 5000, 5)

    result = inv.remove_stock("Monitor", 2)

    assert result is True
    assert inv.products["Monitor"]["stock"] == 3


def test_inventory_value():
    inv = Inventory()

    inv.add_product("Laptop", 20000, 2)

    assert inv.total_value() == 40000


def test_wrong_stock():
    inv = Inventory()

    inv.add_product("Phone", 10000, 1)

    result = inv.remove_stock("Phone", 5)

    assert result is False
