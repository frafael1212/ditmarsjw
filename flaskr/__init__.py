#imports
from flask import Flask, request, abort, json, jsonify, render_template, redirect
from flask_migrate import Migrate
from flask_cors import CORS
from models import Publisher, setup_db

#variables
app = Flask(__name__)
db = setup_db(app)
migrate = Migrate(app, db)

# GETPUBS
def getPubs():
    query = Publisher.query.all()
    formatted_publishers = [q.format() for q in query]
    return formatted_publishers

# DECORATORS
@app.route('/')
def hello():
    return render_template('index.html')

# PUBLISHER
@app.route('/publisher', methods=['GET'])
def showPubs():
    formatted_publishers = getPubs()
    return render_template('publisher.html', publishers = formatted_publishers)
        
@app.route('/publisher', methods=['POST'])
def addPub():
    body = request.get_json()
    fname = body.get('fname')
    lname = body.get('lname')
    email = body.get('email')
    gender = body.get('gender')
    privilege = body.get('privilege')
    isPioneer = body.get('pioneer')
    pioneer = False
    if(isPioneer == 'yes'):
        pioneer = True
    new_publisher = Publisher(
        email = email,
        fname = fname,
        lname = lname,
        gender = gender,
        privilege = privilege,
        pioneer = pioneer
    )
    Publisher.insert(new_publisher)
    return jsonify({
        'success': 'True'
    }),200
@app.route('/publisher/<int:p_id>', methods=['DELETE'])
def delPub(p_id):
    publisher = Publisher.query.filter(Publisher.id == p_id).one_or_none()
    if publisher == None:
        return jsonify({
            'Message': 'This record does not exist'
        }),404
    publisher.delete()
    return jsonify({
        'status': 'Delete Successful'
    }),200
@app.route('/publisher/<int:p_id>', methods=['PATCH'])
def del_updPub(p_id):
    publisher = Publisher.query.filter(Publisher.id == p_id).one_or_none()
    if publisher == None:
        return jsonify({
            'Message': 'This record does not exist'
        }),404
    body = request.get_json()
    publisher.fname = body.get('fname')
    publisher.lname = body.get('lname')
    publisher.email = body.get('email')
    publisher.gender = body.get('gender')
    publisher.privilege = body.get('privilege')
    isPioneer = body.get('pioneer')
    publisher.pioneer = False
    if(isPioneer == 'yes'):
        publisher.pioneer = True
    Publisher.patch(publisher)
    return jsonify({
        'status': 'Record was updated successfully!'
    }),200
@app.route('/reports')
def reports():
    return render_template('/reports.html')
@app.route('/checkbox')
def checkbox():
    result = request.form['checkbox']
    print(result)
@app.route('/jstest')
def jstest():
    return render_template('jstest.html')
