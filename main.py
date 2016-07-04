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

@app.route("/projects")
def projects():
    return render_template ("projects.html")

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run()