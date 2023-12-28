from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.secret_key = "4pm5gugppwigpi9rir"
Bootstrap5(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///libary.db"
db = SQLAlchemy()
db.init_app(app)


class BookForm(FlaskForm):
    book_name = StringField(label='Book Name', validators=[DataRequired()])
    author_name = StringField(label='Author Name', validators=[DataRequired()])
    rating = SelectField(label='Rating', choices=['1', '2', '3', '4', '5'], validators=[DataRequired()])
    submit = SubmitField(label='Submit')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template('index.html',books=all_books)


@app.route("/add",methods=['GET','POST'])
def add():
    book_form = BookForm()
    if book_form.validate_on_submit():
        with app.app_context():
            new_book=Book(title=book_form.book_name.data,author=book_form.author_name.data,rating=book_form.rating.data)
            db.session.add(new_book)
            db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html',form=book_form)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

