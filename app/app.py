from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user database
USERS = {
    "student1": {
        "password": "1234",
        "department": "CSE",
        "name": "Rahul Sharma"
    },
    "student2": {
        "password": "5678",
        "department": "IT",
        "name": "Priya Mehta"
    }
}

ALLOWED_DEPARTMENTS = ["CSE", "IT"]


@app.route("/")
def login_page():
    return render_template("login.html", error=None)


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = USERS.get(username)

    if user and user["password"] == password:
        return redirect(url_for("dashboard", username=username))
    else:
        return render_template("login.html", error="Invalid credentials")


@app.route("/dashboard/<username>")
def dashboard(username):
    user = USERS.get(username)

    if not user:
        return "User not found"

    dept_allowed = user["department"] in ALLOWED_DEPARTMENTS

    return render_template(
        "dashboard.html",
        username=username,
        user=user,
        dept_allowed=dept_allowed
    )


@app.route("/profile/<username>")
def profile(username):
    user = USERS.get(username)

    if not user:
        return "User not found"

    return render_template("profile.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)