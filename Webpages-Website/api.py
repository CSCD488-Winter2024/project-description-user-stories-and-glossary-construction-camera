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

app.run()
