import shopping_card.card as card_module
import shopping_card.item as item
import shopping_card.file_io as file_io
import pytest

@pytest.fixture
def test_card():
    database = "./tests/test_database.json"
    test_card = card_module.Card(database)
    test_card.empty_card()
    return test_card

def test_total_price_of_card(test_card):
    """
    Test the total price of the card
    """
    test_card.add_item_to_card(item.Item(name="apple", type="fruit", _price=10.0))
    test_card.add_item_to_card(item.Item(name="orange", type="fruit", _price=10.0))
    assert test_card.get_total_price() == 20.0

def test_total_item_count(test_card):
    """
    Test the total of the items in the card

    """
    test_card.add_item_to_card(item.Item(name="apple", type="fruit", _price=10.0))
    test_card.add_item_to_card(item.Item(name="orange", type="fruit", _price=10.0))
    assert test_card.get_total_item_count() == 2

def test_add_item_to_card(test_card):
    """
    Test the add_item_to_card method
    """
    test_card.add_item_to_card(item.Item(name="apple", type="fruit", _price=10.0))
    assert test_card.get_total_item_count() == 1

def test_remove_item_from_card_by_query(test_card):
    """
    Test the remove_item_from_card_by_query method
    """
    test_card.add_item_to_card(item.Item(name="apple", type="fruit", _price=10.0))
    test_card.remove_item_from_card_by_query("apple")
    assert test_card.get_total_item_count() == 0

def test_remove_item_by_selection_from_card(test_card, monkeypatch):
    """
    Test the remove_item_by_selection_from_card method
    """
    test_card.add_item_to_card(item.Item(name="apple", type="fruit", _price=10.0))
    test_card.add_item_to_card(item.Item(name="orange", type="fruit", _price=10.0))
    # Simulate user entering "1" to remove the first item
    monkeypatch.setattr("builtins.input", lambda _: "1")

    test_card.remove_item_by_selection_from_card()

    # Check that only 1 item remains
    assert test_card.get_total_item_count() == 1



