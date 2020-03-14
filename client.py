#Refrence from the following link
#https://towardsdatascience.com/create-an-api-to-deploy-machine-learning-models-using-flask-and-heroku-67a011800c50
import json
import requests

def test_response():
    # local url
    url = 'http://127.0.0.1:5000/getlist' # change to your url
    # url = 'https://rbgautammlapi.herokuapp.com/predict' # change to your url
    # sample data
    data = {'state': None
        , 'city': 'cas'
        }
    data = json.dumps(data)
    send_request = requests.post(url,data)
    # print(results)
    res_data = send_request.json()
    # results= res_data['results']
    print(res_data)
    # print(results['city'],",",results['state'])

if __name__== "__main__":
  test_response()