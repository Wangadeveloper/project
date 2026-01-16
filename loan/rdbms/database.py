import os
import json
from .executor import execute_sql

class Database:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
        self.tables = {}
        self._load_tables()

    def _table_file(self, table_name):
        return os.path.join(self.data_dir, f"{table_name}.json")

    def _load_tables(self):
        for filename in os.listdir(self.data_dir):
            if filename.endswith(".json"):
                table_name = filename.replace(".json", "")
                path = os.path.join(self.data_dir, filename)
                with open(path, "r", encoding="utf-8") as f:
                    try:
                        self.tables[table_name] = json.load(f)
                    except json.JSONDecodeError:
                        self.tables[table_name] = []

    def save_table(self, table_name):
        path = self._table_file(table_name)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.tables[table_name], f, indent=2)

    def execute(self, sql, params=None):
        if params is None:
            params = []
        rows, updated_table = execute_sql(self, sql.strip(), params)
        if updated_table:
            self.save_table(updated_table)
        return rows, updated_table
