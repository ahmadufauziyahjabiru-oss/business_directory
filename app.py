from flask import Flask, render_template, request, redirect
from models import Business

app = Flask(__name__)

business_list = []
recent_stack = []

@app.route("/")
def home():
    return render_template("home.html", businesses=business_list, recent=recent_stack)


@app.route("/add", methods=["GET", "POST"])
def add_business():
    if request.method == "POST":
        name = request.form["name"]
        location = request.form["location"]

        new_business = Business(name, location)

        business_list.append(new_business)

        recent_stack.append(new_business)

        if len(recent_stack) > 5:
            recent_stack.pop(0)

        return redirect("/")

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)