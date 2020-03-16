import pandas as pd
import json

file_path = "us_labs_data.csv"
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
        if state == None and city != None:
            result = read_state_city_data(state,city)
            return result
        if city != None:
            result =read_city_data(city)
            return result

    except Exception as ex:
        print(ex)

# Returns a list of cities matching a pattern        
def read_city_from_csv(city):
    if city != None:
        result = csv_data[csv_data['City'].str.startswith(city.upper())] 
    else:
        return csv_data['City'].unique().tolist()
    result = result['City'].unique().tolist()
    # print(result)
    # result = jsonify_result(result)
    return result

def read_city_from_state(state):
    if state != None:
        result = csv_data[csv_data['State'].str.startswith(state.upper())] 
    else:
        return csv_data['City'].unique().tolist()
    result = result['City'].unique().tolist()
    # print(result)
    # result = jsonify_result(result)
    return result

# Returns a list of states matching a pattern        
def read_state_from_csv(state):
    if state != None:
        result = csv_data[csv_data['State'].str.startswith(state.upper())] 
    else:
        return csv_data['State'].unique().tolist()
    result = result['State'].unique().tolist()
    # print(result)
    # result = jsonify_result(result)
    return result

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
    if state == None:
        result = csv_data.loc[csv_data['City'].str.startswith(city.upper())]
    else:    
        result = csv_data.loc[(csv_data['State'] == state.upper()) & csv_data['City'].str.contains(city.upper())]
    
    result = jsonify_result(result)
    # print(result)
    if(len(result) > 0):
        return result

    return result

def jsonify_result(df):
    return json.loads(df.to_json(orient='records'))
if __name__ == "__main__":
    print(read_city_from_csv("chicago"))
    
