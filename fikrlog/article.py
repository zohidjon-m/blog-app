import os
import slugify

class Article:
    def __init__(self, title):
        self.title = title
        self.content = ""
    
    @property 
    def slug(self):
        return slugify.slugify(self.title)
    
    def load_content(self):
        with open(f"articles/{self.title}") as file:
            self.content = file.read()
    
    @classmethod
    def all(cls):
        titles = os.listdir("articles")
        slug_articles = {}
        for title in titles:
            slug = slugify.slugify(title)
            article = cls(title)
            article.load_content()
            slug_articles[slug]=article
        return slug_articles