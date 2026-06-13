from schema_editor import SchemaEditor

def test_add_table():
    editor = SchemaEditor()
    editor.add_table("users")
    assert len(editor.schema.tables) == 1

def test_add_column():
    editor = SchemaEditor()
    editor.add_table("users")
    editor.add_column("users", "id", "integer")
    assert len(editor.schema.tables[0].columns) == 1

def test_add_relationship():
    editor = SchemaEditor()
    editor.add_table("users")
    editor.add_relationship("users", "orders")
    assert len(editor.schema.tables[0].relationships) == 1

def test_validate():
    editor = SchemaEditor()
    editor.add_table("users")
    editor.add_column("users", "id", "integer")
    assert editor.validate() == True

def test_export():
    editor = SchemaEditor()
    editor.add_table("users")
    editor.add_column("users", "id", "integer")
    editor.add_column("users", "name", "varchar(255)")
    migration_file = editor.export()
    assert "-- Generated migration file" in migration_file
    assert "CREATE TABLE users" in migration_file
    assert "id integer" in migration_file
    assert "name varchar(255)" in migration_file
