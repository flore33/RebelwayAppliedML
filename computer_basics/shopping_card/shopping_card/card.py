import json
from dataclasses import dataclass, field
from shopping_card.item import Item
from shopping_card.file_io import FileIO
from shopping_card.random_number_utils import RandomNumberUtils

@dataclass
class Card:
    """
    Class for managing a shopping card (cart).
    """
    database_path: str
    isEmpty: bool = True
    isActive: bool = False
    id: str = field(init=False, default_factory=RandomNumberUtils.generate_random_id)

    def get_all_items(self, verbose=0) -> dict:
        """
        Loads all items from the card's database.
        """
        try:
            data_file = FileIO.load_json_files(self.database_path)
        except Exception as e:
            raise ValueError(f"Failed to load JSON: {e}")

        items = data_file.get("Items", {})
        self.isEmpty = len(items) == 0
        self.isActive = not self.isEmpty

        if verbose:
            FileIO().print_json_structure(data_file)
        
        return data_file

    def search_items(self, query: str) -> list[Item]:
        """
        Searches items in the card by a query string.
        """
        data_file = self.get_all_items()
        matching_items = []

        for item_id, item_data in data_file["Items"].items():
            item = Item(name=item_data["name"], type=item_data["type"],
                        _price=item_data["price"], id=item_id)
            if query.lower() in item.search_string.lower():
                matching_items.append(item)

        if matching_items:
            for item in matching_items:
                print(f"Found: {item.name} {item.type} £{item.price} {item.id}")
        else:
            print(f"No items found for query: {query}")

        return matching_items

    def get_total_item_count(self) -> int:
        """
        Returns the number of items in the card.
        """
        data = self.get_all_items()
        return len(data["Items"])

    def add_item_to_card(self, item: Item):
        """
        Adds an item to the card and updates the database.
        """
        data = self.get_all_items()
        data["Items"][item.id] = {
            "name": item.name,
            "type": item.type,
            "price": item.price
        }

        self._save_data(data)
        self.isEmpty = False
        self.isActive = True

        print(f"Item '{item.name}' added to the card.")

    def remove_item_from_card_by_query(self, query: str):
        """
        Removes items from the card that match a search query.
        """
        data = self.get_all_items()
        items_to_remove = [
            item_id for item_id, item in data["Items"].items()
            if query.lower() in Item(name=item["name"], type=item["type"], _price=item["price"], id=item_id).search_string.lower()
        ]

        if not items_to_remove:
            print(f"No items found for query: {query}")
            return

        for item_id in items_to_remove:
            print(f"Removing: {data['Items'][item_id]['name']}")
            del data["Items"][item_id]

        self._save_data(data)
        self._update_card_status(data)

    def remove_item_by_selection_from_card(self):
        """
        Prompts the user to select and remove an item from the card.
        """
        data = self.get_all_items()
        items = list(data["Items"].items())

        if not items:
            print("No items found in the card.")
            return

        for i, (item_id, item) in enumerate(items, 1):
            print(f"{i}: {item['name']} {item['type']} £{item['price']} {item_id}")

        try:
            selection = int(input("Enter the number of the item to remove: "))
            if not 1 <= selection <= len(items):
                raise ValueError
        except ValueError:
            print("Invalid selection.")
            return

        selected_id = items[selection - 1][0]
        print(f"Removing: {data['Items'][selected_id]['name']}")
        del data["Items"][selected_id]

        self._save_data(data)
        self._update_card_status(data)

    def get_total_price(self) -> float:
        """
        Calculates the total price of all items in the card.
        """
        data = self.get_all_items()
        return sum(item["price"] for item in data["Items"].values())

    def empty_card(self):
        """
        Removes all items from the card.
        """
        data = self.get_all_items()

        if not data["Items"]:
            print("Card is already empty.")
            return

        data["Items"] = {}
        self._save_data(data)

        self.isEmpty = True
        self.isActive = False
        print("Card emptied.")

    def _save_data(self, data: dict):
        """
        Helper function to save the current state to the JSON file.
        """
        with open(self.database_path, "w") as file:
            json.dump(data, file, indent=4)

    def _update_card_status(self, data: dict):
        """
        Updates card status flags based on item count.
        """
        self.isEmpty = len(data["Items"]) == 0
        self.isActive = not self.isEmpty
