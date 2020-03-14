import pandas as pd
file_path = "us_labs.csv"
csv_data = pd.read_csv(file_path)

def read_from_csv(state,city):
    try:
        if state == None and city == None:
            return None 
        if city != None:
            return read_city_data(city)
        if state != None and city == None:
            return read_state_data(state)
        if state != None and city != None:
            return read_state_city_data(state,city)

    except Exception as ex:
        print(ex)

def read_city_data(city):
    result = csv_data[csv_data['City'].str.contains(city.upper())] 
    # print(result)
    return result

def read_state_data(state):
    result = csv_data.loc[(csv_data['State'] == state)]
    # print(result)
    return result

def read_state_city_data(state,city):
    result = csv_data.loc[(csv_data['State'] == state) & (csv_data['City'] == city.upper())]
    return result
if __name__ == "__main__":
    read_from_csv("IL",None)
    
