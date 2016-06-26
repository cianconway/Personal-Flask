from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template ("index.html")

@app.route("/about")
def about():
    return render_template ("about.html")

@app.route("/resume")
def resume():
    return render_template ("resume.html")

if __name__ == "__main__":
    app.run()