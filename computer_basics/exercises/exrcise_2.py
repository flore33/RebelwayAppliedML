my_card = Card(database_path="my_items.json")
print(my_card.get_total_item_count())

my_card.add_item("apple", 10)
my_card.add_item("banana", 20)
my_card.add_item("orange", 30)

print(my_card.get_total_item_count())
