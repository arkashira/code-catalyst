from src.data_model import DataModel, Table, Column
import pytest

def test_data_model():
    data_model = DataModel()
    table = Table("users", [Column("id", "int"), Column("name", "string")])
    data_model.add_table(table)
    assert len(data_model.get_tables()) == 1
    assert data_model.get_tables()[0].name == "users"
    assert len(data_model.get_tables()[0].columns) == 2
    assert data_model.get_tables()[0].columns[0].name == "id"
    assert data_model.get_tables()[0].columns[1].name == "name"

def test_table():
    table = Table("users", [Column("id", "int"), Column("name", "string")])
    assert table.name == "users"
    assert len(table.columns) == 2
    assert table.columns[0].name == "id"
    assert table.columns[1].name == "name"

def test_column():
    column = Column("id", "int")
    assert column.name == "id"
    assert column.type == "int"
