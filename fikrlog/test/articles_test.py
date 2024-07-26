import pytest
from articles import Article

@pytest.fixture
def article():
    return Article("Test title")


def test_article_init(article):
    #a = Article("Test title")
    assert article.title == "Test title"
    assert article.content == ""
    
def test_article_slug(article):
    assert article.slug == "test-title"
   
def test_article_slug_mock(mocker,article):
    #given
    mock_slugify = mocker.patch('articles.slugify', return_value="slug")
    
    #when   
    got = article.slug
    
    #then
    assert got == "slug"
    mock_slugify.assert_called_with("Test title")