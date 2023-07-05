from flask import Flask, request, jsonify

from db import Db_manager

#Create a Flask application instance:
app = Flask(__name__)
db = Db_manager()

@app.route('/api/data', methods=['GET'])
def get_data():
    db.db_connect()
    results = db.db_query("SELECT * FROM ktk_table LIMIT 5000")
    return jsonify(results)

@app.route('/api/sales', methods=['GET'])
def get_data_sales():
    db.db_connect()
    res = db.db_query("SELECT CON_NOM_EMPRESA, CON_CANTIDAD FROM ktk_table LIMIT 5000")

    data_dict = {}

    for i in res:
        if i[0] in data_dict:
            data_dict[i[0]] = data_dict[i[0]] + i[1]
        else:
            data_dict[i[0]] = i[1]

    return jsonify(data_dict)

@app.route('/api/citylist', methods=['GET'])
def get_data_city():
    db.db_connect()
    query = "SELECT CON_NOM_EMPRESA, CON_CANTIDAD, CON_NOM_CIUDAD FROM ktk_table LIMIT 5000"
    res = db.db_query(query)

    city_list = []
    for i in res:
        if i[2] not in city_list:
            city_list.append(i[2])

    return jsonify(city_list)

@app.route('/api/city/<string:_city>', methods=['GET'])
def get_data_sales_city(_city):
    db.db_connect()
    query = "SELECT CON_NOM_EMPRESA, CON_CANTIDAD FROM ktk_table WHERE CON_NOM_CIUDAD = %s LIMIT 5000"
    res = db.db_val_query(query,_city)

    data_dict = {}

    for i in res:
        if i[0] in data_dict:
            data_dict[i[0]] = data_dict[i[0]] + i[1]
        else:
            data_dict[i[0]] = i[1]

    return jsonify(data_dict)

@app.route('/api/monthlist', methods=['GET'])
def get_data_month():
    db.db_connect()
    query = "SELECT CON_NOM_EMPRESA, CON_CANTIDAD, CON_MES FROM ktk_table LIMIT 5000"
    res = db.db_query(query)

    month_list = []
    for i in res:
        if i[2] not in month_list:
            month_list.append(i[2])

    return jsonify(month_list)

@app.route('/api/month/<string:_month>', methods=['GET'])
def get_data_sales_month(_month):
    db.db_connect()
    query = "SELECT CON_NOM_EMPRESA, CON_CANTIDAD FROM ktk_table WHERE CON_MES = %s LIMIT 5000"
    res = db.db_val_query(query,_month)

    data_dict = {}

    for i in res:
        if i[0] in data_dict:
            data_dict[i[0]] = data_dict[i[0]] + i[1]
        else:
            data_dict[i[0]] = i[1]

    return jsonify(data_dict)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)