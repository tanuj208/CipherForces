from flask import Blueprint, jsonify, request
from . import db 
from .models import Algorithm

main = Blueprint('main', __name__)

@main.route('/add_algorithm', methods=['POST'])
def add_algorithm():
    algo_data = request.get_json()

    new_algo = \
        Algorithm(
            name = algo_data['name'],
            type = algo_data['type'],
            description = algo_data['description'],
            challenge = algo_data['challenge'],
            hint = algo_data['hint'],
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
    algo_list = Algorithm.query.all()
    algorithms = []
    for algo in algo_list:
        algorithms.append(
            {
                'name': algo.name,
                'type': algo.type,
                'description': algo.description,
                'challenge' : algo.challenge,
                'hint' : algo.hint,
                'plaintext' : algo.plaintext,
                'ciphertext' : algo.ciphertext,
                'attempts' : algo.attempts,
                'success' : algo.success,
            }
        )
    return jsonify({'algorithms': algorithms})