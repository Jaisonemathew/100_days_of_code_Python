from flask import Flask, render_template,request
from password import emailid,password
import requests
import smtplib

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


@app.route("/contact" ,methods=["GET", "POST"])
def contact():
  if request.method == "POST":
       # getting input with name = fname in HTML form
      data = request.form
      send_email(data["name"], data["email"], data["phone"], data["message"])
      return render_template("contact.html", msg_sent=True)
  return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(emailid,password)
        connection.sendmail(emailid,emailid,email_message)

if __name__ == "__main__":
    app.run(debug=True)