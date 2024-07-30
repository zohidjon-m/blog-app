import os
from slugify import slugify
from flask import (Flask, render_template, request)
from article import Article
app = Flask(__name__)

articles = Article.all()

@app.route("/")
def blog():
    return render_template("blog.html", articles = articles)

@app.route("/blog/<slug>")
def article(slug: str):
    article = articles[slug]
    return render_template("article.html", article = article)

@app.route("/blog/new_article")
def new_article():
    return render_template("new_article.html")
if __name__ == "__main__":
    app.run(port=4440, debug=True)
