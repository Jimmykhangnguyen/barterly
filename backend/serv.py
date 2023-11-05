from flask import Flask, request, jsonify
import psycopg2
import pandas as pd
import numpy as np
import json
from flask_cors import CORS
import datetime

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
        cursor.execute("SELECT password, name FROM users WHERE username = '{u}'".format(
            u=usercheckquery))
        data = cursor.fetchall()

        # df = pd.DataFrame(data, columns=["column_name_1", "column_name_2", ...])

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

        cursor.execute(
            "SELECT * FROM users WHERE username = '{u}';".format(u=usercheckquery))
        data = cursor.fetchall()
        cursor.execute(
            "SELECT * FROM product WHERE username = '{u}';".format(u=usercheckquery))
        data = data + cursor.fetchall()

        cursor.close()
        connection.close()

        return data
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_recommended', methods=['GET'])
def get_recommended():
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM product LIMIT 0")
        prod_column_names = [desc[0] for desc in cursor.description]
        cursor.execute(
            "SELECT * FROM transactions LIMIT 0")
        trans_column_names = [desc[0] for desc in cursor.description]

        cursor.execute(
            "SELECT * FROM product")
        data = cursor.fetchall()
        df_prods = pd.DataFrame(data, columns=prod_column_names)
        cursor.execute(
            "SELECT * FROM transactions")
        data = cursor.fetchall()
        df_trans = pd.DataFrame(data, columns=trans_column_names)

        cursor.close()
        connection.close()

        # add new columns to df_prods dataframe
        df_prods["rate_acc"] = len(df_prods)*[0]
        df_prods["rate_count"] = len(df_prods)*[0]
        df_prods["rate_avg"] = len(df_prods)*[0]

        # fill rate_acc and rate_count columns by parsing through transactions
        for i in range(len(df_trans)):
            item_ind = df_prods.index[df_prods['item']
                                      == df_trans['itemg'][i]].tolist()

            df_prods.loc[item_ind[0], 'rate_acc'] += df_trans['ratingg'][i]
            df_prods.loc[item_ind[0], 'rate_count'] += 1

            item_ind = df_prods.index[df_prods['item']
                                      == df_trans['itemr'][i]].tolist()
            df_prods.loc[item_ind[0], 'rate_acc'] += df_trans['ratingr'][i]
            df_prods.loc[item_ind[0], 'rate_count'] += 1

        # fill rate_avg
        df_prods['rate_avg'] = df_prods['rate_acc'].divide(
            df_prods['rate_count'])

        m = 1  # minimum rate count to be used
        C = df_prods['rate_avg'].mean()

        def weighted_rating(x, m=m, C=C):
            v = x['rate_count']
            R = x['rate_avg']
            return (v/(v+m) * R) + (m/(m+v) * C)

        df_prods['score'] = df_prods.apply(weighted_rating, axis=1)

        # rank df_prods based on score
        df_prods = df_prods.sort_values('score', ascending=False)

        # print the top 5 most highly rated items
        data = df_prods[['username', 'item', 'condition',
                         'listlocation']].head(5).to_numpy().tolist()

        return data
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_marketplace', methods=['GET'])
def get_marketplace():
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM product LIMIT 0")
        prod_column_names = [desc[0] for desc in cursor.description]
        cursor.execute(
            "SELECT * FROM transactions LIMIT 0")
        trans_column_names = [desc[0] for desc in cursor.description]

        cursor.execute(
            "SELECT * FROM product")
        data = cursor.fetchall()
        df_prods = pd.DataFrame(data, columns=prod_column_names)
        cursor.execute(
            "SELECT * FROM transactions")
        data = cursor.fetchall()
        df_trans = pd.DataFrame(data, columns=trans_column_names)

        cursor.close()
        connection.close()

        # add new columns to df_prods dataframe
        df_prods["rate_acc"] = len(df_prods)*[0]
        df_prods["rate_count"] = len(df_prods)*[0]
        df_prods["rate_avg"] = len(df_prods)*[0]

        # fill rate_acc and rate_count columns by parsing through transactions
        for i in range(len(df_trans)):
            item_ind = df_prods.index[df_prods['item']
                                      == df_trans['itemg'][i]].tolist()

            df_prods.loc[item_ind[0], 'rate_acc'] += df_trans['ratingg'][i]
            df_prods.loc[item_ind[0], 'rate_count'] += 1

            item_ind = df_prods.index[df_prods['item']
                                      == df_trans['itemr'][i]].tolist()
            df_prods.loc[item_ind[0], 'rate_acc'] += df_trans['ratingr'][i]
            df_prods.loc[item_ind[0], 'rate_count'] += 1

        # fill rate_avg
        df_prods['rate_avg'] = df_prods['rate_acc'].divide(
            df_prods['rate_count'])

        m = 1  # minimum rate count to be used
        C = df_prods['rate_avg'].mean()

        def weighted_rating(x, m=m, C=C):
            v = x['rate_count']
            R = x['rate_avg']
            return (v/(v+m) * R) + (m/(m+v) * C)

        df_prods['score'] = df_prods.apply(weighted_rating, axis=1)

        # rank df_prods based on score
        df_prods = df_prods.sort_values('score', ascending=False)

        # print the top 5 most highly rated items
        data = df_prods[['username', 'item', 'condition',
                         'listlocation']].to_numpy().tolist()

        return data
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/add_user', methods=['GET'])
def add_user():
    try:
        # returns 1 if success, 0 if taken email or username, -1 otherwise
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        query_list = request.args.get('query').split("+")
        query_list = query_list[0].split(" ")

        if (len(query_list) > 6):
            return []

        username = query_list[0]
        email = query_list[1]

        cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
        emaillen = len(cursor.fetchall())
        cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
        usernamelen = len(cursor.fetchall())

        if (emaillen > 0 or usernamelen > 0):
            return []

        password = query_list[2]
        mailaddress = query_list[3].replace("_", " ")
        location = query_list[4].replace("_", " ")
        name = query_list[5].replace("_", " ")

        current_datetime = datetime.datetime.now()

        Yr = current_datetime.year
        Mn = current_datetime.month
        Dt = current_datetime.day

        datejoined = f"{Yr}-{Mn}-{Dt}"

        posgresquery = "INSERT INTO users (username, email, password, name, rating, numtransactions, mailaddress, location, joineddate)\n" + \
            "VALUES\n" + \
            f"('{username}', '{email}', '{password}', '{name}', '0', '0', '{mailaddress}', '{location}', '{datejoined}')"

        cursor.execute(posgresquery)
        connection.commit()

        cursor.close()
        connection.close()
        return [1]

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/add_item', methods=['GET'])
def add_item():
    try:
        # returns 1 if success, 0 if taken email or username, -1 otherwise
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        query_list = request.args.get('query').split("+")
        query_list = query_list[0].split(" ")

        if (len(query_list) > 6):
            return []

        username = query_list[0]
        email = query_list[1]

        cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
        emaillen = len(cursor.fetchall())
        cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
        usernamelen = len(cursor.fetchall())

        if (emaillen > 0 or usernamelen > 0):
            return []

        password = query_list[2]
        mailaddress = query_list[3].replace("_", " ")
        location = query_list[4].replace("_", " ")
        name = query_list[5].replace("_", " ")

        current_datetime = datetime.datetime.now()

        Yr = current_datetime.year
        Mn = current_datetime.month
        Dt = current_datetime.day

        datejoined = f"{Yr}-{Mn}-{Dt}"

        posgresquery = "INSERT INTO users (username, email, password, name, rating, numtransactions, mailaddress, location, joineddate)\n" + \
            "VALUES\n" + \
            f"('{username}', '{email}', '{password}', '{name}', '0', '0', '{mailaddress}', '{location}', '{datejoined}')"

        cursor.execute(posgresquery)
        connection.commit()

        cursor.close()
        connection.close()
        return [1]

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
