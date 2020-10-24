from flask import Blueprint, jsonify, request
from . import db 
from .models import Algorithm
from werkzeug.utils import secure_filename
import json

main = Blueprint('main', __name__)

@main.route('/add_algorithm', methods=['POST'])
def add_algorithm():
    algo_data = request.form
    selectedFile = request.files['selectedFile']
    filename = "XXXX.txt"
    selectedFile.save(filename)

    new_algo = \
        Algorithm(
            name = algo_data['name'],
            type = algo_data['type'],
            description = algo_data['description'],
            challenge = algo_data['challenge'],
            hint = algo_data['hint'] if 'hint' in algo_data else '',
            plaintext = algo_data['plaintext'],
            ciphertext = algo_data['ciphertext'],
            attempts = 0,
            success = 0
        )
    db.session.add(new_algo)
    db.session.commit()

    return 'Algorithm Added Successfully', 201

@main.route('/algorithms')
def algorithms():
    data = Algorithm.query.all()
    all_rows = [{'id' : row.id, 'name' : row.name, 'type' : row.type, 'description' : row.description, 'challenge' : row.challenge, 'hint' : row.hint, 'plaintext' : row.plaintext, 'ciphertext' : row.ciphertext, 'attempts' : row.attempts, 'success' : row.success} for row in data]
    return json.dumps(all_rows)

@main.route('/get_algo')
def get_algo():
    data = Algorithm.query.get(request.args.get('id'))
    data = {'id' : data.id, 'name' : data.name, 'type' : data.type, 'description' : data.description, 'challenge' : data.challenge, 'hint' : data.hint, 'plaintext' : data.plaintext, 'ciphertext' : data.ciphertext, 'attempts' : data.attempts, 'success' : data.success}
    print(data)
    return json.dumps(data)
