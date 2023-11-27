from flask import Flask, render_template
import requests

posts=requests.get("https://api.npoint.io/a059da1db75e77b2f515").json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",all_posts=posts)

@app.route('/post/<int:p_id>')
def get_post(p_id):
    return render_template('post.html', post=posts[int(p_id) - 1])

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)