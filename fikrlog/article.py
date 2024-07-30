import os
from slugify import slugify

class Article:
    def __inint__(self, title):
        self.title = title
        self.content = ""
    
    @property 
    def slug(self):
        return slugify(self.title)
    
    def load_content(self):
        with open(f"artice/{self.title}") as file:
            self.content = file.read()
    
    
    def all():
        titles = os.listdir("articles")
        slug_articles = {}
        for title in titles:
            slug = slugify(title)
            article = Article(title)
            article.load_content()
            slug_articles[slug]=article
        return slug_articles