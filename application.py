from flask import Flask, jsonify, request,render_template
from dataaccess  import read_from_csv,read_city_from_csv,read_state_from_csv,read_city_from_state
from wtforms import TextField, Form


# app
app = Flask(__name__)

class SearchForm(Form):
    autocomp= TextField('City',id='autocity')
    autocomp2= TextField('State',id='autostate')
# routes
@app.route('/')
def searchform():
    return render_template("index.html")

@app.route('/index')
def index():
    form = SearchForm(request.form)
    return render_template("index.html",form=form)
    

@app.route('/sample')
def sample():
    return render_template("sample.html")

@app.route("/chart")
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart.html', values=values, labels=labels, legend=legend)

# @app.route('/', methods=['GET'])
# def hello():
#     return "Get list of Covid-19 testing Labs in US"
    
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

@app.route('/getcityfromstate', methods=['GET'])
def get_city_from_state_list():
    data = request.args.get('state') 
    result = read_city_from_state(data)
    return jsonify(results=result)

@app.route('/getcovidstatedata', methods=['GET'])
def getcovidstatedata():
      


if __name__ == '__main__':
    app.run(port = 5000, debug=True)