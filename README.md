# CipherForces

CipherForces is a Learning Platform for various Security Schemes where one can learn by experimenting (OJ for POIS). It is a Web app for hosting security challenges where the student can interact with different security
schemes. A Prehosted set of Challenges spanning from Ancient Ciphers to Advanced Ciphers covering concepts covered in POIS course have already been uploaded to the Web app.

# Features
  - Ability to host Problem Statements
  - Upload security algorithms
  - User specified Server Interface Access (SIA)
  - Solve Challenges
  - Keeping track of the Attempts and Successes
  - Play around with Common Security Algorithms
  - Number of attempts and success of each algorithm.

# Users
  - Teaching Assistant : 
    - Interface for Uploading Challenge 
    - Ability to use custom codes with limited interaction ability
    - Uploading Algorithms for free interaction
  - Student : 
    - Browse through chapters
    - Interact with uploaded challenge codes
    - Solve Challenges
    - Keep track of attempts and successes

# Challenge Upload
For challenge upload, the security scheme should adhere to a specific format for proper execution.
The uploaded file should be in a zip file containing a folder having the following contents:
 - encrypt.py
 - decrypt.py
 - generate_keys.py
 - keys.json
 
The above programs should have the same functionality as their names.
All the files should take a command line argument and output the respective content in the console itself without any other redundant data.

# How to Run

To run, clone the directory, then type the following commands, inside the cloned directory.

For flask app - 

```sh
$ cd flask_app
$ export FLASK_APP=__init__.py
$ pip3 -r requirements.txt
$ flask run
```

For react app - 

```sh
$ cd app
$ npm install
$ npm start
```

To create a fresh database, delete the previous database and create a fresh database using the command:
```sh
$ python3 create_db.py
```

License
-------
Copyright &copy; 2020 Cipher Forces <tanuj.garg@students.iiit.ac.in>
