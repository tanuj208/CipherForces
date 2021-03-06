from flask import Blueprint, jsonify, request
from . import db 
from .models import Algorithm
from werkzeug.utils import secure_filename
import json
import os
import subprocess
from sqlalchemy.sql import text

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
            solution = algo_data['solution'],
            level = algo_data['level'],
            attempts = 0,
            success = 0,
            allow_encrypt = algo_data['allow_encrypt'],
            allow_decrypt = algo_data['allow_decrypt']
        )
    db.session.add(new_algo)
    db.session.commit()

    selectedFile = request.files['selectedFile']
    filename = str(new_algo.id) + ".zip"
    selectedFile.save(filename)
    subprocess.run(["mkdir", str(new_algo.id)])
    subprocess.run(["mv", filename, str(new_algo.id)])
    os.chdir(str(new_algo.id))
    subprocess.run(["unzip", filename])
    folder_name = ''
    for file_name in os.listdir('.'):
        if not os.path.isfile(file_name):
            folder_name = file_name
            subprocess.run(['mv', file_name, '../'])
    os.chdir('../')
    subprocess.run(['rm', '-rf', str(new_algo.id)])
    subprocess.run(['mv', folder_name, str(new_algo.id)])

    return 'Algorithm Added Successfully', 201

@main.route('/algorithms')
def algorithms():
    data = Algorithm.query.all()
    all_rows = [{'id' : row.id, 'name' : row.name, 'type' : row.type, 'description' : row.description, 'challenge' : row.challenge, 'hint' : row.hint, 'solution' : row.solution, 'attempts' : row.attempts, 'success' : row.success, 'level' : row.level} for row in data]
    return json.dumps(all_rows)

@main.route('/get_algo')
def get_algo():
    data = Algorithm.query.get(request.args.get('id'))
    data = {'id' : data.id, 'name' : data.name, 'type' : data.type, 'description' : data.description, 'challenge' : data.challenge, 'hint' : data.hint, 'solution' : data.solution, 'attempts' : data.attempts, 'success' : data.success, 'level' : data.level, 'allow_encrypt' : data.allow_encrypt, 'allow_decrypt' : data.allow_decrypt}
    return json.dumps(data)

@main.route('/update_attempts')
def update_attempts():
	data = Algorithm.query.filter(text('id==' + str(request.args.get('id')))).first()
	data.attempts += 1
	db.session.commit()
	return "done"

@main.route('/update_success')
def update_success():
    data = Algorithm.query.filter(text('id==' + str(request.args.get('id')))).first()
    data.success += 1
    db.session.commit()
    return "done"

@main.route('/get_algo_level')
def get_algo_level():
    data = Algorithm.query.filter(text('level==' + str(request.args.get('level')))).all()
    data = [{'id' : row.id, 'name' : row.name, 'type' : row.type, 'description' : row.description, 'challenge' : row.challenge, 'hint' : row.hint, 'solution' : row.solution, 'attempts' : row.attempts, 'success' : row.success, 'level' : row.level} for row in data]
    return json.dumps(data)

@main.route('/get_level_count')
def get_level_count():
    data = Algorithm.query.filter(text('level==' + str(request.args.get('level')))).count()
    return str(data)

@main.route('/solve-challenge')
def solve_challenge():
	data = Algorithm.query.get(request.args.get('id'))
	data = {'id' : data.id, 'name' : data.name, 'type' : data.type, 'description' : data.description, 'challenge' : data.challenge, 'hint' : data.hint, 'solution' : data.solution, 'attempts' : data.attempts, 'success' : data.success, 'level' : data.level}
    # return json.dumps(data)
	return "Hello ji challenge solve karlo" + str(request.args.get('id'))

@main.route('/encrypt', methods = ['POST'])
def encrypt():
    dataa = request.form
    id = dataa['id']
    plaintext = dataa['plaintext']
    os.chdir(str(id))
    encryptFile = "encrypt.py"
    res = subprocess.run(["python3", encryptFile, plaintext], stdout = subprocess.PIPE)
    ciphertext = res.stdout.decode('utf-8')[:-1]
    ciphertext = {"ciphertext": ciphertext}
    os.chdir('..')
    return json.dumps(ciphertext)

@main.route('/decrypt', methods = ['POST'])
def decrypt():
    dataa = request.form
    id = dataa['id']
    ciphertext = dataa['ciphertext']
    # file to run would be data.name / encrypt / plaintext
    os.chdir(str(id))
    decryptFile = "decrypt.py"

    res = subprocess.run(["python3", decryptFile, ciphertext], stdout = subprocess.PIPE)

    plaintext = res.stdout.decode('utf-8')[:-1]

    plaintext = {"plaintext": plaintext}
    os.chdir('..')
    return json.dumps(plaintext)
