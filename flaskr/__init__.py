#imports
from flask import Flask, request, abort, json, jsonify
from models import setup_db, Publisher

#app
app = Flask(__name__)
setup_db(app)


@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello World!'
    })

#Publisher Methods
#POST
@app.route('/publisher', methods=['POST','GET'])
def get_addPub():
    if request.method == 'POST':
        body = request.get_json()
        email = body.get('email')
        fname = body.get('fname')
        lname = body.get('lname')
        try:
            new_publisher = Publisher(
                email=email,
                fname=fname,
                lname=lname
            )
            Publisher.insert(new_publisher)
        except BaseException:
            return jsonify({
                'status':'Failed post',
            }), 404
        return jsonify({
            'status': 'Successful!'
        }), 200
    if request.method == 'GET':
        try:
            publishers = Publisher.query.all()
            formatted_publishers = [publisher.format() for publisher in publishers]
        except BaseException:
            jsonify({
                'status': 'Failure'
            }), 404
        return jsonify({
            'publishers':formatted_publishers
        }), 200
@app.route('/publisher/<int:p_id>', methods=['DELETE', 'PATCH'])
def del_updPub(p_id):
    if request.method == 'DELETE':
        try:
            publisher = Publisher.query.filter(Publisher.id == p_id).one_or_none()
            publisher.delete()
            return jsonify({
                'status': 'Delete Successful'
            }), 200
        except BaseException:
            jsonify({
                'status':'Failed to delete!'
            }), 404
    if request.method == 'PATCH':
        body = request.get_json()
        try:
            publishers = Publisher.query.filter()

            # CONTINUE HERE