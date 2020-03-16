import pandas as pd
import googlemaps
from datetime import datetime
import csv
import json
#pip install -U googlemaps

def convert_to_csv():
    read_file = pd.read_excel ('labs_list.xlsx')
    read_file.to_csv ('us_labs.csv', index = None, header=True)

def get_address_from_google(address):
    gmaps = googlemaps.Client(key='[REPLACE_WITH_KEY]')
    # Geocoding an address
    geocode_result = gmaps.geocode(address)
    if len(geocode_result)>0:
        geo_json = geocode_result[0]
        geo_geometry = geo_json["geometry"]
        geo_loc = geo_geometry["location"]
        address_components = geo_json["address_components"]
        address_components_zip = address_components[len(address_components)-1]
        print(address_components)
        print(geo_json["formatted_address"],",",address_components_zip["long_name"],",",geo_loc["lat"],",",geo_loc["lng"])
        return geo_json["formatted_address"],address_components_zip["long_name"],geo_loc["lat"],geo_loc["lng"]
    else:
        return "","","",""

def create_csv_with_address_data():
    file_path = "us_labs.csv"
    csv_data = pd.read_csv(file_path)

    with open(file_path,mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                csv_fileName = "us_labs_data.csv"
                # write_to_csv(csv_fileName,"","","" ,"","","","" ,"","", True )
                for row in csv_reader:
                    line_count += 1
                    if row["City"] != "None":
                        address = row["Laboratory Name"]+", "+row["City"]+", "+row["State"]
                    else:
                        address = row["Laboratory Name"]+","+row["State"]
                    Formatted_address,Zip_code,lat,lng = get_address_from_google(address)
                    write_to_csv(csv_fileName,row["CLIA Number"],row["Laboratory Name"],row["Certificate"] ,row["City"],row["State"],Formatted_address,Zip_code,lat,lng,False)
                    print(line_count,", ",address)

def write_to_csv(csv_fileName,CLIANumber,LaboratoryName,Certificate ,City,State,Formatted_address,Zip_code,lat,lng, Is_Header ):

        with open(csv_fileName, mode='a',newline='') as dll_file:
                fieldnames = ["CLIA Number","Laboratory Name","Certificate" ,"City","State","Formatted_address","Zip_code","lat","lng"]
                writer = csv.writer(dll_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                if(not Is_Header):
                        
                        writer.writerow([CLIANumber,LaboratoryName,Certificate ,City,State,Formatted_address,Zip_code,lat,lng])
                if(Is_Header):
                        writer.writerow(fieldnames)

if __name__ == "__main__":
    get_address_from_google('COPPE LABORATORIES,WI,USA')
    #create_csv_with_address_data()