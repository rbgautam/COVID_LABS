import pandas as pd
import json

file_path = "us_labs.csv"
csv_data = pd.read_csv(file_path)

def read_from_csv(state,city):
    try:
        result = None
        if state == None and city == None:
            return None 
       
        if state != None and city == None:
            result = read_state_data(state)
            return result
        if state != None and city != None:
            result = read_state_city_data(state,city)
            return result
        if city != None:
            result =read_city_data(city)
            return result

    except Exception as ex:
        print(ex)

def read_city_data(city):
    result = csv_data[csv_data['City'].str.contains(city.upper())] 
    result = jsonify_result(result)
    print(len(result))
    if(len(result) > 0):
        return result
    return result

def read_state_data(state):
    result = csv_data.loc[(csv_data['State'] == state)]
    result = jsonify_result(result)
    print(len(result))
    if(len(result) > 0):
        return result
    return result

def read_state_city_data(state,city):
    result = csv_data.loc[(csv_data['State'] == state.upper()) & csv_data['City'].str.contains(city.upper())]
    result = jsonify_result(result)
    # print(result)
    if(len(result) > 0):
        return result

    return result

def jsonify_result(df):
    return json.loads(df.to_json(orient='records'))
if __name__ == "__main__":
    read_from_csv(None,"cas")
    
