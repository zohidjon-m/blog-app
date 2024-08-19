import hashlib
from flask import (
    Flask,
    render_template, 
    request, 
    session, 
    # make_response, 
    redirect
)
from article import Article
app = Flask(__name__)

articles = Article.all()
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
    return "loged out"
    
    
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

    return "Submitted"



# @app.route("/set-session")
# def set_session():
#     session["user_id"] = 54
#     return "session set"

# @app.route("/get-session")
# def get_session():
#     return f"user_id = {session['user_id']}"

# @app.route("/first-time")
# def first_time():
#     if 'seen' not in request.cookies:
#        response = make_response("you are new here")
#        response.set_cookie("seen", "1")
#        return response
   
#     seen = int(request.cookies["seen"])
#     response = make_response(f"I have seen you before {seen} times")
#     response.set_cookie("seen", str(seen+1))
#     return response

if __name__ == "__main__":
    app.run(port=4444, debug=True)

