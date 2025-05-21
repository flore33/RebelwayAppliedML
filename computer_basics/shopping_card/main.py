import shopping_card.card as card
import shopping_card.item as item
import shopping_card.file_io as file_io

__name__ = "__main__"

#the main database for the shopping card to pass to the class
database = "database.json"
my_card = card.Card(database)

#search for items in the card
print("Search for items in the card")
results = my_card.search_items("apple")
print("--------------------------------")

#get the total number of items in the card
print("Total number of items in the card: ")
total_item_count = my_card.get_total_item_count()
print(f"Total number of items in the card: {total_item_count}")
print("--------------------------------")

#Create an Item object so it can be added to the card
print("Create an Item object so it can be added to the card")
print("--------------------------------")
milk = item.Item(name="milk", type="dairy", _price=2.0)
my_card.add_item_to_card(milk)
onion = item.Item(name="onion", type="vegetable", _price=1.0)
my_card.add_item_to_card(onion)

#get the total number of items in the card
print("--------------------------------")
print("Total number of items in the card: ")
print("--------------------------------")
my_card.get_all_items(verbose=1)
print("--------------------------------")

#remove all items by name or type
print("Remove all items by name or type:")
print("--------------------------------")
my_card.remove_item_from_card_by_query("onion")
print("--------------------------------")
print("\n")

#remove a selected item from the card
print("Remove a selected item from the card:")
print("--------------------------------")
my_card.remove_item_by_selection_from_card()
print("--------------------------------")

#print all the current items in the card
print("All the current items in the card:")
print("--------------------------------")
my_card.get_all_items(verbose=1)
print("--------------------------------")

#print the total price of the card
print("Total price of the card:")
print("--------------------------------")
total_price = my_card.get_total_price()
print(f"Total price of the card: £{total_price}")
print("--------------------------------")


