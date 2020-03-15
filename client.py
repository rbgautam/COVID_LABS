#Refrence from the following link
#https://towardsdatascience.com/create-an-api-to-deploy-machine-learning-models-using-flask-and-heroku-67a011800c50
import json
import requests

def test_response():
    # local url
    url = 'http://127.0.0.1:5000/getlist' # change to your url
    # url = 'https://covidtestinglabsus.herokuapp.com/getlist' # change to your url
    # sample data
    #sample 1 NO Data
    # data = {'state': None
    #     , 'city': None
    #     }
    #Sample 2 State wise
    # data = {'state': "IL"
    #     , 'city': None
    #     }
    #Sample 3 City wise looks for pattern in city names
    # data = {'state': "IL"
    #     , 'city': "chi"
    #     }
    #Sample 4 City wise looks for pattern in city names
    data = {'state': None
        , 'city': "chicago"
        }
    data = json.dumps(data)
    send_request = requests.post(url,data)
    # print(results)
    res_data = send_request.json()
    # results= res_data['results']
    print(res_data)
    # print(results['city'],",",results['state'])
def test_city_response():
    # local url
    # url = 'http://127.0.0.1:5000/getcity?city=nap' # change to your url
    url = 'https://covidtestinglabsus.herokuapp.com/getcity?city=ALL' # change to your url
    send_request = requests.get(url)
    # print(results)
    res_data = send_request.json()
    # results= res_data['results']
    print(res_data)
    # print(results['city'],",",results['state'])
def test_state_response():
    # local url
    # url = 'http://127.0.0.1:5000/getstate?state=ALL' # change to your url
    url = 'https://covidtestinglabsus.herokuapp.com/getstate?state=ALL' # change to your url
    send_request = requests.get(url)
    # print(results)
    res_data = send_request.json()
    # results= res_data['results']
    print(res_data)
    # print(results['city'],",",results['state'])
def test_city_state_response():
    # local url
    url = 'http://127.0.0.1:5000/getcityfromstate?state=ia' # change to your url
    # url = 'https://covidtestinglabsus.herokuapp.com/getstate?state=ALL' # change to your url
    send_request = requests.get(url)
    # print(results)
    res_data = send_request.json()
    # results= res_data['results']
    print(res_data)
    # print(results['city'],",",results['state'])
if __name__== "__main__":
  test_response()