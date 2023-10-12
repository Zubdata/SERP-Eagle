"""This module is used for saving the scraped data"""

import json


class DataSaver:

    def save_data(data):
        
        with open("data output.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)
