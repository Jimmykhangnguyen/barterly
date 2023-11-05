from flask import Flask, request, jsonify
import psycopg2
import pandas as pd
import numpy as np
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Replace these with your database credentials
db_config = {
    'host': '34.31.57.71',
    'port': '5432',  # Default PostgreSQL port
    'user': 'charles',
    'password': 'charlesnh2023',
    'database': 'postgres',
}

@app.route('/get_login', methods=['GET'])
def get_login():
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        usercheckquery = request.args.get('query')
        cursor.execute("SELECT password FROM users WHERE username = '{u}'".format(u=usercheckquery))
        data = cursor.fetchall()

        # df = pd.DataFrame(data, columns=["column_name_1", "column_name_2", ...])
        print(data)
        cursor.close()
        connection.close()
        return data
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/get_useritems', methods=['GET'])
def get_useritems():
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        usercheckquery = request.args.get('query')

        cursor.execute("SELECT * FROM your_table")
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM your_table")
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
