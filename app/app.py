from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USERS = {
    "student1": {
        "password": "1234",
        "name": "Rahul Sharma",
        "department": "CSE"
    },
    "student2": {
        "password": "5678",
        "name": "Priya Mehta",
        "department": "IT"
    },
    "student3": {
        "password": "1111",
        "name": "Aman Verma",
        "department": "ECE"
    },
    "student4": {
        "password": "2222",
        "name": "Neha Singh",
        "department": "CSE"
    },
    "student5": {
        "password": "3333",
        "name": "Rohit Patil",
        "department": "MECH"
    },
    "student6": {
        "password": "4444",
        "name": "Sara Khan",
        "department": "IT"
    }
}


@app.route("/")
def login():
    return render_template("login.html", error=None)


@app.route("/login", methods=["POST"])
def login_post():
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
    return render_template("dashboard.html", username=username)


@app.route("/profile/<username>")
def profile(username):
    user = USERS.get(username)
    return render_template("profile.html", user=user)


@app.route("/subjects/<username>")
def subjects(username):
    subjects = ["Math", "DSA", "DBMS", "CN"]
    return render_template("subjects.html", subjects=subjects)


@app.route("/attendance/<username>")
def attendance(username):
    data = {
        "Math": "85%",
        "DSA": "90%",
        "DBMS": "80%",
        "CN": "88%"
    }
    return render_template("attendance.html", data=data)


@app.route("/announcements/<username>")
def announcements(username):
    news = [
        "Exam starts next month",
        "Assignment submission deadline extended",
        "New workshop on AI"
    ]
    return render_template("announcements.html", news=news)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)