import json
import os

class FileIO:
    """
    Utility class for file I/O operations

    read a json file and return its contents as a dictionary
    """

    @classmethod
    def load_json_files(cls, path: str) -> dict:
        """
        Read a JSON file and return its contents as a dictionary.
        """

        if not os.path.exists(path):
            raise FileNotFoundError(f"No such file: {path}")
        
        with open(path, "r") as data_file:
            cls.data_file = json.load(data_file)

        return cls.data_file
        

    @staticmethod
    def save_json_files(data: dict, path: str):
        """
        Save the data to a JSON file
        """
        with open(path, "w") as data_file:
            json.dump(data, data_file, indent=4)
            
#result = FileIO.load_json_files("../database.json")
#print(result)


        
        
