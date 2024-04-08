"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import Cupcake

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

@app.route('/api/cupcakes', methods=['GET'])
def get_cupcakes():
    cupcakes = Cupcake.query.all()
    cupcakes_data = [{
        'id': cupcakes.id,
        'flavor': cupcakes.flavor,
        'size': cupcakes.size,
        'rating': cupcakes.rating,
        'image': cupcakes.image} for cupcake in cupcakes]
    return jsonify(cupcakes=cupcakes_data)





if __name__ == '__main__':
    app.run(debug=True)