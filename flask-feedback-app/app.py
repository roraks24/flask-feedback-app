from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        experience = request.form.get("experience")

        return render_template("thankyou.html", name = name)

    return render_template("feedback.html")

