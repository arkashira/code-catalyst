import json
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
    relationships: List[str]

@dataclass
class Schema:
    tables: List[Table]

class SchemaEditor:
    def __init__(self):
        self.schema = Schema(tables=[])

    def add_table(self, name: str):
        self.schema.tables.append(Table(name=name, columns=[], relationships=[]))

    def add_column(self, table_name: str, column_name: str, column_type: str):
        for table in self.schema.tables:
            if table.name == table_name:
                table.columns.append(Column(name=column_name, type=column_type))
                break

    def add_relationship(self, table_name: str, relationship: str):
        for table in self.schema.tables:
            if table.name == table_name:
                table.relationships.append(relationship)
                break

    def validate(self) -> bool:
        # Basic validation, does not cover all PostgreSQL syntax
        for table in self.schema.tables:
            for column in table.columns:
                if not isinstance(column.name, str) or not isinstance(column.type, str):
                    return False
        return True

    def export(self) -> str:
        migration_file = "-- Generated migration file\n"
        for table in self.schema.tables:
            migration_file += f"CREATE TABLE {table.name} (\n"
            for column in table.columns:
                migration_file += f"    {column.name} {column.type},\n"
            migration_file = migration_file.rstrip(",\n") + "\n"
            migration_file += ");\n"
        return migration_file

def main():
    editor = SchemaEditor()
    editor.add_table("users")
    editor.add_column("users", "id", "integer")
    editor.add_column("users", "name", "varchar(255)")
    editor.add_relationship("users", "orders")
    print(editor.export())

if __name__ == "__main__":
    main()
