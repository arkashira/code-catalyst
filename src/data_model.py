from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Column:
    name: str
    type: str

@dataclass
class Table:
    name: str
    columns: List[Column]

class DataModel:
    def __init__(self):
        self.tables = []

    def add_table(self, table: Table):
        self.tables.append(table)

    def get_tables(self) -> List[Table]:
        return self.tables
