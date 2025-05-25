from lib.models.author import Author

def test_author_save_and_find():
    a = Author(name="Test Author")
    a.save()
    fetched = Author.find_by_id(a.id)
    assert fetched.name == "Test Author"
