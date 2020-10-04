from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_marshmallow import Marshmallow

# App declaration
app = Flask(__name__,
            static_url_path='',
            static_folder='public/static'
            )
# REST API config
api = Api(app)
ma = Marshmallow(app)
# Database initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:123456789@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    """User Model"""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))

    def __repr__(self):
        return '<User %r>' % self.name


class UserSchema(ma.Schema):
    """User Schema"""
    class Meta:
        fields = ('id', 'username')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class IndexView(Resource):
    """Index view"""

    def get(self):
        return {"message": "This is a REST API"}


class UserView(Resource):
    """User view"""

    def get(self):
        """Get all users"""
        users = User.query.all()
        result = users_schema.dump(users)
        return jsonify(result)

    def post(self):
        """Create an user"""
        data = request.get_json()
        user = User(username=data['username'])
        db.session().add(user)
        db.session.commit()

        return {
            "message": "User saved successfully"
        }, 201


api.add_resource(IndexView, '/api')
api.add_resource(UserView, '/api/users')


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
