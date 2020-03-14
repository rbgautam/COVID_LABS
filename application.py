import pandas as pd
from flask import Flask, jsonify, request



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

    # predictions
    # result = model.predict(data_df)

    # send back to browser
    output = data

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)