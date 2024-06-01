import flask
import json
import mariadb
from flask import Flask
from flask_cors import CORS
from flask import request
from flask import redirect


app = flask.Flask(__name__)
CORS(app)
CORS(app, origins='*')
app.config["DEBUG"] = True


config = {
    'host': '0.0.0.0',
    'port': 3306,
    'user': 'root',
    'password': 'Password123!',
    'database': 'employees'
}


@app.route('/api/loginConfirm', methods=['GET'])
def index():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    username = request.args.get('username')
    password = request.args.get('password')
    cur.execute("SELECT COUNT(*) FROM users WHERE username=%s AND password=%s", (username, password))

    row_header=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]
    
    for result in rv:
        json_data.append(dict(zip(row_header,result)))

    if json_data[0]['COUNT(*)'] > 0:
        return redirect('http://localhost:8000/videoPage.html')
    else:
        return "User or Password Incorrect"




@app.route('/api/changeUsername', methods=['GET'])
def change_username():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    curUsername = request.args.get('curUsername')
    newUsername = request.args.get('newUsername')
    cur.execute("UPDATE users SET username=%s WHERE username=%", (newUsername, curUsername))

@app.route('/api/changePassword', methods=['GET'])
def change_password():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    curPassword = request.args.get('curPassword')
    newPassword = request.args.get('newPassword')
    cur.execute("UPDATE users SET password=%s WHERE password=%s", (newPassword, curPassword))


@app.route('/api/changeEmail', methods=['GET'])
def change_email():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    curEmail = request.args.get('curEmail')
    newEmail = request.args.get('newEmail')
    cur.execute("UPDATE users SET email=%s WHERE email=%s", (newEmail, curEmail))   

@app.route('/api/changePhoneNumber', methods=['GET'])
def change_phone():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    curPhoneNumber = request.args.get('curPhoneNumber')
    newPhoneNumber = request.args.get('newPhoneNumber')
    cur.execute("UPDATE users SET phone_number=%s WHERE phone_number=%s", (newPhoneNumber, curPhoneNumber))
   




@app.route('/api/fetchUserData', methods=['GET'])
def fetch_user_profile():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    username = request.args.get('username')
    cur.execute("SELECT name, email, phone_number FROM users WHERE username=%s", (username,))

    profile_data = cur.fetchone()

    if profile_data:
        profile = {
            'name': profile_data[0],
            'email': profile_data[1],
            'phone_number': profile_data[2]
        }
        return json.dumps(profile), 200
    else:
        return "User not found", 404


@app.route('/api/deleteUser', methods=["GET"])
def delete_user():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    data = request.json
    email = data('email')
    password = data('password')
    username = request.args.get('username')
    cur.execute("DELETE FROM users WHERE email=%s AND WHERE password=%s", (email, password))
    conn.commit()
    conn.close()
    return jsonify({'success': True})



@app.route('/api/updateUserData', methods=['POST'])
def update_user_data():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    field = data['field']
    value = data['value']
    username = request.args.get('username')

    if field == 'username':
        cur.execute("UPDATE users SET username=%s WHERE username=%s", (value, username))
    elif field == 'password':
        cur.execute("UPDATE users SET password=%s WHERE username=%s", (password, username))
    elif field == 'email':
        cur.execute("UPDATE users SET email=%s WHERE username=%s", (value, username))
    elif field == 'phone_number':
        cur.execute("UPDATE users SET phone_number=%s WHERE username=%s", (value, username))
    else:
        return jsonify({'success': False, 'message': 'Invalid field'})

    conn.commit()
    conn.close
    return jsonify({'success': True})



app.run()
