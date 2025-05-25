from lib.models.magazine import Magazine

def test_magazine_save_and_find():
    m = Magazine(name="Test Mag", category="Tech")
    m.save()
    fetched = Magazine.find_by_id(m.id)
    assert fetched.name == "Test Mag"
