
import logging
import os, hashlib
from turtle import title
from slugify import slugify
from flask import (Flask, redirect, render_template, request, make_response, session)
from articles import Article
app = Flask(__name__)
app.secret_key = "thisisverysecret"
ARTICLES_DIR = "articles"
#Authentication

#cookies, session
#Hashing, sha256

users = {"admin":"fbccbd47dc3ce5b774ac88fcc9b56240f777f429ffbd18c9e406fd5794ae4d30"}

articles = Article.all()

@app.route("/")
def blog():
    
    return render_template("blog.html", articles = articles)

@app.get("/admin")
def admin_page():
    if "user" in session:
        return "you are now authenticated"

    return render_template("login.html")

@app.post("/admin")
def admin_login():
    username = request.form["username"]
    password = request.form["password"]
   
    if username not in users:
        render_template("login.html", error="usernmae")

    hashed = hashlib.sha256(password.encode()).hexdigest()
    
    if users[username] != hashed:
        return render_template("login.html", error ="username/password incorrect")
    
    session["user"] = username
    
    return "you are now authenticated"

@app.get("/logout")
def logout():
    del session["user"]
    return "logged out"


@app.route("/blog/<slug>")
def article(slug: str):
    if slug not in articles:
        return "article not found", 404
    article = articles[slug]
    return render_template("article.html", article = article )

@app.route("/publish")
def publish():
    if 'user' not in session:
        return redirect('/admin')

    return render_template("publish.html")

@app.post("/publish")
def publish_article():
    title = request.form["title"]
    content = request.form["content"]
    
    slug = slugify(title)
    
    file_path = os.path.join(ARTICLES_DIR, f"{slug}.txt")
    with open(file_path, "w") as file:
        file.write(content)
        
    return f"Article '{title}'has been created successfully!"
@app.route("/set-session")
def set_session():
    session["user_id"] = 1
    return "session set"

@app.route("/get-session")
def get_session():
    return f"user_id = {session['user_id']}"



@app.route("/first-time")
def first_time():
    if ' seen ' not in request.cookies:
        response =  make_response("you are new here")
        response.set_cookie("seen", "1")
        return response
    seen = int(request.cookies['seen'])
    
    response = make_response(f"I have seen you before {seen} times")
    response.set_cookie('seen', str(seen+1))
    return response

    return "i have seen you before"



if __name__ == "__main__":
    app.run(port=4200, debug=True)
