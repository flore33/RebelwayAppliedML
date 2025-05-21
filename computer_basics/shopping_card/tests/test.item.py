import shopping_card.item as item

def test_item_price() -> None:
    """
    Test the item price
    """
    item = item.Item(name="apple", type="fruit", _price=10.0)
    assert item.price == 10.0

def test_item_search_string() -> None:
    """
    Test the item search string
    """
    item = item.Item(name="apple", type="fruit", _price=10.0)
    assert item.search_string == "(apple fruit)"

def test_item_id() -> None:
    """
    Test the item id
    """
    item = item.Item(name="apple", type="fruit", _price=10.0)
    assert item.id is not None  

def test_item_quantity() -> None:
    """
    Test the item quantity
    """
    item = item.Item(name="apple", type="fruit", _price=10.0)
    assert item.quantity == 1

def test_item_name() -> None:
    """
    Test the item name
    """
    item = item.Item(name="apple", type="fruit", _price=10.0)
    assert item.name == "apple"

def test_item_type() -> None:
    """
    Test the item type
    """
    item = item.Item(name="apple", type="fruit", _price=10.0)
    assert item.type == "fruit"

def test_item_price() -> None:
    """
    Test the item price
    """
    item = item.Item(name="apple", type="fruit", _price=10.0)
    assert item.price == 10.0
