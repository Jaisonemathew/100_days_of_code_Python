from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask import jsonify
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    cafes = Cafe.query.all()
    random_cafe = random.choice(cafes)
    return jsonify({
        'id': random_cafe.id,
        'name': random_cafe.name,
        'map_url': random_cafe.map_url,
        'img_url': random_cafe.img_url,
        'location': random_cafe.location,
        'seats': random_cafe.seats,
        'has_toilet': random_cafe.has_toilet,
        'has_wifi': random_cafe.has_wifi,
        'has_sockets': random_cafe.has_sockets,
        'can_take_calls': random_cafe.can_take_calls,
        'coffee_price': random_cafe.coffee_price,
    })

def cafe_to_dict(cafe):
    return {
         'id': cafe.id,
        'name': cafe.name,
        'map_url': cafe.map_url,
        'img_url': cafe.img_url,
        'location': cafe.location,
        'seats': cafe.seats,
        'has_toilet': cafe.has_toilet,
        'has_wifi': cafe.has_wifi,
        'has_sockets': cafe.has_sockets,
        'can_take_calls':cafe.can_take_calls,
        'coffee_price': cafe.coffee_price,
    }
        

@app.route("/all")
def get_all_cafes():
    cafes = Cafe.query.all()
    cafes_dict = [cafe_to_dict(cafe) for cafe in cafes]
    return jsonify(cafes_dict)

# HTTP GET - Read Record
@app.route("/search")
def search():
    loc = request.args.get('loc')
    cafes=Cafe.query.filter_by(location=loc).all()
    if cafes:
        return jsonify([cafe_to_dict(cafe) for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    name = request.form.get("name")
    map_url = request.form.get("map_url")
    img_url = request.form.get("img_url")
    location = request.form.get("location")
    seats = request.form.get("seats")
    has_toilet = request.form.get("has_toilet") == 'true'
    has_wifi = request.form.get("has_wifi") == 'true'
    has_sockets = request.form.get("has_sockets") == 'true'
    can_take_calls = request.form.get("can_take_calls") == 'true'
    coffee_price = request.form.get("coffee_price")

    if not name or not map_url or not img_url or not location or not seats:
        return jsonify(error={"Missing Data": "All fields except coffee_price are required."}), 400

    new_cafe = Cafe(
        name=name,
        map_url=map_url,
        img_url=img_url,
        location=location,
        seats=seats,
        has_toilet=has_toilet,
        has_wifi=has_wifi,
        has_sockets=has_sockets,
        can_take_calls=can_take_calls,
        coffee_price=coffee_price
    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Cafe added successfully!"}), 201

# HTTP PUT/PATCH - Update Record
@app.route('/update/<int:cafe_id>', methods=['PATCH'])
def update_coffee_price(cafe_id):
    new_price = request.form.get("coffee_price")
    if not new_price:
        return jsonify(error={"Missing Data": "Coffee price is required."}), 400

    cafe = Cafe.query.get(cafe_id)
    if not cafe:
        return jsonify(error={"Not Found": "Cafe not found."}), 404

    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": "Coffee price updated successfully!"}), 200
# HTTP DELETE - Delete Record
@app.route('/delete/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    print(api_key)
    if api_key == "key":
        cafe = Cafe.query.get_or_404(cafe_id)
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Unauthorized": "Invalid API key."}), 403
    
if __name__ == '__main__':
    app.run(debug=True)
