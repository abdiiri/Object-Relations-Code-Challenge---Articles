from lib.models.article import Article

def test_article_save_and_find():
    a = Article(title="Test Article", author_id=1, magazine_id=1)
    a.save()
    fetched = Article.find_by_id(a.id)
    assert fetched.title == "Test Article"
