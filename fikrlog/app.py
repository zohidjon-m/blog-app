import hashlib
import sqlite3
from flask import (
    Flask,
    render_template, 
    request, 
    session, 
    # make_response, 
    redirect
)
from article import Article
from sender import sendEmail
from users import user
app = Flask(__name__)

articles = Article.all()
user = user()
app.secret_key = "zohidjon"

users = {
    "admin": '21b2d2fcf4da357d16b101f05ea54bcbe69f9749'
}



@app.route("/")
def main():
    return render_template("main.html")

@app.route("/blog/")
def blog():
    return render_template("blog.html", articles = articles)

@app.get("/admin")
def admin_page():
    if "user" in session:
        return "you are already authenticated"
    
    return render_template("login.html")

@app.post("/admin")
def admin_login():
    username = request.form["username"]
    password = request.form["password"]
    
    if username not in users:
        return render_template("login.html", error = "username/password incorrect")

    hashed = hashlib.sha1(password.encode()).hexdigest()
    
    if users[username] != hashed:
        return render_template("login.html", error="username/password incorrect")
    session["user"] = username
    
    return redirect("/publish")

@app.get("/logout")
def logout():
    del session["user"]
    return render_template("main.html")
    
    
@app.route("/blog/<slug>")
def article(slug: str):
    article = articles[slug]
    return render_template("article.html", article = article)

@app.get("/publish")
def publish_page():
    if "user" not in session:
        return redirect("/admin")
    
    return render_template("publish.html")

@app.post("/publish")
def published():
    title = request.form["title"]
    content = request.form["content"]

    file_path = f"articles/{title}"
    
    with open(file_path, 'w') as file:
        file.write(content)
    
    sendEmail(title, content)

    return "Submitted"
@app.get("/subscribe")
def subscribe_page():
    return render_template("subscribe.html")
@app.post("/subscribe")
def subscribme():
    name = request.form["name"]
    email = request.form["email"]
   
    
    try:
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        cur.execute("INSERT  INTO user_information(name, email) VALUES(?,?)",( name, email))
        con.commit()
        cur.close()
        con.close()
        return f"User {name} has successfully subscribed"
    except sqlite3.IntegrityError:
        return f"This {email} already registered"
        
        

if __name__ == "__main__":
    app.run(port=4444, debug=True)

