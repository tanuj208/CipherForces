from flask import Blueprint, jsonify, request
from . import db 
from .models import Algorithm
from werkzeug.utils import secure_filename
import json
import subprocess

main = Blueprint('main', __name__)

@main.route('/add_algorithm', methods=['POST'])
def add_algorithm():
    algo_data = request.form

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

    selectedFile = request.files['selectedFile']
    filename = str(new_algo.id) + ".zip"
    selectedFile.save(filename)
    subprocess.run(["unzip", filename])

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
    return json.dumps(data)

@main.route('/solve-challenge')
def solve_challenge():
	data = Algorithm.query.get(request.args.get('id'))
	data = {'id' : data.id, 'name' : data.name, 'type' : data.type, 'description' : data.description, 'challenge' : data.challenge, 'hint' : data.hint, 'plaintext' : data.plaintext, 'ciphertext' : data.ciphertext, 'attempts' : data.attempts, 'success' : data.success}
    # return json.dumps(data)
	return "Hello ji challenge solve karlo" + str(request.args.get('id'))

@main.route('/encrypt', methods = ['POST'])
def encrypt():
	dataa = request.form
	id = dataa['id']
	plaintext = dataa['plaintext']
	print("aa$$" + plaintext)
	# data = Algorithm.query.get(id)
	# encryptFile = data.name + "/encrypt.py"
	# res = subprocess.run(["python3", encryptFile, plaintext], stdout = subprocess.PIPE)
	# ciphertext = res.stdout.decode('utf-8')[:-1]
	ciphertext = {"ciphertext": "sexyy"}
	print(ciphertext["ciphertext"] + "is there !!!!!!!!!!!!!!!")
	return json.dumps(ciphertext)

@main.route('/decrypt', methods = ['POST'])
def decrypt():
    id = request.get_json()['id']
    ciphertext = request.get_json()['ciphertext']
    data = Algorithm.query.get(id)
    # file to run would be data.name / encrypt / plaintext
    decryptFile = data.name + "/decrypt.py"

    res = subprocess.run(["python3", decryptFile, ciphertext], stdout = subprocess.PIPE)

    plaintext = res.stdout.decode('utf-8')[:-1]

    plaintext = {"ciphertext": plaintext}
    print(plaintext + "boom")
    return json.dumps(plaintext)
