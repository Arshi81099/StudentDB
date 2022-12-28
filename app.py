from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        return render_template("student-details-table.html")

if __name__ == '__main__':
    app.debug=True
    app.run()