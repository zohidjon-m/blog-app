from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("add.html")

@app.route("/add", methods =["POST","GET"] )
def adder():
    a = request.form.get("a", "")
    b = request.form.get("b", "")

    a = int(a)
    b = int(b)
    result = a+b
    
    return render_template("result.html", result = result)

if __name__ == "__main__":
    app.run(port=4200, debug = True)