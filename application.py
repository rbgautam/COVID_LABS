import pandas as pd
from flask import Flask, jsonify, request
from dataaccess  import read_from_csv,read_city_from_csv,read_state_from_csv


# app
app = Flask(__name__)

# routes
@app.route('/', methods=['GET'])
def hello():
    return "Get list of Covid-19 testing Labs in US"
    
@app.route('/getlist', methods=['POST'])

def get_list():
    # get data
    data = request.get_json(force=True)

    print(data)

    # List of Labs
    result = read_from_csv(data['state'],data['city'])
    # print(result)
    # send back to browser
    output = result
    # print(output)
    # return data
    return jsonify(results=output)
@app.route('/getcity', methods=['GET'])
def get_city_list():
    print(type(request.args))
    
    data = request.args.get('city')    
    if data == 'ALL':
        data = None
    # print(data)
    # List of Labs
    result = read_city_from_csv(data)
    # print(result)
    # send back to browser
    output = result
    # print(output)
    # return data
    return jsonify(results=output)

@app.route('/getstate', methods=['GET'])
def get_state_list():
    data = request.args.get('state') 
    if data == 'ALL':
        data = None   
    # print(data)
    # List of Labs
    result = read_state_from_csv(data)
    # print(result)
    # send back to browser
    output = result
    # print(output)
    # return data
    return jsonify(results=output)
if __name__ == '__main__':
    app.run(port = 5000, debug=True)