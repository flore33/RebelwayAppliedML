import json
import os

class FileIO:
    """
    Utility class for file I/O operations
    """

    @staticmethod
    def load_json_files(path: str) -> dict:
        """
        Read a JSON file and return its contents as a dictionary.

        Args:
            path (str): Path to the JSON file.

        Returns:
            dict: Parsed JSON data.
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"No such file: {path}")

        with open(path, "r") as data_file:
            return json.load(data_file)

    @staticmethod
    def print_json_structure(data_file: dict):
        """
        Print the structure of a JSON dictionary assumed to have an "Items" key.

        Args:
            data_file (dict): The loaded JSON content.
        """
        if "Items" not in data_file:
            print("No 'Items' key found in the data.")
            return

        for id, item in data_file["Items"].items():
            print(f"{id}: {item}")
