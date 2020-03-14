import pandas as pd
from flask import Flask, jsonify, request
from dataaccess  import read_from_csv


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

    # print(data)

    # List of Labs
    result = read_from_csv(data['state'],data['city'])
    # print(result)
    # send back to browser
    output = result
    # print(output)
    # return data
    return jsonify(results=output)
    # return output

if __name__ == '__main__':
    app.run(port = 5000, debug=True)