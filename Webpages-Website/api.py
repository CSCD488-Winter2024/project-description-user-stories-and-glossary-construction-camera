import flask
import json
import mariadb


app = flask.Flask(__name__)
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
    cur.execute("SELECT COUNT(*) FROM users WHERE username='johndoe' AND password='Password123'")

    row_header=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]
    
    for result in rv:
        json_data.append(dict(zip(row_header,result)))
    
    return json.dumps(json_data)

@app.route('/api/adminStatus', methods=['GET'])
def check_admin_status():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("SELECT admin_status FROM users WHERE username='johndoe'")

    admin_status = cur.fetchone()

    if admin_status and admin_status[0] == 1:
        return json.dumps({'admin_status': 1}), 200
    else:
        return json.dumps({'admin_status': 0}), 200

    
    

app.run()
