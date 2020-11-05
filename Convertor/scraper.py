

import pandas as pd
import requests
import time

# Import Dataset
data = pd.read_csv("Dataset.csv")
processed_data = []
print(data)

# Define 2 Arrays to store the latitudes and longitudes
latitudes = []
longitudes = []

# Builds the link
def buildUrl(addrs):
    return f"https://developers.onemap.sg/commonapi/search?searchVal={addrs}&returnGeom=Y&getAddrDetails=Y&pageNum=1"



def saveData():
    data.to_csv("dataset_with_ALLLatLong.csv", index=True)
    print("Dataset Saved!")



def processData(json):
    # gets the json data from the scraping
    # The json has a result array whicb contains all the properties of the address
    try:
        result = json['results'][0]
        addrs_lat = result['LATITUDE']
        addrs_long = result['LONGITUDE']
        
    except IndexError:
        addrs_lat = "null"
        addrs_long = "null"
    latitudes.append(addrs_lat)
    longitudes.append(addrs_long)

limit = len(data)

def main():
    # Loops through all the rows in the csv file
    for item in range(0, limit):
        start = time.time()
        print(f"{item}/{len(data)}")
        try:
            # gets the value in the 'Full Address column'
            address = data["Full Address"][item]
            # Gets the link builder by passing the address value into the function to build the url with the values of the address
            r = requests.get(buildUrl(address))
            # Sends the json data returned from the request to be processed to get the data we want
            processData(r.json())
            time_taken = time.time() - start
            print(f"Process took: {time_taken:.2f} seconds.\n\n")
        except:
            latitudes.append("null")
            longitudes.append("null")
        
        # time.sleep(0.5)
    for item in range(limit, len(data)):
        latitudes.append("Null")
        longitudes.append("Null")
    # Adding the array of latitudes into a new column called 'Latitudes' in the file
    data["Latitudes"] = latitudes
    # Adding the array of Longitudes into a new colum called 'Longitudes'
    data["Longitudes"] = longitudes

    # print(data)
    saveData()



main()


