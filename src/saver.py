import json
from pathlib import Path
from threading import Lock

class CommunityDB:
    DATA_FOLDER = Path("data")
    DATA_FOLDER.mkdir(exist_ok=True)

    def __init__(self, community_id: str):
        self.community_id = community_id
        self.lock = Lock()
        self.file_path = self.DATA_FOLDER / f"{community_id}.json"

    # Load the community database
    def load_db(self) -> dict:
        if self.file_path.exists():
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    # Save the community database
    def save_db(self, db: dict):
        with self.lock:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(db, f, indent=4)

    # Get a collection (accounts, characters, etc.)
    def get_collection(self, collection: str) -> dict:
        db = self.load_db()
        return db.get(collection, {})

    # Add or update an item in a collection
    def set_item(self, collection: str, key: str, value: dict):
        db = self.load_db()
        if collection not in db:
            db[collection] = {}
        db[collection][key] = value
        self.save_db(db)

    # Remove an item from a collection
    def remove_item(self, collection: str, key: str):
        db = self.load_db()
        if collection in db and key in db[collection]:
            del db[collection][key]
            self.save_db(db)